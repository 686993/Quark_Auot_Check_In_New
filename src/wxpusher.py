import os
import requests

def send_wxpusher_notification(message):
    app_token = os.getenv('WX_APP_TOKEN')
    uid = os.getenv('WX_UID')
    url = 'https://wxpusher.zjiecode.com/api/send/message'

    data = {
        'appToken': app_token,
        'content': message,
        'uids': [uid],
        'url': '',  # 可选，点击通知后跳转的 URL
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Notification sent:', response.json())
    else:
        print('Failed to send notification:', response.text)

if __name__ == '__main__':
    message = '夸克网盘签到成功！'
    send_wxpusher_notification(message)
    
