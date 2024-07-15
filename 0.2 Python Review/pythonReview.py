def create_youtube_video(Title, Description):
	new_youtube_video ={
	"Title":Title,
	"Description":Description,
	"Likes":0,
	"Dislikes":0,
	"Comments":{}
	}
	return new_youtube_video

Title = input("The name of the video: ")
Description = input("Enter description: ")


cyv = create_youtube_video(Title, Description)
print (cyv)

def Like(cyv):
	for i in range(495):
		if "Likes" in cyv:
			cyv["Likes"]+=1
	return cyv

new_likes = Like(cyv)

def dislike(cyv):
	if "dislike" in cyv:
		cyv["dislike"]+=1
	return cyv
new_dislike = dislike(cyv)

def add_comment(cyv, username, comment):
	cyv["Comments"][username]=comment
	return cyv 

username= input("Enter your name please: ")
comment= input("Enter a comment please: ")	

new_comments = add_comment(cyv,username, comment)
print(new_comments)












	
	
