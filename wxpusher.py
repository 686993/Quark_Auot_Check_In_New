# send_wxpusher.py
import requests
import os

def wxpusher(title, content):
    app_token = os.getenv('WXPUSHER_APP_TOKEN')
    uid = os.getenv('WXPUSHER_UID')
    url = f"https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appToken": app_token,
        "content": content,
        "summary": title,
        "contentType": 1,
        "uids": [uid]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("通知发送成功")
    else:
        print(f"通知发送失败: {response.text}")

if __name__ == "__main__":
    import sys
    title = sys.argv[1]
    content = sys.argv[2]
    wxpusher(title, content)
