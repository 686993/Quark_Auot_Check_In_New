import requests
import os

def send_notification(title, content):
    # 从环境变量中获取 wxpusher 的 API 密钥和应用 ID
    app_token = os.getenv('WXPUSHER_APP_TOKEN')
    uid = os.getenv('WXPUSHER_UID')
    
    if not app_token or not uid:
        print("WxPusher 配置不完整")
        return

    url = f"https://wxpusher.zjiecode.com/api/send/message"
    data = {
        "appToken": app_token,
        "content": content,
        "contentType": 1,  # 文本内容
        "topicIds": [uid],
        "url": "",
        "verifyPay": False
    }
    
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("通知发送成功")
    else:
        print("通知发送失败")

if __name__ == "__main__":
    import sys
    title = sys.argv[1]
    content = sys.argv[2]
    send_notification(title, content)
