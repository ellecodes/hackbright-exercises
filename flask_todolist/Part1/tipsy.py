"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect
import model

# initialize our program to be a Flask application. Notice "Flask" is a class, so this app is an instantiation of the Flask class. The first parameter passed to the initializer is the name of the module (file) that we're doing this from. 
app = Flask(__name__)

# The server, once started, listens for requests from web browsers. When a request comes in, Flask looks at the url asked for by the browser. It then matches the url with any number of 'routes' registered in the application
@app.route("/")
def index():
    return render_template("index.html", user_name="Elle")

# Chew on this view for a moment. When a user accesses the "/tasks" url, it:
# 1. Connects to the database
# 2. Gets a list of all the tasks
# 3. Sends that list to the list_tasks template as a parameter named 'tasks'
@app.route("/tasks")
def list_tasks():
    db = model.connect_db()
    tasks_from_db = model.get_tasks(db, None)
    return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/new_task")
def new_tasks():
    return render_template("new_task.html")

@app.route("/save_task", methods=["POST"]) 
def save_task():
    task_title = request.form['task_title']
    db = model.connect_db()
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(db, task_title, 1)
    return redirect("/tasks")

# These lines start our application server/web server/flask application when we run our program from the command line.
if __name__ == "__main__":
    app.run(debug=True)