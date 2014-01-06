from pymongo import Connection
import datetime
import json
from StringIO import StringIO
import codecs
import re

connection = Connection('localhost', 27017)

db = connection.twemotion
tof= db.tweets
tw = tof.count()

emo=[]
fo = open("lista_emociones", "r")
for i in fo.readlines():
	emo.append(i.replace("\n",""))

print "****"

for emotion in emo:
	print emotion,"::",tof.find({"text": re.compile(emotion)},{"text"}).count()
print "****"	

#print tof.find({"text": re.compile("triste")},{"text"}).count()

print "emotion:  ",tw
'''
fo = open("lista_emociones", "r")
for i in fo.readlines():
	print i, tof.find({"text": re.compile(i)},{"text"}).count()
print "*"*50
'''
