# __init__.py --> see 1*

import os


from flask import Flask, render_template
from .data import db

# --> see 2*
def create_app(test_config=None):
    # __name__ & instance_relative_config --> see 3*
    app = Flask(__name__, instance_relative_config=True)
    # sets default configuration for flask app (development?)
    app.config.from_mapping(
        # TODO: load from enviroment variable
        SECRET_KEY='dev',
        # app.instance.path - path to instance folder
        DATABASE=os.path.join(app.instance_path, 'main.sqlite'),
    )

    db.init_app(app)

    if test_config is None:
        # If config.py exists, then it overrides app.config.from_mapping with config.py
        # production configuration?
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config
        app.config.from_mapping(test_config)

    # checks if instance folder exists; if not then create it for sqlite file
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        return render_template('todo.html')

    @app.route("/about")
    def about():
        return render_template('about.html')

    return app

# 1
# __init__.py tells python that the `main` directory should be treated as a package
# - A python package is a collection of  modules (i.e. python files) that allow for...
#    using dot notation for modules (ex: pkg.mod1, pkg.mod2)
#
# - __init__.py is automatically invoked when the package or a module in the package...
#    is imported; so it can be used to execute code that initializes or setups the package

# 2
# `Flask` is the main application object that acts...
#    as the central registry for view functions, URL rules, template configs, and more
#
# `create_app` is the application function factory that creates the application object and...
#    handles all the configuration, registration, setup, etc for it

# 3
# `__name__`` is the name of the current python module (file)
#   - Flask app needs to know the name of the current file for relative file path configs
#
# `instance_relative_config` tells flask that sensitive configuration data such as...
#   environment variables and values are relative to the instance folder instead...
#   of the application root
#   - instance folder is for deployment specific things that should...
#      not be version controlled, such as .env files; it is located outside the app package
#      - in this app, the database sqlite file will be located in the instance directory
