import urllib
import json
import base64
import sys



#	The website's URL
site = "https://twitter.com/edent"



#	The Google API.  Remove "&strategy=mobile" for a desktop screenshot
api = "https://www.googleapis.com/pagespeedonline/v1/runPagespeed?screenshot=true&url=" + urllib.parse.quote(site)


#	Get the results from Google
try:
    site_data = json.load(urllib.request.urlopen(api))
except urllib.error.URLError:
    print("Unable to retreive data")
    sys.exit()


try:
    screenshot_encoded =  site_data['screenshot']['data']
except ValueError:
    print("Invalid JSON encountered.")
    sys.exit()

#	Google has a weird way of encoding the Base64 data
screenshot_encoded = screenshot_encoded.replace("_", "/")
screenshot_encoded = screenshot_encoded.replace("-", "+")

#	Decode the Base64 data
screenshot_decoded = base64.b64decode(screenshot_encoded)


#	Save the file
with open('screenshot.jpg', 'wb+') as file_:
    file_.write(screenshot_decoded, )

