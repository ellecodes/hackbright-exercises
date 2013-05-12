"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, redirect, request, session, g
import os
import model
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    form = LoginForm()
    return render_template("index_login.html", user_name="chriszf", form = form)

@app.route("/join-create")
def join_create_user():
    form = LoginForm()
    return render_template("user_join_create.html", user_name="chriszf", form = form)

@app.route("/company-search")
def search_company():
    form = LoginForm()
    return render_template("company_search.html", user_name="chriszf", form = form)

@app.route("/company-add")
def add_company():
    form = LoginForm()
    return render_template("company_add.html", user_name="chriszf", form = form)

@app.route("/company-rate")
def rate_company():
    form = LoginForm()
    return render_template("company_rate.html", user_name="chriszf", form = form)

@app.route("/home")
def home_user():
    form = LoginForm()
    return render_template("user_home.html", user_name="chriszf", form = form)



# @app.route("/join")
# def create_user():
#     # new_user = model.session.add(model.User)
#     c = model.session.add(model.User(age=72, zipcode="95112"))
#     model.session.commit()


@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    user_id = model.authenticate(g.db, email, password)
    session['user_id'] = user_id

@app.before_request
def set_up_db():
    g.db = model.connect_db()

@app.teardown_request
def disconnect_db(e):
    g.db.close()

@app.route("/save_task", methods=["POST"])
def save_task():
    title = request.form['title']
    model.new_task(g.db, title)
    return redirect("/tasks")

@app.route("/tasks")
def list_tasks():
    user_id = session.get("user_id", None)
    tasks_from_db = model.get_tasks(g.db, user_id)
    return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
    task_from_db = model.get_task(g.db, id)
    return render_template("view_task.html", task=task_from_db)

@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
    model.complete_task(g.db, id)
    return redirect("/tasks")

if __name__ == "__main__":
    app.run(debug=True)