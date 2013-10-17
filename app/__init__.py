import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from jinja2 import Environment 

app = Flask(__name__)

#Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'secret_key'


#SQLAlchemy+db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",\
	"postgresql+psycopg2://user:pass@localhost/test")
db = SQLAlchemy(app)

#Models+Views
from app import models
from views import general
from views import populate