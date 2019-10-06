#!/usr/bin/env python3
import tweepy
import sys

# Generate all the OAuth tokens you will ever need :-)
# Using your API keys from https://developer.twitter.com/en/apps
# This will generate a URL
# Click on the URL and sign in
# You'll be presented with a PIN
# Type the number into the terminal
# Your OAuth keys will magically appear

CONSUMER_KEY    = ""
CONSUMER_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True

try:
	auth_url = auth.get_authorization_url()
except tweepy.TweepError:
	print('Error! Failed to get request token.')
	sys.exit()

print("Log in to this authorisation URI: " + auth_url + "\nThen return here.")
verifier = input("Enter your PIN: ").strip()
auth.get_access_token(verifier)
print("CONSUMER_KEY        = '%s'" % CONSUMER_KEY)
print("CONSUMER_SECRET     = '%s'" % CONSUMER_SECRET)
print("ACCESS_TOKEN        = '%s'" % auth.access_token)
print("ACCESS_TOKEN_SECRET = '%s'" % auth.access_token_secret)
