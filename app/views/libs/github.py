"""Simple github v3 API  
"""

import urllib2, urllib
import json

base_url = "https://api.github.com/"

def push(user, repo, content):
	#1st: getthe head of the master branch
	#see http://developer.github.com/v3/git/refs/
	response = json.load(urllib2.urlopen\
		(base_url+"repos/"+user+"/"+repo+"/git/refs/heads"))
	sha = response[0]['object']['sha']

	#2nd: get last commit
	#see http://developer.github.com/v3/git/commits/
	response = json.load(urllib2.urlopen\
		(base_url+"repos/"+user+"/"+repo+"/git/commits/"+sha))	
	current_tree_sha = response['tree']['sha']

	#3rd: create tree object (also implicitly creates a blob based on content)
	#see http://developer.github.com/v3/git/trees/
	
	params = urllib.urlencode(\
		{'base_tree': current_tree_sha,\
		'tree': {'path':"test1", 'mode':"100644", 'type':"blob",\
		'sha':current_tree_sha}})


	#return params

	response = urllib2.urlopen\
		(base_url+"repos/"+user+"/"+repo+"/git/trees", params).read()



	return response




#4th: create commit
#see http://developer.github.com/v3/git/commits/

#5th: update branch to the point of the new commit
#see http://developer.github.com/v3/git/refs/

	return "github_push"	