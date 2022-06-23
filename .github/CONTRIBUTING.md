# Contributing

## Getting Started

### Project setup

**Windows (_VSCode_)**
- Create virtual environment
  - `python -m venv .venv`
- Add path to python interpreter
  - Open command palette: `CTRL-SHIFT-P`
  - Type and select `Python: Select Interpreter` option
  - Open `venv` folder and select `python.exe` file
- Verify `venv` is activated 
  - should see `(.venv)` in terminal prompt
    - if not, then close terminal and relaunch it
- Install project dependencies
  - `pip install -r requirements.txt`
- Setup pre-commit hook
  - `pre-commit install`

### Running app

**Windows**
- Set `FLASK_APP` env variable
  - `$env:FLASK_APP="main"`
- Set `FLASK_ENV` env variable
  - `$env:FLASK_ENV="development"`
- Initialize database
  - `flask init-db`
- Run app
  - `flask run` or `python -m flask`

## Github Workflow
_refer to github guidelines for more info - [link](https://github.com/CSSG-Labs/flask-todo-app/wiki/Github-guidelines)

### Issues
- Please follow the suggested templates when creating an issue
- If your issue does not fit any templates, then create a blank issue

### Branching
- Branch naming convention
  - Ex: `32-add-user-auth`
  - More information: [link](https://deepsource.io/blog/git-branch-naming-conventions/)


## Coding Style

- Python coding style - [_The Hitchhikers Guide to Python_](https://docs.python-guide.org/writing/style/)_
- Violations to coding styles defined in [pre-commit-config](.pre-commit-config.yaml) will result in your commits being blocked


## Code of Conduct

*See [Contributors Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.txt)*

## Join us

Please contact andromedamoon-stack by DM on Github 
