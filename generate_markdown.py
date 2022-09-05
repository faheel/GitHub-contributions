#! venv/bin/python3

'''
Generates Markdown for the repositories to which a user has contributed to on
GitHub.

Usage:
  generate_markdown.py <user> [-o <type>] [-r] [-a]
  generate_markdown.py <user> -o table [-c <cols>] [-r] [-a]
  generate_markdown.py -h

Options:
  -o <type>, --output-as <type>  Generate Markdown for either a list or a table
                                 [default: list].
  -c <cols>, --columns <cols>    Number of columns for the table [default: 3].
  -a, --append                   Append to file.
  -r, --reverse-order            Generate output in reverse chronological
                                 order.
  -h, --help                     Display this help text.
'''

import os
from docopt import docopt
from fetch_repos import get_repo_list

TABLE_CELL = '''\
<td>
  <a href="https://github.com/{repo}/commits?author={user}">
    {owner}/<b>{repo_name}</b>
  </a>
</td>
'''

LIST_ITEM = '''\
* [{owner}/**{repo_name}**](https://github.com/{repo}/commits?author={user})
'''


def output_list(user, repo_list, output_file, mode):
    with open(output_file, mode) as file:
        for repo in repo_list:
            owner, repo_name = repo.split("/")
            file.write(LIST_ITEM.format(user=user, repo=repo, owner=owner,
                       repo_name=repo_name))
        print("Markdown for contribution list written to '{}'"
              .format(output_file))


def output_table(user, repo_list, num_columns, output_file, mode):
    with open(output_file, mode) as file:
        file.write("<table>\n<tr>\n")
        repos_written = 0
        for repo in repo_list:
            owner, repo_name = repo.split("/")
            if repos_written and repos_written % num_columns == 0:
                file.write("</tr>\n\n<tr>\n")
            file.write(TABLE_CELL.format(user=user, repo=repo, owner=owner,
                       repo_name=repo_name))
            repos_written += 1
        file.write("</tr>\n<table>\n")
        print("Markdown for contribution table written to '{}'"
              .format(output_file))


if __name__ == '__main__':
    arguments = docopt(__doc__)

    mode = "a" if arguments['--append'] else "w"
    user = arguments['<user>']
    repo_list = get_repo_list(user)
    if repo_list:
        if arguments['--reverse-order']:
            repo_list.reverse()
        output_as = arguments['--output-as']
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        output_file = os.path.join(output_dir, "contribution-" + output_as +
                                   ".md")
        if output_as == 'list':
            output_list(user, repo_list, output_file, mode)
        elif output_as == 'table':
            num_columns = int(arguments['--columns'])
            output_table(user, repo_list, num_columns, output_file, mode)
        else:
            print("Invalid value for output type! Possible values: 'list', "
                  "'table'")
