# GitHub contributions
Get details about all the projects to which you have contributed to on GitHub.

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
### Fetch list of repositories contributed to
Run the script `fetch_repos.py` along with your GitHub username to get a simple
list of repositories you've contributed to:
```
Usage:
  fetch_repos.py <user> [-r]
  fetch_repos.py -h

Options:
  -r, --reverse-order   Display the list in reverse chronological order.
  -h, --help            Display this help text.
```

#### Example
```bash
$ ./fetch_repos.py faheel
```
```
Leaflet/Leaflet
TycheOrg/Tyche
freeCodeCamp/freeCodeCamp
PowerShell/PowerShell
...
```

### Generate Markdown for contributions
Run the script `generate_markdown.py` along with your GitHub username to get a
Markdown file with either a list or table of repositories you've contributed
to:
```
Usage:
  generate_markdown.py <user> [-o <type>] [-r]
  generate_markdown.py <user> -o table [-c <cols>] [-r]
  generate_markdown.py -h

Options:
  -o <type>, --output-as <type>  Generate Markdown for either a list or a table
                                 [default: list].
  -c <cols>, --columns <cols>    Number of columns for the table [default: 3].
  -r, --reverse-order            Generate output in reverse chronological
                                 order.
  -h, --help                     Display this help text.
```

The generated Markdown files are saved in a directory named `output` respective
to the directory from where the script was run.

#### List example
```bash
$ ./generate_markdown.py faheel
$ cat output/contribution-list.md
```
```markdown
* [Leaflet/**Leaflet**](https://github.com/Leaflet/Leaflet/commits?author=faheel)
* [TycheOrg/**Tyche**](https://github.com/TycheOrg/Tyche/commits?author=faheel)
* [freeCodeCamp/**freeCodeCamp**](https://github.com/freeCodeCamp/freeCodeCamp/commits?author=faheel)
* [PowerShell/**PowerShell**](https://github.com/PowerShell/PowerShell/commits?author=faheel)
...
```
which would be rendered on GitHub as:
* [Leaflet/**Leaflet**](https://github.com/Leaflet/Leaflet/commits?author=faheel)
* [TycheOrg/**Tyche**](https://github.com/TycheOrg/Tyche/commits?author=faheel)
* [freeCodeCamp/**freeCodeCamp**](https://github.com/freeCodeCamp/freeCodeCamp/commits?author=faheel)
* [PowerShell/**PowerShell**](https://github.com/PowerShell/PowerShell/commits?author=faheel)
* [NuGetPackageExplorer/**NuGetPackageExplorer**](https://github.com/NuGetPackageExplorer/NuGetPackageExplorer/commits?author=faheel)
* [DjangoGirls/**tutorial-extensions**](https://github.com/DjangoGirls/tutorial-extensions/commits?author=faheel)

#### Table example
```bash
$ ./generate_markdown.py faheel -o table
$ cat output/contribution-table.md
```
```HTML
<table>
<tr>
<td>
  <a href="https://github.com/Leaflet/Leaflet/commits?author=faheel">
    Leaflet/<b>Leaflet</b>
  </a>
</td>
<td>
  <a href="https://github.com/TycheOrg/Tyche/commits?author=faheel">
    TycheOrg/<b>Tyche</b>
  </a>
</td>
...
```
which would be rendered on GitHub as:
<table>
<tr>
<td>
  <a href="https://github.com/Leaflet/Leaflet/commits?author=faheel">
    Leaflet/<b>Leaflet</b>
  </a>
</td>
<td>
  <a href="https://github.com/TycheOrg/Tyche/commits?author=faheel">
    TycheOrg/<b>Tyche</b>
  </a>
</td>
<td>
  <a href="https://github.com/freeCodeCamp/freeCodeCamp/commits?author=faheel">
    freeCodeCamp/<b>freeCodeCamp</b>
  </a>
</td>
</tr>

<tr>
<td>
  <a href="https://github.com/PowerShell/PowerShell/commits?author=faheel">
    PowerShell/<b>PowerShell</b>
  </a>
</td>
<td>
  <a href="https://github.com/NuGetPackageExplorer/NuGetPackageExplorer/commits?author=faheel">
    NuGetPackageExplorer/<b>NuGetPackageExplorer</b>
  </a>
</td>
<td>
  <a href="https://github.com/DjangoGirls/tutorial-extensions/commits?author=faheel">
    DjangoGirls/<b>tutorial-extensions</b>
  </a>
</td>
</tr>
</table>

## License
This project is licensed under the terms of the [MIT license](LICENSE).
