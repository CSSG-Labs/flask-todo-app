# A data access object (DAO) is a pattern that...
# provides an abstract interface to some type of database
#  - this class will deal with all the database logic for Todo CRUD operations

class TodoDAO:
    '''Handles DB operations for Todo Table'''
    def __init__(self, db):
        self.db = db

    def getAll(self):
        todos = self.db.execute('SELECT * FROM todo').fetchall()

        return todos

    def getOne(self, todo_id):
        todo = self.db.execute('SELECT * FROM todo WHERE todo_id = ?', (todo_id,)).fetchone()

        return todo

    def addOne(self, desc):
        self.db.execute('INSERT INTO todo (desc) VALUES (?)', (desc,))
        self.db.commit()

    def editOne(self, todo_id, desc):
        self.db.execute('UPDATE todo SET desc=? WHERE todo_id=?', (desc, todo_id,))
        self.db.commit()

    def deleteOne(self, todo_id):
        self.db.execute('DELETE FROM todo WHERE todo_id=?', (todo_id, ))
        self.db.commit()

    def deleteAll(self):
        self.db.execute('DELETE FROM todo')
        self.db.commit()
