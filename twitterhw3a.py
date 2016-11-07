# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

# Unique code from Twitter
access_token = "16803203-FgMMK3RGdTjwneE2L7n1V64wSvzHOuCkvHI0YhWn8"
access_token_secret = "aUJzuuYtfGRx9uZZTQr95b7FR9DEdjFZyAZyRkHX9yVBd"
consumer_key = "2ovZ0iyuKvAYTnwRUbdq3Swqn"
consumer_secret = "w7BjX5omv5T2rvU8CRTIYCXkvis41DbujrwWRcJ6Lzxa5TkDHt"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

api.update_with_media("quick.jpg","pls ignore this is for class #UMSI-206 #Proj3")

