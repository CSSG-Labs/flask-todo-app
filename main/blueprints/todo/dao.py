# A data access object (DAO) is a pattern that...
# provides an abstract interface to some type of database
#  - this class will deal with all the database logic for Todo CRUD operations

class TodoDAO:
    '''Handles DB operations for Todo Table'''
    def __init__(self, db):
        self.db = db

    def getAll(self):
        todos = self.db.execute('SELECT * FROM todo').fetchAll()
        return todos

    def getOne(self, todo_id):
        todo = self.db.execute('SELECT * FROM todo WHERE todo_id = ?', (todo_id,)).fetchone()
        return todo
