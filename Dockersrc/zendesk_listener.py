import requests
import time
from datetime import datetime, timedelta

ZENDESK_API_BASE_URL = "https://www.zopim.com/api/v2/chats?status=active"
ZENDESK_API_TOKEN = "Xn3QjM00xDU2dZvFt47sGsHu8mOuAhLl25gGDHL0IgUYrWPCbmQxakMbbFXQck7D"
ZENDESK_WEBHOOK_URL = "http://127.0.0.1:5000/webhooks/zendesk"




headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ZENDESK_API_TOKEN}"
}

last_processed_timestamps = {}



def process_messages(chat_id, messages):
    last_processed_timestamp = last_processed_timestamps.get(chat_id, 0)

    for message in messages:
        if message["type"] == "chat.msg":
            sender = message.get("name", "Unknown")
            content = message.get("msg", "")
            timestamp = message.get("timestamp", "")

            if timestamp > last_processed_timestamp:
                print(f"Detected message: {sender}, {content}")  # Print detected messages

                # Comment out the line below to avoid sending data to the Flask app
                # requests.post(ZENDESK_WEBHOOK_URL, json={"sender": sender, "message": content})
                last_processed_timestamps[chat_id] = timestamp




while True:
    print("Polling Zendesk Chat API...")
    response = requests.get(f"{ZENDESK_API_BASE_URL}?status=active", headers=headers)
    print(f"Zendesk API response status: {response.status_code}")  # Print the response status code
    print(f"Response content: {response.content}")  # Print the response content

    if response.status_code == 200:
        chats = response.json()["chats"]

        for chat in chats:
            if chat["history"]:
                process_messages(chat["id"], chat["history"])

    time.sleep(10)  # Poll the API every 10 seconds


# def process_messages(chat_id, messages):
#     last_processed_timestamp = last_processed_timestamps.get(chat_id, 0)

#     for message in messages:
#         if message["type"] == "message" and message["timestamp"] > last_processed_timestamp:
#             sender = chat_id
#             content = message["content"]

#             # Forward the message to the Flask app
#             requests.post(ZENDESK_WEBHOOK_URL, json={"sender": sender, "message": content})
#             print(f"Forwarded message to Flask app: {sender}, {content}")
#             last_processed_timestamps[chat_id] = message["timestamp"]

# while True:
#     print("Polling Zendesk Chat API...")
#     response = requests.get(f"{ZENDESK_API_BASE_URL}", headers=headers)
#     print(f"Zendesk API response status: {response.status_code}")

#     print(f"Response content: {response.text}")



#     if response.status_code == 200:
#         chats = response.json()["chats"]
#         print(f"Chats: {chats}")

#         for chat in chats:
#             if chat["status"] == "open" and chat["history"]:
#                 process_messages(chat["id"], chat["history"])


#     time.sleep(10)  # Poll the API every 10 seconds
