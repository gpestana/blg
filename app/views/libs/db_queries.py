from app import db
import app.models

#Users
def newUser(username, email, password):
	user = app.models.User(username, email, password)
	db.session.add(user)
	db.session.commit()

def getUserByID(id):
	return db.session.query(app.models.User).\
	filter(app.models.User.id == id).first()

def getUserByUsername(username):
	return db.session.query(app.models.User).\
	filter(app.models.User.username == username).first()

#Posts
def newPost(title, content, author, category):
	new_post = app.models.Post(title, content, author, category)
	db.session.add(new_post)
	db.session.commit()

def getPostByID(post_id):
	return db.session.query(app.models.Post).\
	filter(app.models.Post.id == post_id).first()

def getPostByTitle(post_title):
	return db.session.query(app.models.Post).\
	filter(app.models.Post.title == post_title).first()

def removePostWithTitle(post_title):
	post = db.session.query(app.models.Post).\
	filter(app.models.Post.title == post_title).first()
	db.session.delete(post)
	db.session.commit()

def editPost(post_id, post_title = None, post_content = None,\
	post_author = None, post_date = None):
	post = getPostByID(post_id)

	if post_title != None:
		post.title = post_title
	if post_content != None:
		post.post = post_content
	if post_author != None:
		post.author = post_author
	if post_date != None:
		post.date = post_date

	db.session.commit()


#Tags
def newTag(tag_name):
	new_tag = app.models.Tag(tag_name)
	db.session.add(new_tag)
	db.session.commit()

def getTagByID(tag_id):
	return db.session.query(app.models.Tag).\
	filter(app.models.Tag.id == tag_id).first()

def getTagByName(tag_name):
	return db.session.query(app.models.Tag).\
	filter(app.models.Tag.name == tag_name).first()

#-todo-WORKING BUT NOT IN AUTOMATED WAY!
def removeTag(tag_name):
	tag = db.session.query(app.models.Tag).\
	filter(app.models.Tag.name == tag_name).first()
	#Automated way to do it ?
	associations_posts_tag = db.session.query(app.models.PostTagsAssociation).\
	filter(app.models.PostTagsAssociation.tag_id==tag.id).all()
	for ass in associations_posts_tag:
		removeTagFromPost(ass.post_id,ass.tag_id)

	db.session.delete(tag)
	db.session.commit()

def getPostsByTag(tag_name):
	return db.session.query(app.models.PostTagsAssociation).\
	filter(app.models.PostTagsAssociation.tag_name == tag_name).all()

def editTag(old_tag_name, new_tag_name):
	tag = db.session.query(app.models.Tag).\
	filter(app.models.Tag.name == old_tag_name).first()
	
	tag.name = new_tag_name
	db.session.commit()

#Categories:
def newCategory(category_name):
	category = app.models.Category(category_name)
	db.session.add(category)
	db.session.commit()


#Posts&Tags
def addTagToPost(post_id, tag_id):
	post = getPostByID(post_id)
	tag = getTagByID(tag_id)
	association = app.models.PostTagsAssociation()
	association.tag_id = tag_id
	association.post_id = post_id

	post.tag.append(association)

	db.session.commit()

def removeTagFromPost(post_id, tag_id):
	association = db.session.query(app.models.PostTagsAssociation).\
	filter(app.models.PostTagsAssociation.post_id == post_id).\
	filter(app.models.PostTagsAssociation.tag_id == tag_id).first()
	db.session.delete(association)
	db.session.commit()

def getTagsByPost(post_id):
	return db.session.query(app.models.PostTagsAssociation).\
	filter(app.models.PostTagsAssociation.post_id == post_id).all()

def deleteAll():
	app.models.User.query.delete()
	db.session.commit()
	app.models.PostTagsAssociation.query.delete()
	db.session.commit()
	app.models.Post.query.delete()
	db.session.commit()
	app.models.Tag.query.delete()
	db.session.commit()
	app.models.Category.query.delete()
	db.session.commit()