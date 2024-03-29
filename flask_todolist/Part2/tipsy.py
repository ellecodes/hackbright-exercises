"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, redirect, request
import model
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    form = LoginForm()
    return render_template("index.html", user_name="chriszf", form = form)

@app.route("/join")
def create_user():
    form = LoginForm()
    return render_template("join.html", user_name="chriszf", form = form)

# @app.route("/join")
# def create_user():
#     # new_user = model.session.add(model.User)
#     c = model.session.add(model.User(age=72, zipcode="95112"))
#     model.session.commit()

@app.route("/save_task", methods=["POST"])
def save_task():
    db = model.connect_db()
    title = request.form['title']
    model.new_task(db, title)
    return redirect("/tasks")

@app.route("/tasks")
def list_tasks():
    db = model.connect_db()
    tasks_from_db = model.get_tasks(db, None)
    return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
    db = model.connect_db()
    task_from_db = model.get_task(db, id)
    return render_template("view_task.html", task=task_from_db)

@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
    db = model.connect_db()
    model.complete_task(db, id)
    return redirect("/tasks")

if __name__ == "__main__":
    app.run(debug=True)