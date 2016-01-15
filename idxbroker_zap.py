import httplib
import urlparse
import json

#set endpoint and add your API key
url = "https://api.idxbroker.com/leads/lead?interval=.25&dateType=subscribeDate"
headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":"YourAPIKeyHere","outputtype":"json"}
domain = urlparse.urlparse(url).netloc
connection = httplib.HTTPSConnection(domain)
connection.request("GET", url, headers=headers)
response = connection.getresponse()
data = response.read()
data = json.loads(data)
output = data
