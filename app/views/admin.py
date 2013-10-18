from app import app, login_manager
import libs.db_queries as db
from flask import request, render_template, redirect, url_for, flash, jsonify, json, Response
from flask_login import login_user, LoginManager, login_required, logout_user
from app.forms import LoginForm, EditCategoryForm, CategoryForm, TagForm, EditTagForm
from flask_wtf import Form


@app.route("/admin")
@app.route("/admin/")
@login_required
def admin():
	msg = False
	return render_template("admin/adm_index.html", msg=msg)

#Category
@app.route("/admin/add_category", methods=['POST','GET'])
@login_required
def addCategories():
	msg = False
	ok = True
	content = db.getAllCategories()
	if request.method == 'POST':
		form = CategoryForm(request.form)
		msg = "Category added with success!"
		try:
			db.newCategory(form.name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)

	return render_template("admin/category/add_category.html", msg=msg,\
		content=content)


@app.route("/admin/edit_category", methods=['POST','GET'])
@login_required
def editCategories():
	msg = False
	ok = True
	content = db.getAllCategories()

	if request.method == 'POST':
		form = EditCategoryForm(request.form)
		msg = "Category edited with success!"
		try:
			db.editCategory(form.old_name.data, form.new_name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)

	return render_template("admin/category/edit_category.html", msg=msg,\
		content=content)


@app.route("/admin/remove_category", methods=['POST','GET'])
@login_required
def removeCategories():
	msg = False
	ok = True
	content = db.getAllCategories()
	if request.method == 'POST':
		form = CategoryForm(request.form)
		msg = "Category removed with success!"
		try:
			db.removeCategory(form.name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)
	return render_template("admin/category/remove_category.html", msg=msg,\
		content=content)

#Tag
@app.route("/admin/add_tag", methods=['POST','GET'])
@login_required
def addTag():
	msg = False
	ok = True
	content = db.getAllTags()
	if request.method == 'POST':
		form = TagForm(request.form)
		msg = "Tag added with success!"
		try:
			db.newTag(form.name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)

	return render_template("admin/tag/add_tag.html", msg=msg,\
		content=content)

@app.route("/admin/remove_tag", methods=['POST','GET'])
@login_required
def removeTags():
	msg = False
	ok = True
	content = db.getAllTags()
	if request.method == 'POST':
		form = TagForm(request.form)
		msg = "Tag removed with success!"
		try:
			db.removeTag(form.name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)
	return render_template("admin/tag/remove_tag.html", msg=msg,\
		content=content)


@app.route("/admin/edit_tag", methods=['POST','GET'])
@login_required
def editTag():
	msg = False
	ok = True
	content = db.getAllTags()

	if request.method == 'POST':
		form = EditTagForm(request.form)
		msg = "Tag edited with success!"
		try:
			db.editTag(form.old_name.data, form.new_name.data)
		except Exception, e:
			msg = str(e)
			ok = False
		return render_template("admin/adm_index.html", msg=msg, ok=ok)

	return render_template("admin/tag/edit_tag.html", msg=msg,\
		content=content)



#Post
@app.route("/admin/posts")
@login_required
def posts():
	msg = False
	return render_template("admin/adm_posts.html", msg=msg)