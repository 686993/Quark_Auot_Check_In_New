import os
import re
import sys
import requests
import wxpusher # 导入 wxpusher 模块

cookie_list = os.getenv("COOKIE_QUARK").split('\n|&&')

# 替代 notify 功能，现在调用 wxpusher 模块
# 这个函数将不再直接发送，而是返回要发送的完整消息
def format_notification_message(title, message):
    # WxPusher的 content 字段就是消息主体，title可以作为消息的一部分
    # 确保所有详细信息都在 message 参数中
    return f"{title}\n{message}"

# 获取环境变量
def get_env():
    # 判断 COOKIE_QUARK是否存在于环境变量
    if "COOKIE_QUARK" in os.environ:
        # 读取系统变量以 \n 或 && 分割变量
        cookie_list = re.split('\n|&&', os.environ.get('COOKIE_QUARK'))
    else:
        # 标准日志输出
        print('❌未添加COOKIE_QUARK变量')
        # 在这里不调用 send，因为 send 现在是用来构建消息的
        # main函数会在最后统一发送通知
        sys.exit(0)

    return cookie_list

# 其他代码...

class Quark:
    '''
    Quark类封装了签到、领取签到奖励的方法
    '''
    def __init__(self, user_data):
        '''
        初始化方法
        :param user_data: 用户信息，用于后续的请求
        '''
        self.param = user_data

    def convert_bytes(self, b):
        '''
        将字节转换为 MB GB TB
        :param b: 字节数
        :return: 返回 MB GB TB
        '''
        units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = 0
        while b >= 1024 and i < len(units) - 1:
            b /= 1024
            i += 1
        return f"{b:.2f} {units[i]}"

    def get_growth_info(self):
        '''
        获取用户当前的签到信息
        :return: 返回一个字典，包含用户当前的签到信息
        '''
        url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/info"
        querystring = {
            "pr": "ucpro",
            "fr": "android",
            "kps": self.param.get('kps'),
            "sign": self.param.get('sign'),
            "vcode": self.param.get('vcode')
        }
        response = requests.get(url=url, params=querystring).json()
        #print(response)
        if response.get("data"):
            return response["data"]
        else:
            return False

    def get_growth_sign(self):
        '''
        获取用户当前的签到信息
        :return: 返回一个字典，包含用户当前的签到信息
        '''
        url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign"
        querystring = {
            "pr": "ucpro",
            "fr": "android",
            "kps": self.param.get('kps'),
            "sign": self.param.get('sign'),
            "vcode": self.param.get('vcode')
        }
        data = {"sign_cyclic": True}
        response = requests.post(url=url, json=data, params=querystring).json()
        #print(response)
        if response.get("data"):
            return True, response["data"]["sign_daily_reward"]
        else:
            return False, response["message"]

    def queryBalance(self):
        '''
        查询抽奖余额
        '''
        url = "https://coral2.quark.cn/currency/v1/queryBalance"
        querystring = {
            "moduleCode": "1f3563d38896438db994f118d4ff53cb",
            "kps": self.param.get('kps'),
        }
        response = requests.get(url=url, params=querystring).json()
        # print(response)
        if response.get("data"):
            return response["data"]["balance"]
        else:
            return response["msg"]

    def do_sign(self):
        '''
        执行签到任务
        :return: 返回一个字符串，包含签到结果
        '''
        log = ""
        # 每日领空间
        growth_info = self.get_growth_info()
        if growth_info:
            log += (
                f" {'88VIP' if growth_info['88VIP'] else '普通用户'} {self.param.get('user')}\n"
                f"💾 网盘总容量：{self.convert_bytes(growth_info['total_capacity'])}，"
                f"签到累计容量：")
            if "sign_reward" in growth_info['cap_composition']:
                log += f"{self.convert_bytes(growth_info['cap_composition']['sign_reward'])}\n"
            else:
                log += "0 MB\n"
            if growth_info["cap_sign"]["sign_daily"]:
                log += (
                    f"✅ 签到日志: 今日已签到+{self.convert_bytes(growth_info['cap_sign']['sign_daily_reward'])}，"
                    f"连签进度({growth_info['cap_sign']['sign_progress']}/{growth_info['cap_sign']['sign_target']})\n"
                )
            else:
                sign, sign_return = self.get_growth_sign()
                if sign:
                    log += (
                        f"✅ 执行签到: 今日签到+{self.convert_bytes(sign_return)}，"
                        f"连签进度({growth_info['cap_sign']['sign_progress'] + 1}/{growth_info['cap_sign']['sign_target']})\n"
                    )
                else:
                    log += f"❌ 签到异常: {sign_return}\n"
        else:
            # log += f"❌ 签到异常: 获取成长信息失败\n"
            raise Exception("❌ 签到异常: 获取成长信息失败")  # 适用于单账号情形，当 cookie 值失效后直接报错，方便通过 github action 的操作系统来进行提醒 如果你使用的是多账号签到的话，不要跟进此更新

        return log


def main():
    '''
    主函数
    :return: 返回一个字符串，包含签到结果
    '''
    msg = ""
    global cookie_quark
    cookie_quark = get_env()

    print("✅ 检测到共", len(cookie_quark), "个夸克账号\n")

    i = 0
    while i < len(cookie_quark):
        # 获取user_data参数
        user_data = {}  # 用户信息
        for a in cookie_quark[i].replace(" ", "").split(';'):
            if not a == '':
                user_data.update({a[0:a.index('=')]: a[a.index('=') + 1:]})
        # print(user_data)
        # 开始任务
        log = f"🙍🏻‍♂️ 第{i + 1}个账号"
        msg += log
        # 登录
        log = Quark(user_data).do_sign()
        msg += log + "\n"

        i += 1

    # print(msg) # 可以用于调试，但通常不需要在生产环境中打印

    print("----------夸克网盘签到完毕----------")

    # WxPusher调用信息放在----------夸克网盘签到完毕----------的后面
    try:
        # 获取 WXPUSHER_APP_TOKEN 和 WXPUSHER_UID 环境变量
        WXPUSHER_APP_TOKEN = os.getenv("WXPUSHER_APP_TOKEN")
        WXPUSHER_UID = os.getenv("WXPUSHER_UID")

        if not WXPUSHER_APP_TOKEN or not WXPUSHER_UID:
            print("❌ WXPUSHER_APP_TOKEN 或 WXPUSHER_UID 环境变量未设置，无法发送WxPusher消息。")
            # 不再退出，只是不发送通知
        else:
            # 调用 wxpusher.py 中的 wxpusher 函数
            # 使用 format_notification_message 来组织最终的发送内容
            final_notification_content = format_notification_message('夸克自动签到', msg)
            wxpusher.wxpusher(WXPUSHER_APP_TOKEN, WXPUSHER_UID, final_notification_content)
            print("✅ 消息已通过WxPusher发送。")
    except Exception as err:
        print(f'❌ 调用 WxPusher 失败: {err}')
        # 依然打印签到信息到日志，以防通知失败
        print(f"签到结果:\n{msg}")

    return msg[:-1]


if __name__ == "__main__":
    print("----------夸克网盘开始签到----------")
    main()
