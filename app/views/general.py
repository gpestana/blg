#coding=utf-8
from app import app, login_manager
import libs.db_queries as db
from flask import request, render_template, redirect, url_for, flash, jsonify, json, Response
from flask_login import login_user, LoginManager, login_required, logout_user
from app.forms import LoginForm
from flask_wtf import Form

from functools import wraps

"""LoginManager
"""
@login_manager.user_loader
def load_user(id):
	return db.getUserByID(id)

@app.route("/login", methods=["POST", "GET"])
def login():

	if request.method == "POST":
		form = LoginForm(request.form)
		user = db.getUserByUsername(form.username.data)
		ok = False
		if user == None:
			msg = "User does not exist."
			return render_template("admin/adm_login.html", msg = msg,\
				ok = ok)

		elif form.password.data != user.password:  
			msg = "User and password do not match."
			return render_template("admin/adm_login.html", msg = msg,\
				ok = ok)

		login_user(user)
		msg = "User logged in successfully!"
		return render_template("admin/adm_index.html", msg = msg,\
			ok = True)
	else:
		return render_template("admin/adm_login.html", msg = False)


@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))	

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("admin/adm_login.html",\
     msg ="Sorry, you have to be logged in to access the requested page.", ok=False)

'''Main page view
'''

@app.route('/')
def index():
	return render_template("index.html")


'''Blog Engine
'''

@app.route('/blog/', methods=['POST','GET'])
@app.route('/blog/<int:nr_posts>')
def blog(nr_posts=None):
	
	if request.method == 'POST':
		return "POST"
		
	if nr_posts == None:
		nr_posts = 3
	
	last_id = db.getLastPostOrderedByDate().id

	posts = db.getPostsOrderedByDate(nr_posts) 
	return render_template("blog.html", posts = posts,\
	 nr_posts = int(float(nr_posts)), last_id = last_id)

@app.route('/tag/<tag>')
def listTag(tag):
	posts = db.getPostsByTag(tag)
	return render_template("tag_list.html", posts = posts, tag = tag)

@app.route('/post/<post_id>')
def singlePost(post_id):
	nr_posts = 1
	posts = []
	posts.append(db.getPostByID(post_id)) 
	return render_template("blog.html", posts = posts, nr_posts = nr_posts,\
	 singlePost = True)

#RESTfull side

def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function


def getPostsAfterPost(post_id, nr_posts):
	'''Get <nr_posts> posts from ordered by date list os posts after
	   the post <post_id> had occured
	   >> Used for dynamic jQuery loading 
	'''
	all_posts = db.getPostsOrderedByDate()
	new_array = []
	after = False
	for p in all_posts:
		if after == True:
			if nr_posts == 0:
				break
			new_array.append(p)
			nr_posts = nr_posts-1
		if p.id == post_id:
			after = True 
	return new_array


@app.route('/_getPosts')
@jsonp
def restGetPosts():
	post_id = request.args.get('post_id', 9, type=int)
	nr_posts = request.args.get('nr_posts', 3, type=int)

	posts = [i.serialize for i in getPostsAfterPost(post_id,nr_posts)]
	#Posts o 
	for post in posts:
		t_list = []
		tags = db.getTagsByPost(post['id'])
		for tag in tags: 
			t_list.append(tag.tag.name)
		post['tags'] = t_list

	return jsonify(posts=posts)	



##Small tests
@app.route('/test')
def test():
	return str(db.getLastPostOrderedByDate())