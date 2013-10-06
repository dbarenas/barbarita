from pymongo import Connection
import datetime
import json
from StringIO import StringIO
import codecs
import re
import sys 
from bson import BSON
from bson import json_util

connection = Connection('localhost', 27017)
#[u'twfrs1', u'twfilter', u'twopinion', u'twemotion', u'twemotiontwo', u'twemotion2']
db = connection.twfrs1
tof= db.tweets
print tof.count(),"::twfrs1"

db = connection.twfilter
tof= db.tweets
print tof.count(),"::twfilter"

db = connection.twopinion
tof= db.tweets
print tof.count(),"::twopinion"

db = connection.twemotion
tof= db.tweets
print tof.count(),"::twemotion"

db = connection.twemotiontwo
tof= db.tweets
print tof.count(),"::twemotiontwo"

db = connection.twemotion2
tof= db.tweets
print tof.count(),"::twemotion2"

'''
emo= sys.argv[1]
for i in  tof.find({"text": re.compile(emo)},{"text", "user"}):
        a=json.dumps(i, sort_keys=True, default=json_util.default)
	data = json.loads(a)
	print data["user"]["location"].encode('UTF-8'),":",i["text"].encode('UTF-8')

'''	
#	print i["text"].encode('UTF-8')

#datai= tof.find({"text":re.compile('feliz')},{"text", "user"})
