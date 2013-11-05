/*Makes RESTful requests to fetch more posts and display them.
*/

function loadMorePosts() {
	$( "div.loadingAnimation" ).append('<img src="/static/imgs/loading.gif" alt="Smiley face" height="80" width="80">');
	setTimeout(function(){
		loadMorePostsDirect();
	}, 1000);
}


function loadMorePostsDirect() {
	var req = $.ajax({
		url: $SCRIPT_ROOT+"_getPosts?callback=?",
		type: "GET",
		cache: false,
		data: { 
			post_id: last_post_id, 
			nr_posts: 2
		},
		dataType: "jsonp"
	}).done(function(data) {
		$( "div.loadingAnimation" ).children().remove();
		if(data.posts == 0){
			$( "a.loadMore" ).replaceWith("Ups, after all there's no more posts to read :D");		
		} else {
			for (var i = 0; i < data.posts.length; i++) {
				var s = data.posts[i].id
				var max_lenght = 150

					//shorten content
					var trimmedString = data.posts[i].content.substring(0,max_lenght)
					trimmedString = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" ")))
					
					//struct to append data
					var structure ='<div class = "shortPost"><a class="title" id = "postLink'+s+'" href =></a><p id = "content'+s+'" ></p><p><a id = "postLink'+s+'" href =>Read post</a></p><div class="postFooter'+s+'">at <strong><span id ="date'+s+'"></span></strong> by <strong><span id = "author'+s+'"></span></strong><br><span id ="tag_label'+s+'"></span><strong><a id = "tagLink'+s+'" href =><span id="tagName'+s+'"><span></a></strong></div></div>'

					$( "div.morePostsStructure" ).append(structure);

					//data append dynamically
					$("a#postLink"+s).attr("href", "/post/"+data.posts[i].id);
					$("a#postLink"+s+".title").append("<h3>"+data.posts[i].title+"</h3>")
					$("p#content"+s).append(trimmedString+" ... ");
					$("span#date"+s).append(data.posts[i].date);
					$("span#author"+s).append(data.posts[i].author);

					//tags
					if(data.posts[i].tags.length>0) {
						$("span#tag_label"+s).append("tags: ");
						for(var t=0; t<data.posts[i].tags.length; t++) {
							$("a#tagLink"+s).append("#"+data.posts[i].tags[t]+"  ");
							$("a#tagLink"+s).attr("href", "/tag/"+data.posts[i].tags[t]);
						}
					}
					last_post_id = (data.posts[i].id)
					if (last_post_id == '{{last_id}}') {
						$("a.loadMore").replaceWith("No more posts to fetch!");
					}
				}
			}
		});
};


function loadCategories() {
	var req = $.ajax({
		url: $SCRIPT_ROOT+"_getAllCategories?callback=?",
		type: "GET",
		cache: false,
		dataType: "jsonp"
	}).done(function(data) {
		for (var i = 0; i < data.categories.length; i++) {
			$("div#categoriesList").append(data.categories[i].name+"<br>");}
		});
}


function loadTags() {
	var req = $.ajax({
		url: $SCRIPT_ROOT+"_getAllTags?callback=?",
		type: "GET",
		cache: false,
		dataType: "jsonp"
	}).done(function(data) {
		for (var i = 0; i < data.tags.length; i++) {
			$("div#tagsList").append(data.tags[i].name+"<br>");}
		});
}



function sleep(milliSeconds){
	var startTime = new Date().getTime();
	while (new Date().getTime() < startTime + milliSeconds);
}
