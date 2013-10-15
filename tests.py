import os
import unittest
import app.views.libs.db_queries as db
from app import app
from app import db as entry_point

class TestSequencePostsTags(unittest.TestCase):

	def setUp(self):
		db.newUser("user1","user1@blg.com","pass1")
		db.newCategory("cat1")
		db.newCategory("cat2")
		db.newPost("title1","content1","admin", "cat1")
		db.newPost("title2","content2","admin", "cat2")
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
	


def init_testing_db():
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/tests')
	entry_point.create_all()

if __name__ == "__main__":
	init_testing_db()
	unittest.main()
