import os
import requests
import json
import sys

def send_wxpusher_message(content):
    token = os.getenv("WXPUSHER_TOKEN")
    uid = os.getenv("WXPUSHER_UID")

    url = "http://wxpusher.zjiecode.com/api/send/message"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appToken": token,
        "content": content,
        "contentType": 1,
        "uids": [uid],
        "url": "",
        "topicIds": [],
        "verifyPay": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wxpusher.py <message>")
        sys.exit(1)

    message_path = sys.argv[1]
    with open(message_path, 'r', encoding='utf-8') as file:
        message = file.read()
    send_wxpusher_message(message)
