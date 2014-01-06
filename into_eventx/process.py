#!/usr/bin/python
import sys
import json
from pprint import pprint
from pymongo import Connection
import datetime
connection = Connection('localhost', 27017)
db = connection.tweventx


# Open a file
fo = open(sys.argv[1], "r")

data = json.load(fo)
#pprint(data)

n=0
for i in data['statuses']:
	n=n+1	

tweets = db.tweets

for j in range(n):
	#print  data['statuses'][j]['text']
	if tweets.find({'text': data['statuses'][j]['text']}).count() == 0:
        	tweets.insert(data['statuses'][j])
res=[]
for j in range(n):
	cursor=tweets.find({'text': data['statuses'][j]['text']})
	for r in cursor:
		if r['text'] not in res:
			res.append(r['text'])

print "Test eventx:: ",db.tweets.count()
for rj in res:
	if rj.find('http') > 1:
		print rj

fo.close()
