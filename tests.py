import os
import unittest
import app.views.libs.db_queries as db
from app import app
from app import db as entry_point

class TestSequenceBasic(unittest.TestCase):

	def setUp(self):
		db.newUser("user1","user1@blg.com","pass1")
		db.newCategory("cat1")
		db.newCategory("cat2")
		db.newPost("title1","content1","admin", db.getCategoryByName("cat1").id)
		db.newPost("title2","content2","admin", db.getCategoryByName("cat2").id)
		db.newTag("tag1")
		db.newTag("tag2")

	def tearDown(self):
		db.deleteAll()

	def testAddTagToPost(self):
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag1").id)
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag2").id)
		db.addTagToPost(db.getPostByTitle("title2").id, db.getTagByName("tag1").id)
		tags_p1= db.getTagsByPost(db.getPostByTitle("title1").id)
		tags_p2= db.getTagsByPost(db.getPostByTitle("title2").id)
		#Assertions
		self.assertEqual(tags_p1[0].tag_id, db.getTagByName("tag1").id)
		self.assertEqual(tags_p1[1].tag_id, db.getTagByName("tag2").id)
		self.assertEqual(tags_p2[0].tag_id, db.getTagByName("tag1").id)

	def testRemoveTagFromPost(self):
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag1").id)
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag2").id)
		db.removeTagFromPost(db.getPostByTitle("title1").id, db.getTagByName("tag1").id)
		db.removeTagFromPost(db.getPostByTitle("title1").id, db.getTagByName("tag2").id)
		#Assertion
		self.assertEqual(\
			db.getTagsByPost(db.getPostByTitle("title2").id),[])
		self.assertEqual(\
			db.getTagsByPost(db.getPostByTitle("title1").id),[])

	def testRemovePost(self):
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag1").id)
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag2").id)
		db.removePostWithTitle("title1")
		#Assertion
		self.assertEqual(\
			db.getPostByTitle("title1"),None)

	def testRemoveTag(self):
		db.addTagToPost(db.getPostByTitle("title1").id, db.getTagByName("tag1").id)
		db.addTagToPost(db.getPostByTitle("title2").id, db.getTagByName("tag2").id)
		db.removeTag("tag1")
		#Assertion 
		self.assertEqual(\
			db.getTagByName("tag1"),None)


	def testEditPost(self):
		post_id = db.getPostByTitle("title1").id
		db.editPost(post_id, post_title="new_title", post_author="new_author")
		#Assertions
		self.assertEqual(\
			db.getPostByID(post_id).title, "new_title")
		self.assertEqual(\
			db.getPostByID(post_id).author, "new_author")

	def testEditTag(self):
		db.addTagToPost(db.getPostByTitle("title2").id, db.getTagByName("tag1").id)
		db.editTag("tag1", "new tag1")
		#Assertions
		self.assertEqual(\
			db.getTagByName("new tag1").name, "new tag1")

		tag_id = db.getPostByTitle("title2").tag[0].tag_id
		self.assertEqual(db.getTagByID(tag_id).name, "new tag1")

	def testRemoveCategory(self):
		db.removeCategory("cat1")
		#Assertions
		self.assertEqual(\
			len(db.getAllCategories()), 1)
		self.assertEqual(\
			db.getAllCategories()[0].name, "cat2")
		self.assertEqual(\
			db.getPostByTitle("title1").category, None)

	def testEditCategory(self):
		db.editCategory("cat1", "catn")
		#Assertions
		self.assertEqual(\
			db.getCategoryByName("cat1"), None)
		self.assertEqual(\
			db.getCategoryByName("catn").name, "catn")

class TestSequencePostListing(unittest.TestCase):

	def setUp(self):
		db.newUser("user1","user1@blg.com","pass1")
		db.newCategory("cat1")
		db.newCategory("cat2")
		db.newPost("title1","content1","admin", db.getCategoryByName("cat1").id)
		db.newPost("title2","content2","admin", db.getCategoryByName("cat1").id)
		db.newPost("title3","content3","admin", db.getCategoryByName("cat1").id)
		db.newPost("title4","content4","admin", db.getCategoryByName("cat2").id)
		db.newPost("title5","content5","admin", db.getCategoryByName("cat2").id)
		db.newTag("tag1")
		db.newTag("tag2")

	def tearDown(self):
		db.deleteAll()

	def testListPostsByOrder(self):
		posts = db.getPostsOrderedByDate()
		self.assertEqual(posts[0].title, "title5")
		self.assertEqual(posts[1].title, "title4")
		self.assertEqual(posts[2].title, "title3")



def init_testing_db():
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/tests')
	entry_point.create_all()

if __name__ == "__main__":
	init_testing_db()
	unittest.main()
