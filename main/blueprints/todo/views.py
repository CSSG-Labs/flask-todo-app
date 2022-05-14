from flask import Blueprint, render_template, current_app
from . import dao

todo_router = Blueprint('todo', __name__, template_folder='templates',  static_folder='static')

@todo_router.route("/")
def index():
    todoDAO = dao.TodoDAO(current_app.config['db'])
    # see https://flask.palletsprojects.com/en/2.1.x/blueprints/#templates
    return render_template("todo/index.html", todos=todoDAO.getAll())
