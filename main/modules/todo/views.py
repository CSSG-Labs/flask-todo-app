from flask import Blueprint, render_template

# see --> 1*
todo_router = Blueprint('todo', __name__, template_folder='templates',  static_folder='static')

@todo_router.route("/")
def home():
    return render_template("todo.html")
