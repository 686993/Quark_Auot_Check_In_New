import os
import sys
import requests

def send_wxpusher_message(app_token, uid, message):
    """
    发送消息到 WxPusher
    :param app_token: WxPusher AppToken
    :param uid: 用户的 UID
    :param message: 要发送的消息内容
    """
    # 构建请求数据
    data = {
        "appToken": app_token,
        "content": message,
        "contentType": 1,  # 文本消息
        "uids": [uid]
    }

    # 发送请求
    response = requests.post("http://wxpusher.zjiecode.com/api/send/message", json=data)

    # 检查响应
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

def main():
    # 从环境变量中获取 WxPusher 配置
    app_token = os.getenv('WXPUSHER_APP_TOKEN')
    uid = os.getenv('WXPUSHER_UID')

    # 检查环境变量是否已设置
    if not app_token or not uid:
        print("Error: WXPUSHER_APP_TOKEN and WXPUSHER_UID must be set as environment variables.")
        sys.exit(1)

    # 从命令行参数中获取消息内容
    if len(sys.argv) < 2:
        print("Usage: python wxpusher.py <message>")
        sys.exit(1)

    message = sys.argv[1]

    # 发送消息
    send_wxpusher_message(app_token, uid, message)

if __name__ == "__main__":
    main()
