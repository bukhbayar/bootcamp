# Import requests library
import requests

# Define the API endpoint (example: public cat facts API)
url = "https://catfact.ninja/fact"

# Send GET request to the API
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    print(data)
    print("Fact:", data.get("fact"))
else:
    print("Failed to retrieve data.")
