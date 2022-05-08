# SQLite connection

import sqlite3
# creates CLI commands
import click

# current_app & g --> see 1*
from flask import current_app, g
# with_appcontext --> see 2*
from flask.cli import with_appcontext

# singleton factory (only one db connection is ever established)
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            # DATABASE = filepath to the sqlite3 file provided in __init__.py in app.config
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells db to return query results in sqlite3.Row format
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(error=None): # pylint: disable=unused-argument
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    # `with...as` is shorthand for try...finally; it closes resources cleanly
    with current_app.open_resource('data/schema.sql') as file:
        db.executescript(file.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo('Initialized the database.')

# see 3*
def init_app(app):
    # tells flask to call close_db() when cleaning up after returning response
    app.teardown_appcontext(close_db)
    # adds command that can be called with `flask` cli commmand in the terminal
    #    - ex: `flask init_db`
    app.cli.add_command(init_db_command)


# 1
# `g` refers to the global application context that stores data
#   - in this case, the database access object is stored within `g`
#
# `current_app` refers to the flask application object
#   - allows you to refer to the flask object without needing to import it

# 2
# `with_appcontext` is to be used with click commands
#   - allows commands to be executed with flask application context (data)

# 3
# `init_app(app)` registers the `close_db` and `init_db_command` functions...
#   with the flask application
