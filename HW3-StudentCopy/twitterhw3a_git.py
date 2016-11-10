# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
# https://pypi.python.org/pypi/TwitterAPI/2.1.9
from TwitterAPI import TwitterAPI

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
#opens the file of my picture and sets data equal to that picture. Then it makes a request to the api and 
#updates my twitter with the picture and the hashtags
file = open('media/me.png', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'#UMSI_206 #Proj3'}, {'media[]':data})
#print(r.status_code)
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")