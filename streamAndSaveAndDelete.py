import sys
import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key        = 'aaaaaaaaaaa'
consumer_secret     = 'bbbbbbbbbbb'
access_token        = 'ccccccccccc'
access_token_secret = 'ddddddddddd'

# Set up the authorisation to use the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)

# Handle the output generated from the stream
class listener(StreamListener):

    def on_data(self, data):
        # Raw output to screen.
        print data

        # Convert the message to JSON
        json_data = json.loads(data)
        
        if 'id_str' not in json_data:
            # If this isn't a status, do nothing.
            print "no ID"
        else :
            print json_data['id_str']
            # Write a file "123456789.json" containing the Tweet and all the metadata
            text_file = open(json_data['id_str'] + ".json", "w")
            text_file.write(data)
            text_file.close()
        
        if 'delete' in data:
            # Deleted Tweets look like this
            #{"delete":{"status":{"id":123456789,"user_id":99999999,"id_str":"123456789",
            print "DELETED!"
            # Write a file "123456789-DELETED.json" containing the metadata. Do NOT delete the original Tweet
            text_file = open(json_data['delete']['status']['id_str'] + "-DELETED.json", "w")
            text_file.write(data)
            text_file.close()

        return True

    def on_error(self, status):
        print status

#   Start consuming from the stream.  This will get all the Tweets & Deletions from the users the user is following.
twitterStream = Stream(auth, listener()) 
twitterStream.userstream("with=following")