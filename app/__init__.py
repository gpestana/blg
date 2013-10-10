import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#database
#Heroku
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/test')
#Locally
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ[local]


db = SQLAlchemy(app)

from views import general