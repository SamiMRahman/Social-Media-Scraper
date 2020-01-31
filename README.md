# Social-Media-Scraper
Develop an automated process to find changemakers through nebulous social media hashtags.

Code to retrieve the ACCESS TOKEN:

import requests

url = "https://api.hashtagify.me/oauth/token"

payload = "grant_type=client_credentials&client_id=CONSUMER_KEY&client_secret=CONSUMER_SECRET"
headers = {
  'cache-control': "no-cache",
  'content-type': "application/x-www-form-urlencoded"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

response: { "token_type": "bearer", "access_token": ACCESS_TOKEN }


Code to retrieve hashtag:

import requests

url = "https://api.hashtagify.me/1.0/tag/smm"

headers = {
  'authorization': "Bearer ACCESS_TOKEN",
  'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

response: {"hashtag"}
