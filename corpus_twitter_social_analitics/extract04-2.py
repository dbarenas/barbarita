# see "Authentication" section below for tokens and keys
# -*- coding: utf-8 -*-
from twitter import *
import os
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET
import json


MY_TWITTER_CREDS = os.path.expanduser('/home/dbarenas/.twitter_oauth')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

t = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))



# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reasone
#t.users.lookup(screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# Search for the latest tweets about #pycon
query="mal servicio"
out=t.search.tweets(q=query)

#text=stt[:]['text']
stt= json.dumps(out, sort_keys=True,indent=4, separators=(',', ': '), )
print stt
