import datetime
from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean


class User(db.Model):
	__tablename__ = "users"
	id = Column(Integer, primary_key = True)
	username = Column(String(80), nullable = False)
	email = Column(String(80))
	password = Column(String(30), nullable = False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return 'User: %r' % self.username

   	#Flask-Login
   	def is_active(self):
   		return self
   	def get_id(self):
   		return self.id
   	def is_authenticated(self):
   		return True
   	def is_anonymous(self):
   		return False



class Post(db.Model):
	__tablename__ = "posts"
	id = Column(Integer, primary_key = True)
	title = Column(String(80), nullable = False)
	date = Column(DateTime, nullable = False)
	content = Column(String, nullable = False)
	author = Column(String, nullable = False)

	category = Column(Integer, ForeignKey('categories.id'), nullable = True)
	tag = relationship("PostTagsAssociation", backref="tags", cascade='all')

	def __init__(self, title, content, author, category_id):
		self.title = title
		self.content = content
		self.author = author
		self.date = datetime.datetime.now()
		#self.date = datetime.datetime.now().strftime('%d %b %Y, %H %M')
		self.category = category_id

	def __repr__(self):
		return 'Post '+str(self.id)
	
	@property
	def serialize(self):
		return {
		   'id': self.id,
           'title': self.title,
           'content': self.content,
           'date': self.date,
           'category': self.category,
           'author': self.author
       }




class Tag(db.Model):
	__tablename__ = "tags"
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)

	def __init__(self, tag_name):
		self.name = tag_name
	def __repr__(self):
		return 'Tag Name: %r' % self.name




class Category(db.Model):
	__tablename__ = "categories"
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable=False)
	post = relationship("Post")

	def __init__(self, category_name):
		self.name = category_name
	def __repr__(self):
		return 'Category: %r' % self.name




class PostTagsAssociation(db.Model):
	__tablename__ = "posts_tags_association"
	post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key = True)
	tag_id = Column(Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key = True)
	
	tag = relationship("Tag", backref="tags")

	def __init__(self):
		pass
	def __repr__(self):
		return 'Associaltion Post+Tag: ' +str(self.post_id)+", "+str(self.tag_id)