#coding=utf-8
from app import app
import libs.db_queries as db

contentSample = "Agriculture is that which is so universally understood among them that no person, either man or woman, is ignorant of it; they are instructed in it from their childhood, partly by what they learn at school, and partly by practice, they being led out often into the fields about the town, where they not only see others at work but are likewise exercised in it themselves.  Besides agriculture, which is so common to them all, every man has some peculiar trade to which he applies himself; such as the manufacture of wool or flax, masonry, smith’s work, or carpenter’s work; for there is no sort of trade that is in great esteem among them.  Throughout the island they wear the same sort of clothes, without any other distinction except what is necessary to distinguish the two sexes and the married and unmarried.  The fashion never alters, and as it is neither disagreeable nor uneasy, so it is suited to the climate, and calculated both for their summers and winters.  Every family makes their own clothes; but all among them, women as well as men, learn one or other of the trades formerly mentioned.  Women, for the most part, deal in wool and flax, which suit best with their weakness, leaving the ruder trades to the men.  The same trade generally passes down from father to son, inclinations often following descent: but if any man’s genius lies another way he is, by adoption, translated into a family that deals in the trade to which he is inclined; and when that is to be done, care is taken, not only by his father, but by the magistrate, that he may be put to a discreet and good man: and if, after a person has learned one trade, he desires to acquire another, that is also allowed, and is managed in the same manner as the former.  When he has learned both, he follows that which he likes best, unless the public has more occasion for the other."



@app.route('/populate')
def populate():
	db.deleteAll()	
	populate_initially()
	return "Database populated successfully!"


def populate_initially():
	#user
	db.newUser("user1","user1@gmail.com","pass1")
	#categories
	db.newCategory("cat1")
	db.newCategory("cat2")

	#posts
	db.newPost("title1",contentSample,"admin", "cat1")
	db.newPost("title2",contentSample,"admin", "cat1")
	db.newPost("title3",contentSample,"admin", "cat2")
	db.newPost("title4",contentSample,"admin", "cat1")
	db.newPost("title5",contentSample,"admin", "cat1")
	db.newPost("title6",contentSample,"admin", "cat2")
	#tags
	db.newTag("tag1")
	db.newTag("tag2")
	db.newTag("tag3")

	db.addTagToPost(db.getPostByTitle("title1").id,\
		db.getTagByName("tag3").id)
	db.addTagToPost(db.getPostByTitle("title2").id,\
		db.getTagByName("tag3").id)
	db.addTagToPost(db.getPostByTitle("title1").id,\
		db.getTagByName("tag2").id)
	db.addTagToPost(db.getPostByTitle("title2").id,\
		db.getTagByName("tag1").id)
