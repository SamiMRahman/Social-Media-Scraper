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
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    
        

        #write header row to spreadsheet
        
    
    #k = 0
    #hashtagsSearchedFor = [hashtag_phrase]
    
    #while k < numberOfIterations: 
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))
    with open(hashtag_phrase + '.csv', 'w',encoding ='utf-8') as file:
        w = csv.writer(file)
        w.writerow(['tweet_text', 'username', 'all_hashtags', 'followers_count','profile_link'])
        hashtags = {}
        queries = 10
        List = []
        for i in range(queries):
            List.append([])
##            print(List)
        

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        foundUsers = []
        foundHashtags = []
        foundFollowerCount = []
        

        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(5):
            
            foundUsers.append(tweet.user.screen_name)
            foundHashtags.append([e['text'] for e in tweet._json['entities']['hashtags']])
            foundFollowerCount.append(tweet.user.followers_count)

        print(foundUsers)
        print(foundHashtags)
        print(foundFollowerCount)

        for k in range(len(foundUsers)):
            List[k].append(foundUsers[k])
            List[k].append(foundHashtags[k])
            List[k].append(foundFollowerCount[k])
        print(List)
            
            
##            i=+1
##            
##            
##            
##            List[i].append([e['text'] for e in tweet._json['entities']['hashtags']])
##            List[i].append(tweet.user.screen_name)
##            List[i].append(tweet.user.followers_count)
                    
                    
                
            #hashtags[hashtag_phrase] = List
            
##        print(List)
##        results = {}
##    
##        for i in range(0, len(List), 3):
##            for j in range(0, len(List[i]),3):
##                for k in List[i][j]:
##                    if k in results:
##                        results[k] = results[k] + 1
##                    else:
##                        results[k] = 1
##        sortedResults = sorted(results.items(),key=lambda x: x[1], reverse=True)
##        for k in range(len(sortedResults)):
##            numberOfRelatedHashtags = sortedResults
##            
##            
##
##        
##            
##        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(3):
##            if tweet.user.screen_name.replace('b', '', 1).replace('\'','') not in foundUsers and numberOfRelatedHashtags == k:
##                
##                w.writerow([tweet.full_text.replace('\n',' ').replace('b', '', 1), tweet.user.screen_name.replace('b', '', 1).replace('\'',''), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count,'twitter.com/'+tweet.user.screen_name.replace('b', '', 1).replace('\'','')])
##                foundUsers.append(tweet.user.screen_name.replace('b', '', 1).replace('\'',''))
                    #debug
                #print(foundUsers)
                    

##    results = {}
##    
##    for i in range(0, len(List), 3):
##        for j in List[i]:
##            if j in results:
##                results[j] = results[j] +1
##            else:
##                results[j] = 1
##    sortedResults = sorted(results.items(),key=lambda x: x[1], reverse=True)
    
    
##        debug
##        print(results)
##       
##        
##        
##
##        
##        
##        debug
##        print(sortedResults)
##        debug
##        print(hashtagsSearchedFor)
##        
##        if sortedResults[1][0].lower() not in hashtagsSearchedFor:
##            hashtagsSearchedFor.append(sortedResults[1][0])
##            relatedhashtag = sortedResults[1][0]
##        else:
##            for a in range(len(sortedResults)):
##                if sortedResults[a][0].lower() in hashtagsSearchedFor:
##                    continue
##                else:
##                    hashtagsSearchedFor.append(sortedResults[a][0])
##                    relatedhashtag = sortedResults[a][0]
##                    break
##        hashtag_phrase = relatedhashtag
##        debug
##        print(relatedhashtag)
                

            
            
            
        
        
        
     
                    
            
    return list
            
            
consumer_key = "ghybXiUPe9ixRZNGJKxQsOgv8"
consumer_secret = "UEzdwWgy0IOZOZ1Qk5nuvmquDQ1wkyiaOaZAmrRbMGK1fLeVt3"
access_token = "4497707541-j5FJ6vDwrCws68RaKIaynP4ZhX7sfdQDF5o0E3C"
access_token_secret = "i0aGublGJ13ipAZOuhmQ8tG7Gyr3UKDIlkpl2ukMjEfdd"
hashtag_phrase = input('Hashtag Phrase: ')
anything = int(input('Number of Related Hashtags: '))


def main():

    h = search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, anything)
    
    
main()
