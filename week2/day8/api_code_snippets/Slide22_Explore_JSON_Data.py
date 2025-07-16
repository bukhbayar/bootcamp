# Let's simulate a more complex JSON response
mock_response = {
    "user": {
        "id": 101,
        "name": "Alice",
        "email": "alice@example.com",
        "social": {
            "twitter": "@alice_in_data",
            "youtube": "AliceDataChannel"
        }
    },
    "subscriptions": [
        {"service": "Twitter", "active": True},
        {"service": "YouTube", "active": True}
    ]
}

# Access nested JSON keys
print("User ID:", mock_response["user"]["id"])
print("Twitter Handle:", mock_response["user"]["social"]["twitter"])

# Loop through subscriptions
for sub in mock_response["subscriptions"]:
    print(f"{sub['service']}: Active = {sub['active']}")
