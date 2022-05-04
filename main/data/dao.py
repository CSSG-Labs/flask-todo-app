# SQLite connection

import sqlite3

# current_app & g --> see 1*
from flask import current_app, g

# singleton factory (only one db connection is ever established)
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            # DATABASE = filepath to the sqlite3 file provided in __init__.py in app.config
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells DAO to return query results in sqlite3.Row format...
        #    which allows access to columns by name
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(error=None): # pylint: disable=unused-argument
    db = g.pop('db', None)

    if db is not None:
        db.close()

# 1
# `g` refers to the global application context that stores data
#   - in this case, the database access object is stored within `g`
#
# `current_app` refers to the flask application object
#   - allows you to refer to the flask object without needing to import it
