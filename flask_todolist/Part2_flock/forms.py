from flask.ext.wtf import Form, TextField, PasswordField, BooleanField, validators, Required
from flask.ext.wtf.html5 import IntegerRangeField

class LoginForm(Form):
	email = TextField('email', [validators.Required()])
	password = PasswordField('password', [validators.Required()])
#	number = IntegerRangeField('password')






