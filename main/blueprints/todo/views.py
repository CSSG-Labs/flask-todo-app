from flask import Blueprint, render_template, current_app, request, flash, redirect, url_for, abort
from . import dao

todo_router = Blueprint('todo', __name__, template_folder='templates',  static_folder='static')

@todo_router.route("/")
def display_todos():
    db = current_app.config['DB_CONNECTION']
    todoDAO = dao.TodoDAO(db())

    # https://flask.palletsprojects.com/en/2.1.x/blueprints/#templates for why todo/index.html
    return render_template("todo/index.html", todos=todoDAO.getAll())

@todo_router.route("/add", methods=['GET', 'POST'])
def add_todos():
    db = current_app.config['DB_CONNECTION']
    todoDAO = dao.TodoDAO(db())

    if request.method == 'POST':
        desc = request.form['new_task']

        if not desc:
            print("no task entered")
            flash('Please enter a task')
            return redirect(url_for('todo.display_todos'))

        todoDAO.addOne(desc)

    return redirect(url_for('todo.display_todos'))

@todo_router.route('/<int:todo_id>/edit/', methods=['GET', 'POST'])
def edit_todo(todo_id):
    db = current_app.config['DB_CONNECTION']
    todoDAO = dao.TodoDAO(db())

    if not todo_id:
        abort(404)

    if request.method == 'POST':
        new_desc = request.form['new_desc']

        if not new_desc:
            print("no task entered")
            flash('Please enter a task')
            return render_template("todo/edit.html", todo_id=todo_id)

        todoDAO.editOne(todo_id, new_desc)
        return redirect(url_for('todo.display_todos'))

    return render_template("todo/edit.html", todo_id=todo_id)


@todo_router.route("/<int:todo_id>/delete/", methods=['GET', 'POST'])
def del_todos(todo_id):
    db = current_app.config['DB_CONNECTION']
    todoDAO = dao.TodoDAO(db())

    if request.method == 'POST':
        todoDAO.deleteOne(todo_id)

    return redirect(url_for('todo.display_todos'))

@todo_router.route("/clear", methods=['GET', 'POST'])
def del_all_todos():
    db = current_app.config['DB_CONNECTION']
    todoDAO = dao.TodoDAO(db())

    if request.method == 'POST':
        todoDAO.deleteAll()

    return redirect(url_for('todo.display_todos'))
