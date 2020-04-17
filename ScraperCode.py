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
        
    
    
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))
    with open(hashtag_phrase + '.csv', 'w',encoding ='utf-8') as file:
        w = csv.writer(file)
        w.writerow(['tweet_text', 'username', 'all_hashtags', 'followers_count','profile_link'])
        hashtags = {}
        queries = 100
        List = []
        for i in range(queries):
            List.append([])

        

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        foundUsers = []
        foundHashtags = []
        foundFollowerCount = []
        foundTweetText = []
        

        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(queries):
            
            foundUsers.append(tweet.user.screen_name)
            foundHashtags.append([e['text'] for e in tweet._json['entities']['hashtags']])
            foundFollowerCount.append(tweet.user.followers_count)
            foundTweetText.append(tweet.full_text.replace('\n',' '))
            


        for k in range(len(foundUsers)):
            List[k].append(foundUsers[k])
            List[k].append(foundHashtags[k])
            List[k].append(foundFollowerCount[k])
            List[k].append(foundTweetText[k])
##        print(List)

        results = {}
    
        for i in range(len(List)):
            for j in range(len(List[i][1])):
            
                if List[i][1][j].lower() in results:
                
                
                    results[List[i][1][j].lower()] += 1
                
                else:
                
                    results[List[i][1][j].lower()] = 1
                
                
        sortedResults = sorted(results.items(),key=lambda x: x[1], reverse=True)
        tooManyLists = []
        anotherFlippinList = []
        for ii in range(len(List)):
            anotherFlippinList.append(0)
        for a in range(len(sortedResults)):
            tooManyLists.append(sortedResults[a][0])

        filteredList = []
        coolestFilterNumberEver = 0
        for i in range(queries):
            filteredList.append([])
        
        for i in range(len(List)):
            for j in range(len(List[i][1])):
                if List[i][1][j] in tooManyLists:
                    
                    anotherFlippinList[i] += 1
                    
                    
                    
                
            if anotherFlippinList[i] >= (numberOfIterations+1):
                filteredList.append(List[i])

        filteredList[:] = [x for x in filteredList if x != []]

        listTime = []
        for jj in range(len(filteredList)):
            if filteredList[jj][0] not in listTime:
                listTime.append(filteredList[jj][0])
                w.writerow([filteredList[jj][3], filteredList[jj][0], filteredList[jj][1], filteredList[jj][2],'twitter.com/'+filteredList[jj][0]])

    return list
            
            
consumer_key = "ghybXiUPe9ixRZNGJKxQsOgv8"
consumer_secret = "UEzdwWgy0IOZOZ1Qk5nuvmquDQ1wkyiaOaZAmrRbMGK1fLeVt3"
access_token = "4497707541-j5FJ6vDwrCws68RaKIaynP4ZhX7sfdQDF5o0E3C"
access_token_secret = "i0aGublGJ13ipAZOuhmQ8tG7Gyr3UKDIlkpl2ukMjEfdd"
hashtag_phrase = input('Hashtag Phrase: ')
anything = int(input('Number of Related Hashtags: '))


def main():

    h = search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, anything)
    print("Done.")
    
    
main()
