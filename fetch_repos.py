#! venv/bin/python3

'''
Fetches a list of repositories to which a user has contributed to on GitHub.

Usage:
  fetch_repos.py <user> [-r]
  fetch_repos.py -h

Options:
  -r, --reverse-order   Display the list in reverse chronological order.
  -h, --help            Display this help text.
'''


import math
import requests
from docopt import docopt

API_URL = "https://api.github.com/search/issues"
RESULTS_PER_PAGE = 30


def get_results_page(author, page=1):
    # GET request parameters:
    params = {
        "q": "is:pr author:{} archived:false is:merged".format(author),
        "sort": "created",
        "order": "asc",
        "per_page": str(RESULTS_PER_PAGE),
        "page": str(page)
    }

    response = requests.get(API_URL, params=params)
    if response.status_code == requests.codes.ok:
        return response.json()

    print("Unable to get results page {}".format(page))
    print("HTTP {}".format(response.status_code))
    return None


def get_repo_list(user):
    repo_set = set()
    repo_list = list()
    results_page = get_results_page(author=user)
    if results_page:
        total_results = results_page["total_count"]
        num_pages = int(math.ceil(total_results / RESULTS_PER_PAGE))

        for page in range(1, num_pages + 1):
            if page > 1:    # page 1 has already been fetched
                results_page = get_results_page(author=user, page=page)
                if not results_page:
                    break
            for pr in results_page["items"]:
                if pr["author_association"] != "OWNER":
                    # the user is not the repo's owner
                    temp = pr["repository_url"].split("/")
                    owner, repo_name = temp[-2], temp[-1]
                    repo = owner + "/" + repo_name
                    if repo not in repo_set:
                        repo_set.add(repo)
                        repo_list.append(repo)

        return repo_list

    print("Unable to fetch repositories")
    return None


if __name__ == "__main__":
    arguments = docopt(__doc__)

    user = arguments['<user>']
    repo_list = get_repo_list(user)
    if repo_list:
        if arguments['--reverse-order']:
            repo_list.reverse()
        for repo in repo_list:
            print(repo)
