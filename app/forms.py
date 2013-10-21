from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from wtforms import Form, TextField, SelectMultipleField, PasswordField,\
IntegerField, DateTimeField, validators
from wtforms.validators import Email, DataRequired, EqualTo, InputRequired

class LoginForm(Form):
	username = TextField('Username',\
	 [Required(message='Username Required')])
	password = PasswordField('Password',\
	 [Required(message='Password Required')])

class CategoryForm(Form):
	name = TextField('Name', [Required(message='Category name Required')])

class EditCategoryForm(Form):
	old_name = TextField('OldName',\
	 [Required(message='Category (old) name Required')])
	new_name = TextField('NewName',\
	 [Required(message='Category (new) name Required')])

class TagForm(Form):
	name = TextField('Name', [Required(message='Tag name Required')])

class EditTagForm(Form):
	old_name = TextField('OldName',\
	 [Required(message='Tag (old) name Required')])
	new_name = TextField('NewName',\
	 [Required(message='Tag (new) name Required')])

class SearchForm(Form):
	query = TextField('Query', [Required(message='Query for search Required')])