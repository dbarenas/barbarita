#!/usr/bin/python
import sys
import json
from pprint import pprint
from pymongo import Connection
import datetime
connection = Connection('localhost', 27017)
db = connection.twfrs1


# Open a file
fo = open(sys.argv[1], "r")

data = json.load(fo)
#pprint(data)

n=0
for i in data['statuses']:
	n=n+1	

tweets = db.tweets
for j in range(n):
	if tweets.find({'text': data['statuses'][j]['text']}).count() == 0:
        	print tweets.insert(data['statuses'][j])

print db.tweets.count()
fo.close()
