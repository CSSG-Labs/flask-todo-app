
# Contributing
## How to participate

    Assign yourself to an open git issue
        To suggest a new feature or bugfix:
            Check it does not already exist first! If it doesn't then:
            Open github issue
            Label it accordingly
            Discuss with project members on discord or through github
    Create a branch with <issue-number>-<branch-descriptor> naming scheme 
    Work on assigned issue
        Try not to go outside the scope of the git issue
            discuss with project members if you end up having to implement new features outside of the original scope
    Sync branch with dev
    Create remote branch and push to that branch
    Start the pull request process

## Git workflow: Issue branch workflow

    Branches are created from issues/ tasks
    Branches have the same name of its issue id#
    One Branch per issue and one issue per branch
    see article

## Coding Style

todo...

## Development Environment Setup

Instructions are written with Windows vscode users in mind...

    Create virtual environment
        python -m venv .venv
    Add path to python interpreter from new virtual environment to IDE
        Open command palette: CTRL-SHIFT-P
        Type and select Python: Select Interpreter option
        Select python.exe file inside the venv folder
        Close terminal and relaunch
        Verify venv is activated by seeing (.venv) prompt in terminal
    Install project dependencies
        pip install -r requirements.txt

Running app

    Set FLASK_APP env variable
        set FLASK_APP=run.py
    Set FLASK_ENV env variable
        set FLASK_ENV=development
    Run app
        flask run

## Testing

todo...

## Pull Request Process

    Create branch with correct naming scheme (see section)
    Ensure code is working properly and passed all tests (see section)
    Open PR (against dev branch)
    Code review must be completed by running the code and tests, and ensuring code meets our coding standards (see section)
        review is not necessary if PR is related to documentation or project maintenance
    Upon approving PR:
        Close the github issue that the PR for
        Delete PR branch
        Merge PR into dev branch (just merge PR to main if its related to documenation or project maintenance)

## Deployment

todo...