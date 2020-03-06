import requests
import re
import json


def hashTagGetter(astr,aint):
    i = 0
    while i < aint:
        url = "https://api.hashtagify.me/1.0/tag/" + astr
        headers = {
          'authorization': "Bearer 990bef44f88a9d3132c06ed94711e00642346d0d",
          'cache-control': "no-cache"
        }
        response = requests.request("GET", url, headers=headers,verify=False)

        json_data = response.json()
        print(json_data)

    


        top_influencers = json_data[astr]['top_influencers']

        for value in top_influencers:
            print(value[0])
        astr = str(json_data[astr]['related_tags']['name'])
        print("related hashtag: " + astr)
        i += 1
    return

def main():
    userInputHashtag = input("Enter a hashtag: ")
    userInputCycles = int(input("Enter an integer: "))
    
    
    
    hashTagGetter(userInputHashtag,userInputCycles)
        

main()

    







