#coding=utf-8
from app import app
import libs.db_queries as db

content1="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus, nibh at vestibulum rutrum, orci libero elementum ante, id lobortis lacus dolor nec orci. Suspendisse sollicitudin est nunc, quis euismod nibh sagittis vel. Vivamus ultricies sit amet velit in egestas. Cras aliquet metus a mauris sagittis semper. Phasellus ullamcorper tincidunt nibh, at aliquet nunc. In hac habitasse platea dictumst. Integer sit amet sapien ut leo sagittis rutrum in a diam. Curabitur sed nulla augue. Vestibulum a risus sit amet risus lacinia pharetra. Integer sed pretium tortor, vitae rhoncus tortor. Praesent venenatis tortor in justo malesuada pellentesque. Phasellus ornare, tortor vel pretium pulvinar, lectus massa facilisis sapien, vitae blandit massa urna vitae neque. Cras a accumsan nisi. Morbi condimentum, neque sed tincidunt aliquet, tortor nisi sodales sem, et dapibus velit tortor eget nisi. Donec non placerat velit, ac tempor ante. Sed vehicula mattis sapien, vitae lobortis enim cursus id. Duis suscipit est vitae elit molestie, at aliquam ante pulvinar. Phasellus euismod, nunc eget hendrerit porta, nunc massa mattis lectus, sit amet viverra velit ligula sit amet mi. Maecenas ut pharetra magna. Curabitur pulvinar molestie quam sit amet ullamcorper."
title1="In id ornare est"
content2="Sed blandit arcu ut augue sagittis, id fermentum orci placerat. Sed dolor quam, placerat sed tempus commodo, faucibus eget eros. Aliquam vestibulum, erat eu mollis dapibus, leo augue tincidunt eros, non fermentum tortor quam sed turpis. Quisque massa lorem, consectetur et sapien id, auctor mattis urna. Vivamus dignissim magna nunc, a gravida lorem euismod vulputate. Sed in hendrerit ipsum. Vivamus est massa, fringilla a semper sit amet, accumsan at odio. Duis et diam at massa pharetra consequat. Maecenas et venenatis lectus, sit amet tempor tellus. Donec tincidunt sit amet odio sit amet tempus. Nam vulputate, tellus at venenatis eleifend, lorem augue interdum mauris, non bibendum orci felis a nisl."
title2 ="Nulla justo sem"
content3="Aliquam ultrices neque urna. In id ornare est, sit amet fermentum sem. Phasellus venenatis, ante vel luctus porttitor, libero nulla molestie metus, sit amet pretium lorem leo at diam. Nam volutpat tortor eget scelerisque mollis. Pellentesque eget placerat ante. Ut ante augue, ornare et elementum sed, faucibus eget lacus. Duis ac tincidunt lacus. Pellentesque dignissim, augue sit amet elementum porta, diam ipsum lacinia risus, non convallis ante risus in magna. Aenean et rhoncus quam, sit amet egestas nisl. Ut vel volutpat est. Morbi quis est justo."
title3="Pulvinar nulla erat"
content4="Ut nec sodales massa. Nulla nec pharetra ante, at molestie massa. Quisque eu lobortis ipsum, at adipiscing felis. Ut porta ante erat, vitae vehicula erat condimentum id. Donec tempor felis eget elit faucibus, at semper nisl congue. Nunc interdum lorem velit, vel eleifend neque lobortis nec. Curabitur sit amet ullamcorper urna. Aliquam sit amet velit porta erat luctus semper. Vestibulum odio tortor, feugiat non nunc vel, porttitor pellentesque turpis. Praesent ultricies enim in nibh fermentum, non accumsan sem imperdiet. Etiam consequat ligula at magna pulvinar, euismod hendrerit est eleifend. In ipsum quam, tristique eu ultricies ac, accumsan sit amet nibh. Integer laoreet interdum justo quis tempor. Aenean dignissim enim quis mauris tempus, id blandit lectus venenatis. Aenean vitae orci viverra eros blandit dignissim. Phasellus dapibus enim sed interdum ultricies. In vulputate vulputate diam quis tempus. Aenean tristique vulputate felis in cursus. Suspendisse non diam erat. Integer lacinia eget risus non convallis."
title4 ="Quisque eu lobortis ipsum"
content5="Integer aliquam orci a erat bibendum, ut cursus velit posuere. Vivamus sodales est venenatis nunc placerat fermentum. Nullam eget adipiscing nulla, eu volutpat enim. Nulla gravida arcu nec nisi facilisis, id dapibus magna ullamcorper. Donec ac venenatis eros, ut consectetur velit. Cras sit amet mauris quis orci adipiscing viverra. In dignissim adipiscing justo id tempus. Donec dictum massa ut iaculis blandit. Praesent non sem in eros molestie commodo ornare vitae massa. Nunc consectetur placerat nisi ac aliquet. Etiam turpis dui, sodales et lobortis eu, dictum eget mi. Curabitur vel consectetur felis. Maecenas nisl tortor, tempor quis porttitor nec, varius a nulla. Fusce mauris mauris, rutrum vitae fermentum nec, facilisis sit amet velit."
title5="Sit amet fermentum sem"
content6="Nulla justo sem, adipiscing nec ipsum ac, imperdiet dignissim nisl. Maecenas vitae diam dignissim, lobortis sapien sit amet, vulputate sem. Nulla luctus, diam in condimentum malesuada, leo mauris vestibulum mi, id consectetur neque risus eu nisi. Nulla in gravida nunc. Fusce ullamcorper sapien enim, vitae varius velit mollis ac. In sed aliquam magna, et eleifend velit. Donec mattis malesuada interdum. Nunc ornare fermentum arcu, in placerat sapien aliquet sed. Sed quis semper quam. Fusce ut est vel arcu iaculis gravida vel at erat. Aenean eu elit lacus. Vivamus sed consequat sapien. Morbi ut eros dictum, fringilla enim a, condimentum ante. Proin lobortis nibh non mi facilisis vehicula. Aenean ornare in purus ac tincidunt." 
title6="Id fermentum orci placerat"
content7="Phasellus pulvinar nulla erat, in sodales nibh luctus sit amet. Quisque pharetra urna et nisl dignissim, quis tempus nulla condimentum. Nunc felis sem, fringilla id commodo vel, posuere et dolor. Vivamus quis vehicula arcu. Aenean congue sapien quis ipsum fermentum fringilla. Donec aliquet purus metus, et lobortis ante varius nec. Sed fringilla libero ut volutpat rutrum. Sed tincidunt adipiscing elit vitae convallis. Nulla a neque sodales, venenatis ante sit amet, ornare dui. Aenean varius porta pharetra. Duis faucibus tellus a vulputate interdum."
title7 ="Imperdiet dignissim nisl"

tag1="Dignissim"
tag2="Sodales"
tag3="Posuere"
tag4="Aliquam"

cat1="Quisque"
cat2="Pulvinar"
cat3="Bibendum"

@app.route('/populate')
def populate():
	db.deleteAll()	
	populate_initially()
	return "Database populated successfully!"

def populate_initially():
	#user
	db.newUser("admin","admin@gmail.com","pass")
	#categories
	db.newCategory(cat1)
	db.newCategory(cat2)
	db.newCategory(cat3)

	#posts
	db.newPost(title1,content1,"admin", db.getCategoryByName(cat1).id)
	db.newPost(title2,content2,"admin", db.getCategoryByName(cat1).id)
	db.newPost(title3,content3,"admin", db.getCategoryByName(cat1).id)
	db.newPost(title4,content4,"admin", db.getCategoryByName(cat2).id)
	db.newPost(title5,content5,"admin", db.getCategoryByName(cat3).id)
	db.newPost(title6,content6,"admin", db.getCategoryByName(cat3).id)
	db.newPost(title7,content7,"admin", db.getCategoryByName(cat2).id)

	#tags
	db.newTag(tag1)
	db.newTag(tag2)
	db.newTag(tag3)
	db.newTag(tag4)

	db.addTagToPost(db.getPostByTitle(title1).id,\
		db.getTagByName(tag3).id)
	db.addTagToPost(db.getPostByTitle(title2).id,\
		db.getTagByName(tag3).id)
	db.addTagToPost(db.getPostByTitle(title1).id,\
		db.getTagByName(tag2).id)
	db.addTagToPost(db.getPostByTitle(title2).id,\
		db.getTagByName(tag1).id)
	db.addTagToPost(db.getPostByTitle(title3).id,\
		db.getTagByName(tag3).id)
	db.addTagToPost(db.getPostByTitle(title4).id,\
		db.getTagByName(tag4).id)
	db.addTagToPost(db.getPostByTitle(title4).id,\
		db.getTagByName(tag1).id)
	db.addTagToPost(db.getPostByTitle(title6).id,\
		db.getTagByName(tag1).id)
	db.addTagToPost(db.getPostByTitle(title6).id,\
		db.getTagByName(tag3).id)
	db.addTagToPost(db.getPostByTitle(title6).id,\
		db.getTagByName(tag2).id)
	db.addTagToPost(db.getPostByTitle(title7).id,\
		db.getTagByName(tag3).id)
	db.addTagToPost(db.getPostByTitle(title7).id,\
		db.getTagByName(tag2).id)
