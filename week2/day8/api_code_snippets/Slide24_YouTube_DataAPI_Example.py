# YouTube Data API Example (mocked structure)
# NOTE: To run this live, you'd need an actual API key from Google Cloud

import requests

api_key = "YOUR_API_KEY"  # replace with actual key
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Google Developers channel ID

# API endpoint to get channel details
url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    stats = data["items"][0]["statistics"]
    print("Subscribers:", stats["subscriberCount"])
    print("Video Count:", stats["videoCount"])
    print("View Count:", stats["viewCount"])
else:
    print("Error fetching data:", response.status_code)
