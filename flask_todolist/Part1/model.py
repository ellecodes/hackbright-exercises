"""
model.py
"""

import sqlite3

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

	return None

# new_task(db, title, user_id) -- Created a new task, returns the id of the newly created row. Make sure to populate the created_at field.
def new_task(db, title, user_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (NULL, ?, DATETIME('now'), NULL, ?)"""
	result = c.execute(query, (title, user_id))
	if result:
		db.commit()
		return result.lastrowid


# get_user(db, user_id) -- Fetch a user's record based on his id. Return the user as a dictionary, like our authenticate method.
def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT * from Users WHERE id=?"""
	c.execute(query, (id))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None


# complete_task(db, task_id) -- Marks a task as being complete, setting the completed_at field.
def complete_task(db, task_id):
	c = db.cursor()
	query = """UPDATE Tasks SET completed_at=DATETIME('now') WHERE id=?"""
	result = c.execute(query, (task_id))
	if result:
		db.commit()
		return result.lastrowid
	else:
		return None

# get_tasks(db, user_id) -- Gets all the tasks for the given user id. Returns all the tasks in the system if no user_id is given. Returns them as a list of dictionaries.
def get_tasks(db, user_id):
	c = db.cursor()
	if user_id:
		query = """SELECT * from Tasks WHERE user_id=?"""
		c.execute(query, (user_id))
	else:
		query = """SELECT * from Tasks"""
		c.execute(query)
	tasks = []
	rows = c.fetchall()
	for row in rows:
		task = dict(zip(["id", "title", "created_at", "completed_at", "user_id"], row))
		tasks.append(task)

	return tasks

    
# get_task(db, task_id) -- Get a single task, given its id. Return the task as a dictionary as above in the authenticate method.
def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * from Tasks WHERE task_id=?"""
	c.execute(query, (task_id))
	result = c.fetchone()
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))

	return None








