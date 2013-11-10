from app import db
import app.models
from sqlalchemy import desc, asc

#Search
def search(keywords, nr_posts):
	raw_results = db.engine.execute("SELECT id, ts_rank_cd\
		(to_tsvector('content'),query) AS rank FROM posts,\
		to_tsquery('"+keywords+"') query WHERE to_tsvector(content) @@ query\
		ORDER BY rank DESC LIMIT "+nr_posts+";")
	return raw_results

def getHighlightContent(id_post, keywords):
	content = getPostByID(id_post).content
	return db.engine.execute("SELECT ts_headline('english', '"+content+"',\
	 to_tsquery('"+keywords+"'))");

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

def getPostsOrderedByDate(nr_posts=None):
	all_posts = db.session.query(app.models.Post).\
	order_by(desc(app.models.Post.date)).all()
	if nr_posts != None:
		final_posts = []
		for p in all_posts:
			if nr_posts == 0:
				break
			final_posts.append(p)
			nr_posts=nr_posts-1
		return final_posts
	return all_posts

def getLastPostOrderedByDate():
	return db.session.query(app.models.Post).\
	order_by(asc(app.models.Post.date)).first()

def getAllPosts():
	return db.session.query(app.models.Post).\
	order_by(desc(app.models.Post.date)).all()

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
	posts = []

	tag_id = db.session.query(app.models.Tag.id).\
	filter(app.models.Tag.name == tag_name).first()
	associations = db.session.query(app.models.PostTagsAssociation).\
	filter(app.models.PostTagsAssociation.tag_id == tag_id).all()

	for assoc in associations:
		post = getPostByID(assoc.post_id)
		posts.append(post)

	return posts

def editTag(old_tag_name, new_tag_name):
	tag = db.session.query(app.models.Tag).\
	filter(app.models.Tag.name == old_tag_name).first()
	
	tag.name = new_tag_name
	db.session.commit()

def getAllTags():
	return db.session.query(app.models.Tag).all()

#Categories:
def getCategoryByName(category_name):
	return db.session.query(app.models.Category).\
	filter(app.models.Category.name == category_name).first()

def getCategoryByID(category_id):
	return db.session.query(app.models.Category).\
	filter(app.models.Category.id == category_id).first()

def newCategory(category_name):
	category = app.models.Category(category_name)
	db.session.add(category)
	db.session.commit()

def removeCategory(category_name):
	category = db.session.query(app.models.Category).\
	filter(app.models.Category.name == category_name).first()
	db.session.delete(category)
	db.session.commit()

def editCategory(old_name, new_name):
	category = db.session.query(app.models.Category).\
	filter(app.models.Category.name == old_name).first()
	category.name = new_name
	db.session.commit()

def getAllCategories():
	return db.session.query(app.models.Category).all()

def getPostsByCategory(category):
	
	category = "Quisque"

	cat_id = db.session.query(app.models.Category.id).\
	filter(app.models.Category.name == category).first()	

	print "--------------"
	print category
	print cat_id
	
	posts = db.session.query(app.models.Post).\
	filter(app.models.Post.category == cat_id).all()

	return posts


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