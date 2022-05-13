from flask import Blueprint, render_template

# see --> 1*
todo_router = Blueprint('todo', __name__, template_folder='templates',  static_folder='static')

@todo_router.route("/")
def home():
    # see link for why we nest index.html inside todo folder
    # https://flask.palletsprojects.com/en/2.1.x/blueprints/#templates
    return render_template("todo/index.html")
