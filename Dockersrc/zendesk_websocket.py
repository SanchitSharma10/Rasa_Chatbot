import requests
import time
import base64


ZENDESK_API_BASE_URL = "https://actosupport.zendesk.com/api/v2/chats"
ZENDESK_EMAIL = "sanchit@actoapp.com"
ZENDESK_API_TOKEN = "PjSG65QPTji58q3eG3sG7UrE2ZhPPFiZCbyjIV3G"
FLASK_APP_URL = "http://127.0.0.1:5000/webhooks/rasa"

auth_string = f"{ZENDESK_EMAIL}/token:{ZENDESK_API_TOKEN}"
auth_string_encoded = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_string_encoded}"
}

import requests

CHAT_API_URL = "https://chat-api.zopim.com/graphql/request"

query = """
mutation {
  startAgentSession(access_token: "my_oauth_access_token") {
    websocket_url
    session_id
    client_id
  }
}
"""

response = requests.post(
    CHAT_API_URL,
    json={"query": query},
    headers={"Content-Type": "application/json"},
)

print(response.json())
