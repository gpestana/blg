import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/test')
db = SQLAlchemy(app)

#Locally DB:
#dropdb -U <user> <namedb>
#createdb -U <user> <namedb> 

from app import models
from views import general