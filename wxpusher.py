import os
import requests
import json
import sys

def send_wxpusher_message(content):
    token = os.getenv("WXPUSHER_APP_TOKEN")
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

    message = sys.argv[1]
    wxpusher(message)
