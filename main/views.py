from flask import Blueprint, render_template

# see --> 1*
app_router = Blueprint('app', __name__, template_folder='templates', static_folder='static')

@app_router.route("/")
def home():
    return render_template("index.html")

@app_router.route("/about")
def about():
    return render_template('about.html')

# 1
# Blueprint is an object that represents a collection of routes
#  - Allows you to define routes without requiring a flask application object ahead of time
#  - flask application object will import this blueprint and register it
