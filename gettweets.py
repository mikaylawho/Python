import http.client
import json


c = http.client.HTTPConnection('api.twitter.com/1.1/search')
c.request('GET', '/search.json?q=mikelhensley')
r = c.getresponse()
data = r.read()
datas = str(data, 'utf-8')
print(datas)
o = json.loads(datas)
#tweets = o['results']

#for tweet in tweets:
 #   print(tweet['text'])


    

