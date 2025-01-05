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

def generate_notification_message(sign_in_result, success):
    # 根据签到结果生成通知内容
    message = "----------夸克网盘开始签到----------\n"
    message += "✅ 检测到共 1 个夸克账号\n\n"
    
    if success:
        message += f"夸克自动签到: 🙍🏻‍♂️ 第1个账号 {sign_in_result['account_type']} {sign_in_result['account_name']}\n"
        message += f"💾 网盘总容量：{sign_in_result['total_capacity']}，签到累计容量：{sign_in_result['signed_capacity']}\n"
        message += f"✅ 签到日志: {sign_in_result['sign_log']}\n"
    else:
        message += "❌ 签到失败，请检查账号信息和网络连接\n"
    
    message += "\n----------夸克网盘签到完毕----------"
    return message

if __name__ == "__main__":
    app_token = os.getenv("WX_APP_TOKEN")
    uid = os.getenv("WX_UID")
    
    # 示例签到结果数据，实际使用时应从签到脚本获取
    sign_in_result = {
        "account_type": "普通用户",
        "account_name": "一号",
        "total_capacity": "31.88 GB",
        "signed_capacity": "10.88 GB",
        "sign_log": "今日已签到+20.00 MB，连签进度(1/7)"
    }
    
    # 假设签到成功
    success = True  # 实际使用时根据签到脚本的结果设置
    
    notification_message = generate_notification_message(sign_in_result, success)
    send_wxpusher_notification(app_token, uid, notification_message)
    
