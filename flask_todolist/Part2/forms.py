from flask.ext.wtf import Form, TextField, BooleanField, Required

class LoginForm(Form):
	email = TextField('email')
	password = TextField('password')


