from TwitterAPI import TwitterAPI, constants
import json

# Uses TwitterAPI to generate a twarc by monkeypatching in Twitter's private conversation API.

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

constants.ENDPOINTS.update({'conversation/show/:PARAM': ('GET', 'api')})
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

twid = 828627925578706945

r = api.request('conversation/show/:%d' % twid, {"count":100})

for item in r:
   print(json.dumps(item))
