from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
	# return "Hello world!"
	user_list = model.session.query(model.User).limit(10).all()
	return render_template("user_list.html", users=user_list)

# @app.route("/")
# def create_user():
# 	# new_user = model.session.add(model.User)
# 	c = model.session.add(model.User(age=72, zipcode="95112"))
# 	model.session.commit()


if __name__ == "__main__":
	app.run(debug = True)
