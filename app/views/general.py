from app import app, login_manager
import libs.db_queries as db
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, LoginManager, login_required, logout_user
from app.forms import LoginForm
from flask_wtf import Form

"""LoginManager
"""
@login_manager.user_loader
def load_user(id):
	return db.getUserByID(id)

@app.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm(request.form)
	user = db.getUserByUsername(form.username.data)

	if user == None:
		flash("User does not exist.")
		return redirect(url_for('index'))

	elif form.password.data != user.password:  
		flash("Wrong password.")
		return redirect(url_for('index'))

	flash("Logged IN successfully.")
	login_user(user)
	return redirect(url_for('index'))

@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash("Logged OUT successfully.")
	return redirect(url_for('index'))	

@login_manager.unauthorized_handler
def unauthorized():
    flash("Sorry, you have to be logged in to access the page requested.")
    return redirect(url_for('index'))

"""Other Views
"""

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/test')
def test():
	return render_template("test.html")

@app.route('/blog')
def blog():
	return render_template("blog.html")