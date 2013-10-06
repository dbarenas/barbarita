from pymongo import Connection
import datetime
import json
from StringIO import StringIO
import codecs
import re
import sys 

connection = Connection('localhost', 27017)

db = connection.twemotion
tof= db.tweets
tw = tof.count()
emo= sys.argv[1]

for i in  tof.find({"text": re.compile(emo)},{"text"}):
	print i["text"].encode('UTF-8')


print "*"*80
print "emotion:  ",tw
print "*"*80
