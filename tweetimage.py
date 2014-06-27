#!/usr/bin/env python2.7
import tweepy

# This will take an image already saved on the computer.
# It will post it to Twitter
# It will include a status, and a physical location

# Consumer keys and access tokens, used for OAuth
consumer_key        = 'wwwwwwwww'
consumer_secret     = 'xxxxxxxxx'
access_token        = 'yyyyyyyyy'
access_token_secret = 'zzzzzzzzz'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Send the tweet with photo
photo_path = 'example.jpg'
status = 'This is a test' 
api.update_with_media(photo_path, status=status, lat='51.7', long='-1.2')