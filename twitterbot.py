# Imports

import tweepy
import random
import time

# Keys and Access Tokens

CONSUMER_KEY    = 'DPWn6Lb94U8thsbRXpIGN1B9o'
CONSUMER_SECRET = 'Q5RIFprVcVB3Ko1z6a6TdJtjz0edVmkeeu8ARm7c3IKBXqAkBW'

ACCESS_TOKEN    = '1017154560253571073-WUnJ4GCl2f7o6QjXq1XV1o1sDsXfnE'
ACCESS_SECRET   = 'ofNrtDh7QJoFMvntgZURZAsEfVCM9tT2HF5suAp2JXu40'

tweets = ["you are a snacc", "are you google? cuz i just found what i was looking for", "how u doinnn"]


# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
while True:
    count += 1
    index = random.randint(0, len(tweets) - 1)
    api.update_status(tweets[index] + str(count))
    time.sleep(5)
