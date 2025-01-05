import requests
import os

def send_wxpusher_message(app_token, uid, content):
    url = "http://wxpusher.zjiecode.com/api/send/message"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appToken": app_token,
        "content": content,
        "contentType": 1,  # 1表示文本
        "uids": [uid]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print("消息发送失败")

if __name__ == "__main__":
    app_token = os.getenv("WXPUSHER_APP_TOKEN")
    uid = os.getenv("WXPUSHER_UID")
    content = "夸克网盘签到成功！"
    send_wxpusher_message(app_token, uid, content)
