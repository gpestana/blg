from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from wtforms import Form, TextField, SelectMultipleField, PasswordField, IntegerField, DateTimeField, validators
from wtforms.validators import Email, DataRequired, EqualTo, InputRequired

class LoginForm(Form):
	username = TextField('Username', [Required(message='Username Required')])
	password = PasswordField('Password', [Required(message='Password Required')])
