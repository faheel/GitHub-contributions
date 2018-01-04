# GitHub contributions
Get a list of projects to which you have contributed to on GitHub.

## Setup
1. Clone the repo and `cd` into it.

2. Create a Python 3 virtual environment (named `venv` here):

   ```bash
   virtualenv-3 venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

## Run
Run the script `fetch_repos.py` from the `src` directory, and enter your GitHub username when prompted.
```bash
python3 src/fetch_repos.py
```

## License
This project is licensed under the terms of the [MIT license](LICENSE).
