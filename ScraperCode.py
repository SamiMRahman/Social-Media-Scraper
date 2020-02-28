import json
import csv
import tweepy
import re

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    #fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    #with open(hashtag_phrase + '.csv', 'w') as file:

        #w = csv.writer(file)

        #write header row to spreadsheet
        #w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])
    d = {"timestamp" : 0, "tweet_text" : 0, "username" : 0, "all_hashtags" : 0, "followers_count" : 0}
    hashtags = {}
    List = []

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(100):
        List.append([e['text'] for e in tweet._json['entities']['hashtags']])
        List.append(tweet.user.screen_name.encode('utf-8'))
        List.append(tweet.user.followers_count)
        hashtags[hashtag_phrase] = List
                    
            #d([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
    return hashtags
            
            #w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
consumer_key = "ghybXiUPe9ixRZNGJKxQsOgv8"
consumer_secret = "UEzdwWgy0IOZOZ1Qk5nuvmquDQ1wkyiaOaZAmrRbMGK1fLeVt3"
access_token = "4497707541-j5FJ6vDwrCws68RaKIaynP4ZhX7sfdQDF5o0E3C"
access_token_secret = "i0aGublGJ13ipAZOuhmQ8tG7Gyr3UKDIlkpl2ukMjEfdd"
hashtag_phrase = input('Hashtag Phrase ')


def main():

    h = search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
    print(h)
main()
