import requests
import os

def send_wxpusher_notification(app_token, uid, content):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appToken": app_token,
        "content": content,
        "contentType": 1,  # 文本类型
        "uids": [uid]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("通知发送成功")
    else:
        print("通知发送失败，状态码：", response.status_code)

if __name__ == "__main__":
    app_token = os.getenv("WX_APP_TOKEN")
    uid = os.getenv("WX_UID")
    content = "夸克网盘签到成功！"
    send_wxpusher_notification(app_token, uid, content)
