#!/usr/bin/env python
import tweepy

# Generate all the OAuth tokens you will ever need :-)
# Using your API keys from https://apps.twitter.com
# This will generate a URL
# Click on the URL and sign in
# You'll be presented with a PIN
# Type the number into the terminal
# Your OAuth keys will magically appear

API_KEY    = 'zzzzzzzzzzzzzzzzz'
API_SECRET = 'xxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_TOKEN = '%s'" % auth.access_token
print "ACCESS_TOKEN_SECRET = '%s'" % aauth.access_token_secret
