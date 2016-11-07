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
access_token = "16803203-FgMMK3RGdTjwneE2L7n1V64wSvzHOuCkvHI0YhWn8"
access_token_secret = "aUJzuuYtfGRx9uZZTQr95b7FR9DEdjFZyAZyRkHX9yVBd"
consumer_key = "2ovZ0iyuKvAYTnwRUbdq3Swqn"
consumer_secret = "w7BjX5omv5T2rvU8CRTIYCXkvis41DbujrwWRcJ6Lzxa5TkDHt"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('"Kanye West"')

counter = 0
polarity = 0
subjectivity = 0
for tweet in public_tweets:
	
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	counter += 1
	polarity += analysis.sentiment.polarity
	subjectivity += analysis.sentiment.subjectivity
try:

	print("Average subjectivity is: " , subjectivity/counter)
	print("Average polarity is: " , polarity/counter)

except:
	print("No tweets to show :(")
