import requests
import time

# Display title when script runs
print("@YOURFAVNIGGAHERE On TG")

# API endpoint for sending tap requests
url = "https://api.monkeyrush.fun/api/v1/game/tap"

# Function to load auth tokens from data.txt
def load_auth_tokens(file_path="data.txt"):
    try:
        with open(file_path, "r") as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print("Error: data.txt file not found!")
        return []

# Load auth tokens from file
auth_tokens = load_auth_tokens()
if not auth_tokens:
    print("No tokens found. Exiting...")
    exit()

# Payload specifying the tap score
payload = {
    "score": 7  # Each tap increments score by 7 to match manual tapping
}

# Function to send a tap request to the API for a given token
def send_tap(token):
    headers = {"Authorization": token}  # Set the authorization token dynamically
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"Tap sent for {token[:20]}... Status Code: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"Error sending tap for {token[:20]}...: {e}")

# Infinite loop to continuously send taps for all accounts
while True:
    # Tap 1000 times per second for 1 minute
    start_time = time.time()
    while time.time() - start_time < 60:  # Loop runs for 60 seconds
        for _ in range(1000):  # Perform 1000 tap requests per second
            for token in auth_tokens:  # Loop through all accounts
                send_tap(token)

    # Wait for 2 minutes before resuming taps
    print("Waiting for 2 minutes...")
    time.sleep(120)  # Pause execution for 120 seconds
