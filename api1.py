
import json
import csv
import tweepy
import re

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
"""
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, numberOfIterations):

    
    
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
    #d = {"timestamp" : 0, "tweet_text" : 0, "username" : 0, "all_hashtags" : 0, "followers_count" : 0}
    k = 0
    hashtagsSearchedFor = [hashtag_phrase]
    
    while k < numberOfIterations:
        hashtags = {}
        List = []

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(100):
            List.append([e['text'] for e in tweet._json['entities']['hashtags']])
            List.append(tweet.user.screen_name.encode('utf-8'))
            List.append(tweet.user.followers_count)
            hashtags[hashtag_phrase] = List

        results = {}
    
        for i in range(0, len(List), 3):
            for j in List[i]:
                if j in results:
                    results[j] = results[j] +1
                else:
                    results[j] = 1
        sortedResults = sorted(results.items(),key=lambda x: x[1], reverse=True)
        print(results)
       
        
        

        
        

        print(sortedResults)
        
        print(hashtagsSearchedFor)
        
        if sortedResults[1][0].lower() not in hashtagsSearchedFor:
            hashtagsSearchedFor.append(sortedResults[1][0])
            relatedhashtag = sortedResults[1][0]
        else:
            for a in range(len(sortedResults)):
                if sortedResults[a][0].lower() in hashtagsSearchedFor:
                    continue
                else:
                    hashtagsSearchedFor.append(sortedResults[a][0])
                    relatedhashtag = sortedResults[a][0]
                    break
        hashtag_phrase = relatedhashtag        
        print(relatedhashtag)
                

            
            
            
        k += 1
        
        
     
                    
            #d([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
    return list
            
            #w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
consumer_key = "ghybXiUPe9ixRZNGJKxQsOgv8"
consumer_secret = "UEzdwWgy0IOZOZ1Qk5nuvmquDQ1wkyiaOaZAmrRbMGK1fLeVt3"
access_token = "4497707541-j5FJ6vDwrCws68RaKIaynP4ZhX7sfdQDF5o0E3C"
access_token_secret = "i0aGublGJ13ipAZOuhmQ8tG7Gyr3UKDIlkpl2ukMjEfdd"
hashtag_phrase = input('Hashtag Phrase: ')
anything = int(input('Number of Searches: '))


def main():

    h = search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, anything)
    
    
main()
