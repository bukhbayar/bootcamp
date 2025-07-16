import requests
import time

# Simulate paginated API using placeholder API
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Add headers (if needed) and make request
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises error for bad status

    posts = response.json()

    # Save first 5 posts to file
    for post in posts[:5]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")

    # Respect API rate limits (simulate)
    time.sleep(1)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
