from app import app
import libs.db_queries as db



@app.route('/populate')
def populate():
	db.deleteAll()	
	populate_initially()

	#-todo- Not working
	#db.editTag("tag3","t")


	return "Database populated successfully!"


def populate_initially():
	#user
	db.newUser("user1","user1@gmail.com","pass1")
	#posts
	db.newPost("title1","content1","admin")
	db.newPost("title2","content2","admin")
	db.newPost("title3","content3","admin")
	#tags
	db.newTag("tag1")
	db.newTag("tag2")
	db.newTag("tag3")

	db.addTagToPost(db.getPostByTitle("title1").id,"tag3")
	db.addTagToPost(db.getPostByTitle("title1").id,"tag2")
	db.addTagToPost(db.getPostByTitle("title2").id,"tag1")
