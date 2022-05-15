# Contributing

## How to participate

1. Assign yourself to an open git issue
    - To suggest a new feature or bugfix:
      - Check it does not already exist first! If it doesn't then:
      - Open github issue
      - Label it accordingly
      - Discuss with project members on discord or through github
2. Create a branch with `<issue-number>-<branch-descriptor>` naming scheme [ *(see article)*](https://deepsource.io/blog/git-branch-naming-conventions/)
3. Work on assigned issue
    - Try not to go outside the scope of the git issue
      - discuss with project members if you end up having to implement new features outside of the original scope
4. Sync branch with dev
5. Create remote branch and push to that branch
6. Start the [pull request process](#pull-request=process)

## Git workflow: Issue branch workflow

- Branches are created from issues/ tasks
- Branches have the same name of its issue id#
- One Branch per issue and one issue per branch
- see [article](https://medium.com/flexisaf/git-workflow-for-your-project-3d9dbdc5f8e2)

## Coding Style

_The coding style was inspired by [The Hitchhikers Guide to Python](https://docs.python-guide.org/writing/style/)_

- General Concepts
    -Explicit Code
        - The most straighforward way of coding is prefered. 
        -Bad
         def make_complex(*args):
         x, y = args
         return dict(**locals())

        -Good

        def make_complex(x, y):
        return {'x': x, 'y': y}

    - One Statement per line
        - While there are some areas where compound statements are allowed in  general it is good practice to have one statement per line

        -Bad

            print('one'); print('two')
            if x == 1: print('one')
            if <complex comparison> and <other complex comparison>:# do something

        -Good

            print('one')
            print('two')

            if x == 1:
            print('one')

            cond1 = <complex comparison>
            cond2 = <other complex comparison>
            if cond1 and cond2:
            # do something
    - in general do your best to try and keep you code concise and clean so it is readable to everyone. For more detailed examples or if you are unsure about something please refer to the documentation linked above or reach out to one of us.


## Development Environment Setup

_Instuctions for Windows in VS Code

- Create virtual environment
  - `python -m venv .venv`
- Add path to python interpreter from new virtual environment to IDE
  - Open command palette: `CTRL-SHIFT-P`
  - Type and select `Python: Select Interpreter` option
  - Select `python.exe` file inside the `venv` folder
  - Close terminal and relaunch
  - Verify `venv` is activated by seeing `(.venv)` prompt in terminal
- Install project dependencies
  - `pip install -r requirements.txt`
- Setup pre-commit hook
  - `pre-commit install`


Linux/ MacOS
These instructions were made with VS Code in mind 

    -check to see if python is installed
        - open a new terminal if one is not already present
        - enter in terminal ' python3 --version'
        - if that dosn't work try 'python --version'
        - if you have python 2, or are missing python you will need to download and follow instructions from [Python.org](https://www.python.org/downloads/)

    -create a virtual enviroment
      - `mkdir myproject `(name it based on what project you are keeping in the folder)
      - `cd myproject` (or folder name)
      - ` python3 -m venv venv`
      - activate the enviroment with `.venv/bin/activate`
    
    -install Flask
        - once your enviroment is active type in `pip install Flask'

### Using Git to make a pull request
_Instructions on [Sachinsf.com](https://www.sachinsf.com/how-to-push-the-code-from-vs-code-to-github/)
  - Make sure you have git installed on your PC, and that all the files you are pushing are in one folder before you push any changes

### Running app

- Set `FLASK_APP` env variable
  - `$env:FLASK_APP="main"`
- Set `FLASK_ENV` env variable
  - `$env:FLASK_ENV="development"`
- Initialize database
  - `flask init-db`
- Run app
  - `flask run` or `python -m flask`
  
### Troubleshooting
- What to do if your server does not start
    - check to make sure your version of Flask is not outdated
    - check the Import name
        -The FLASK_APP environment variable is the name of the module to import at flask run. In case that module is incorrectly named you will get an import error upon start (or if debug is enabled when you navigate to the application). It will tell you what it tried to import and why it failed.The most common reason is a typo or because you did not actually create an app object.
    - if these don't resolve your issue please let one of the admins on the project know  and also refer to the [Flask_Documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

## Testing

todo...

## Pull Request Process

1. Create branch with correct naming scheme (see [section](#how-to-participate))
2. Ensure code is working properly and passed all tests (see [section](#testing))
3. Open PR (against dev branch)
4. Code review must be completed by running the code and tests, and ensuring code meets our coding standards (see [section](#coding-style))
    - *review is not necessary if PR is related to documentation or project maintenance*
5. Upon approving PR:
    - Close the github issue that the PR for
    - Delete PR branch
    - Merge PR into `dev` branch (*just merge PR to main if its related to documenation or project maintenance*)

## Deployment

_todo..._

## Code of Conduct

*See [Contributors Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.txt)*

## Join us

We are discussing this project on [discord]. Please contact andromedamoon-stack by DM on Github or riboney @ ironbe#4809 for details on our server.
