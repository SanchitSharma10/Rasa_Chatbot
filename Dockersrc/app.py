import requests
from flask import Flask, request, jsonify
import threading
import time
import base64


app = Flask(__name__)

ZENDESK_API_BASE_URL = "https://actosupport.zendesk.com/api/v2/chats"
ZENDESK_EMAIL = "sanchit@actoapp.com"
ZENDESK_API_TOKEN = "Y0iEOnCqWM00DcO1rbjpVVavxLJ2jeiuqnoW9NZhHJuJN62bpu6yoo2ixdq7JDJF"

# Encode the email and API token in Base64 format for Basic authentication
auth_string = f"{ZENDESK_EMAIL}/token:{ZENDESK_API_TOKEN}"
auth_string_encoded = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_string_encoded}"
}

@app.route("/webhooks/zendesk", methods=["POST"])
def zendesk_webhook():
    data = request.json
    sender = data.get("sender")
    message = data.get("message")
    
    print(f"Incoming message from sender {sender}: {message}")  # Print the incoming message

    # Send the message from the user to the chatbot
    response = send_message_to_chatbot(sender, message)
    print(f"Rasa chatbot response: {response}")  # Print the chatbot response

    # Send the response back to the user
    send_message_to_user(sender, response)
    print(f"Message sent back to Zendesk: {response}")  # Print the message sent back to Zendesk

    return jsonify({"status": "success"})


def send_message_to_user(sender, message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZENDESK_API_TOKEN}"
    }

    data = {
        "message": {
            "type": "text",
            "text": message
        }
    }

    url = f"{ZENDESK_API_BASE_URL}/conversations/{sender}/messages"
    requests.post(url, json=data, headers=headers)

def get_conversation(sender):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZENDESK_API_TOKEN}"
    }

    url = f"{ZENDESK_API_BASE_URL}/conversations/{sender}"

    params = {
        "wait_time": 30, #Maximum time to wait for new messages (in seconds)
        "timeout": 600 #Maximum time to keep tghe long polling connection open (in seconds)
    }
    response = requests.get(url, headers=headers, params=params)

    while response.status_code == 200:
        # Parse the respons e JSON to extract any new messages
        conversation = response.json
        messages = conversation.get("conversation").get("events")


        # Process each new message
        for message in messages:
            #Extract relevant data fields from the message
            message_type = message.get("type")
            text = message.get("body")
            sender_id = message.get("author_id")
            created_at = message.get("created_at")

            #Do something with the message data (e.g, call a bot function to process the message)
            print(f"New message received from sender {sender_id}: {text}")

        #Set up the next request to continue checking for new messages
        last_event_id =  messages[-1].get("id") if messages else None
        params["last_even_id"] = last_event_id
        response = requests.get(url, headers=headers, params=params)

    return None



def send_message_to_chatbot(sender, message):
    rasa_api_url = "https://dockersrc-sanchitsharma10.cloud.okteto.net/webhooks/rest/webhook"
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "sender": sender,
        "message": message
    }

    response = requests.post(rasa_api_url, json=data, headers=headers)

    if response.status_code == 200:
        # Extract the chatbot's response from the Rasa API response
        rasa_response = response.json()
        handoff = False

        # Check if any of the responses have the handoff action
        for res in rasa_response:
            if res.get("custom") and res["custom"].get("handoff"):
                handoff = True
                break

        return {"text": rasa_response[0]['text'], "handoff": handoff}
    else:
        return None

def delayed_check(sender):
    # Wait for a specified amount of time (e.g., 60 seconds)
    time.sleep(60)

    # Check if the conversation is still in the open queue
    conversation = get_conversation(sender)
    if conversation['status'] == 'open':
        # Send a message to the user if no agent picked up the conversation
        send_message_to_user(sender, "Sorry, no users are available at this time.")


def transfer_to_live_agent(sender):
    # This function transfers the conversation to a live agent
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZENDESK_API_TOKEN}"
    }

    data = {
        "routing": {
            "type": "transfer"
        }
    }

    url = f"{ZENDESK_API_BASE_URL}/conversations/{sender}/routing"
    requests.put(url, json=data, headers=headers)


if __name__ == "__main__":
    app.run(debug=True)
