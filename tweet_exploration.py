# Import Libraries
import json

file = open("tweets.json", "r")
data = json.load(file) # Load from file into a json object

for d in data: # dat is a list, d is a dictionary
    # # Loop through the dictionary (which corresponds to a single tweet)

    # TO PRINT OUR DICTIONARY
    # for info_category, info in d.items():
    #     print(info_category, info)


    # TO PRINT THE TWEET TEXT
    # print(d["text"])

    # TO PRINT THE FAVOURITES COUNT
    # print(d["user"]["favourites_count"])
        # d is our dictionary about our tweet
    print(d["retweet_count"])
    # for user_mention in d["user_mentions"]:
    #     # Each user_mention is a dictionary
    #     # i correspond
    #     print(user_mention["screen_name"])
    break
