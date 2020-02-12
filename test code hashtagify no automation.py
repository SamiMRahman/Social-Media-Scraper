import requests
import re
import json
astr = 'elderly'

url = "https://api.hashtagify.me/1.0/tag/" + astr

headers = {
  'authorization': "Bearer 4cf68da56551682d21fb738b250b2515502d76a9",
  'cache-control': "no-cache"
}


response = requests.request("GET", url, headers=headers, verify=False)

json_data = response.json()


top_influencers = json_data[astr]['top_influencers']

for value in top_influencers:
    print(value[0])

print(json_data[astr]['related_tags'])






