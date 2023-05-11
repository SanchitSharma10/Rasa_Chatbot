import requests
import json
import time
from datetime import datetime, timedelta

# Define the URL for the Zendesk Chat History API
url = 'https://www.zopim.com/api/v2/chats'
ZENDESK_API_TOKEN = "Xn3QjM00xDU2dZvFt47sGsHu8mOuAhLl25gGDHL0IgUYrWPCbmQxakMbbFXQck7D"

# Set up the request headers with your authentication credentials
headers = {
    'content-type': 'application/json',
    'Authorization': f'Bearer {ZENDESK_API_TOKEN}'
}

# Create a dictionary to store the last message timestamp for each chat
last_timestamps = {}

threshold_datetime = datetime.now() - timedelta(minutes=1)  # Adjust the timedelta to your desired time window

while True:  # Run the script indefinitely
    print("Polling Zendesk Chat History API...")
    try:
        # Send the API request to retrieve chat sessions
        response = requests.get(url, headers=headers)

        # Parse the JSON response
        data = json.loads(response.text)
        chats = data.get('chats')

        # Loop through each chat session
        for chat in chats:
            # Retrieve the chat ID
            chat_id = chat['id']

            # Get the history from the chat data
            history = chat.get('history')

            if history:
                # Extract the chat messages from the history
                messages = [item for item in history if item['type'] == 'chat.msg']

                if messages:
                    # Extract the latest chat message
                    latest_message = messages[-1]

                    # Get the latest message timestamp
                    latest_timestamp = latest_message.get('timestamp')
                    # Convert the message timestamp to a datetime object
                    message_datetime = datetime.fromisoformat(latest_timestamp.rstrip('Z'))
                    # Check if there's a stored timestamp for the chat and if the latest message is newer
                    if (chat_id not in last_timestamps or message_datetime > last_timestamps[chat_id]) and message_datetime > threshold_datetime:
                        # Print the message text and timestamp
                        print(f"Chat ID {chat_id}: Message: {latest_message.get('msg')}")
                        print(f"Timestamp: {latest_timestamp}")

                        # Update the last message timestamp for the chat
                        last_timestamps[chat_id] = message_datetime

        # Wait for a certain period before sending another request to the API (e.g., 10 seconds)
        time.sleep(10)

    except Exception as e:
        print(e)
