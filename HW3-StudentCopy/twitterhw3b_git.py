# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

# finds the tweets that contain the term that we want to search for
public_tweets = api.search('science')
#initializes the polarity, subjectivity, and count to 0 
total_polarity = 0
total_subjectivity = 0 
count = 0
#iterates throught the tweets that the search found and prints the tweet
# then it analyzes the sentiment from the tweet and pulls out the polarity and subjectivity score and
# adds it to their respective total. Finally, the count is also incremented at 1
for tweet in public_tweets:
	print(tweet.text)
	print("")
	analysis = TextBlob(tweet.text)
	total_polarity += analysis.sentiment[0]
	total_subjectivity += analysis.sentiment[1]
	count += 1
# finds the average polarity and subjectivity by dividing their totals by the number of tweets (count)
average_polarity = total_polarity / count
average_subjectivity = total_subjectivity / count 
print("")
print("Average subjectivity is %s" % str(average_subjectivity))
print("Average polarity is %s" % str(average_polarity))