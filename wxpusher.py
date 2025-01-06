import os
import requests
import json
import sys

def wxpusher(content):
    token = os.getenv("WXPUSHER_APP_TOKEN")
    uid = os.getenv("WXPUSHER_UID")

    url = "http://wxpusher.zjiecode.com/api/send/message"  # 修正 URL 字符串
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
    try:
        with open(message_path, 'r', encoding='utf-8') as file:
            message = file.read()
        response = wxpusher(message)
        print("推送结果:", response)
    except FileNotFoundError:
        print(f"Error: File not found at {message_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
