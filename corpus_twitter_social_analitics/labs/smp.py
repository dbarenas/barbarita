import os
import sys
import pymongo
from bson import BSON
from bson import json_util

if __name__ == '__main__':
  try:
    connection = pymongo.Connection('mongodb://localhost:27017')
    database = connection['mongotest']
  except:
    print('Error: Unable to Connect')
    connection = None

  if connection is not None:
    database["test"].insert({'name': 'foo'})
    doc = database["test"].find_one({'name': 'foo'})
    return json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
