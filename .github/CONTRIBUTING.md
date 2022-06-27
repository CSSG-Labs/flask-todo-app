# Contributing

- [Project Setup](#project-setup)
- [Running App](#running-app)
- [Github Workflow](#github-workflow)
  - [Issues](#issues)
  - [Branching](#feature-branching)
- [Coding Style](#coding-style)
- [Code of Conduct](#code-of-conduct)
- [Join Us](#join-us)

## Project setup

### Windows _(VSCode)_

<details>
  <summary>1. Create virtual environment</summary>
  
  - Enter `python -m venv .venv` in terminal
  - Before: 
  
    ![image](https://user-images.githubusercontent.com/14286113/175195616-4f16667a-6be9-494d-b42e-f15d4d7f41dc.png)
  - After: 
    
    ![image](https://user-images.githubusercontent.com/14286113/175196247-c5a45c4a-7291-4bda-9e06-d1dc69267f61.png)
</details>

<details>
  <summary>2. Setup Python Interpreter in IDE</summary>

  - Open command palette: `CTRL-SHIFT-P`
  - Type & select `Python: Select Interpreter`
  - Select project's `venv` folder 
  - Select `Scripts` folder
  - Select `python.exe`
  - ![image](https://user-images.githubusercontent.com/14286113/175197841-feb191eb-a8f3-42a1-a5ba-0dee5adbb3ea.png)
</details>

<details>
  <summary>3. Verify `venv` is activated</summary>
  
  - Should see `(venv)` in terminal prompt
    - If not, try ["Killing active terminal instance"](https://code.visualstudio.com/docs/editor/integrated-terminal#_managing-terminals) and relaunching the terminal  
    
  - Before

    ![image](https://user-images.githubusercontent.com/14286113/175198470-15bf291c-b52d-438f-bb36-4e6d04d28e60.png)
  - After

    ![image](https://user-images.githubusercontent.com/14286113/175198652-c3f2eb91-4490-489d-9c0a-6b445fe67d0c.png)

</details>

<details>
  <summary>4. Install project dependencies</summary>
  
  - Enter `pip install -r requirements.txt` in terminal
</details>

<details>
  <summary>5. Setup pre-commit hook</summary>
  
  - Enter `pre-commit install` in terminal
    ![image](https://user-images.githubusercontent.com/14286113/175199611-b96b93c9-ecbe-482d-afb1-41e0cbe09d01.png)

</details>

### Windows _(PyCharm)_
_todo..._

### Linux/Mac _(VSCode)_
_todo..._

### Linux/Mac _(PyCharm)_
_todo..._

## Running app

### Windows 
1. _Set app env variable:_ `$env:FLASK_APP="main"`
2. _Set environment env variable:_ `$env:FLASK_ENV="development"`
3. _Initialize database:_ `flask init-db`
4. _Run app:_ `flask run` or `python -m flask`
5. _Open_ `http://127.0.0.1:5000` in your browser to see application 

<details>
  <summary>Output</summary>
  
  ![image](https://user-images.githubusercontent.com/14286113/175203818-12a66f37-3f81-4b8e-89d8-aaa4cf8bb41b.png)
</details>

### Linux/ Mac
_todo..._

## Github Workflow
_for more info - [github guidelines](https://github.com/CSSG-Labs/flask-todo-app/wiki/Github-guidelines)_

### Issues
- Please follow the suggested templates when creating an issue
- If your issue does not fit any templates, then create a blank issue

### Feature Branching
- To add new features or address issues
  - Create or select a git issue
  - Create branch for issue
  - Push your code to your branch
  - Make PR from your branch to `main` branch

- Branch naming convention
  - Ex: `32-add-user-auth`
  - More information: [link](https://deepsource.io/blog/git-branch-naming-conventions/)

## Coding Style

- Python coding style - [_The Hitchhikers Guide to Python_](https://docs.python-guide.org/writing/style/)
- Coding style violations will be automatically blocked by pre-commit hook
  - as defined in [pre-commit-config](.pre-commit-config.yaml)


## Code of Conduct

*See [Contributors Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.txt)*

## Join us

Please contact andromedamoon-stack by DM on Github 
