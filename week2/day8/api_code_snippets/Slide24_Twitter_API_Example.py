# Twitter API Example using v2 Bearer Token (X / Twitter API required)
# NOTE: You need a Twitter Developer account and a Bearer Token

import requests

bearer_token = "YOUR_BEARER_TOKEN"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}
username = "TwitterDev"

# Endpoint to get user details by username
url = f"https://api.twitter.com/2/users/by/username/{username}"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    user_data = response.json()
    print("User ID:", user_data['data']['id'])
    print("Name:", user_data['data']['name'])
    print("Username:", user_data['data']['username'])
else:
    print("Failed to fetch Twitter data:", response.status_code)
