import os 
import re 
import sys 
import requests 
import subprocess

# 替代 notify 功能
def send(title, message):
    print(f"{title}: {message}")

# 获取环境变量 
def get_env(): 
    if "COOKIE_QUARK" in os.environ: 
        cookie_list = re.split('\n|&&', os.environ.get('COOKIE_QUARK')) 
    else: 
        print('❌未添加COOKIE_QUARK变量') 
        send('夸克自动签到', '❌未添加COOKIE_QUARK变量') 
        sys.exit(0) 

    return cookie_list 

class Quark:
    def __init__(self, user_data):
        self.param = user_data

    def convert_bytes(self, b):
        units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = 0
        while b >= 1024 and i < len(units) - 1:
            b /= 1024
            i += 1
        return f"{b:.2f} {units[i]}"

    def get_growth_info(self):
        url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/info"
        querystring = {
            "pr": "ucpro",
            "fr": "android",
            "kps": self.param.get('kps'),
            "sign": self.param.get('sign'),
            "vcode": self.param.get('vcode')
        }
        try:
            response = requests.get(url=url, params=querystring).json()
            if response.get("data"):
                return response["data"]
            else:
                print(f"❌ 获取成长信息失败: {response.get('message')}")
                return False
        except requests.RequestException as e:
            print(f"❌ 请求异常: {e}")
            return False

    def get_growth_sign(self):
        url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign"
        querystring = {
            "pr": "ucpro",
            "fr": "android",
            "kps": self.param.get('kps'),
            "sign": self.param.get('sign'),
            "vcode": self.param.get('vcode')
        }
        data = {"sign_cyclic": True}
        try:
            response = requests.post(url=url, json=data, params=querystring).json()
            if response.get("data"):
                return True, response["data"]["sign_daily_reward"]
            else:
                print(f"❌ 获取签到信息失败: {response.get('message')}")
                return False, response["message"]
        except requests.RequestException as e:
            print(f"❌ 请求异常: {e}")
            return False, "请求异常"

    def queryBalance(self):
        url = "https://coral2.quark.cn/currency/v1/queryBalance"
        querystring = {
            "moduleCode": "1f3563d38896438db994f118d4ff53cb",
            "kps": self.param.get('kps'),
        }
        try:
            response = requests.get(url=url, params=querystring).json()
            if response.get("data"):
                return response["data"]["balance"]
            else:
                print(f"❌ 查询余额失败: {response.get('msg')}")
                return response["msg"]
        except requests.RequestException as e:
            print(f"❌ 请求异常: {e}")
            return "请求异常"

    def do_sign(self):
        log = ""
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
            log += f"❌ 签到异常: 获取成长信息失败\n"

        print(log)
        return log


def main():
    msg = ""
    cookie_quark = get_env()

    print(f"✅ 检测到共 {len(cookie_quark)} 个夸克账号\n")

    for i, cookie in enumerate(cookie_quark):
        user_data = {}
        for a in cookie.replace(" ", "").split(';'):
            if not a == '':
                user_data.update({a[0:a.index('=')]: a[a.index('=') + 1:]})
        log = f"🙍🏻‍♂️ 第{i + 1}个账号"
        print(log)
        msg += log + "\n"
        log = Quark(user_data).do_sign()
        msg += log + "\n"

    try:
        subprocess.run(['python', 'wxpusher.py', msg], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 调用 wxpusher.py 失败: {e}")
    except Exception as err:
        print(f"❌ 错误，请查看运行日志！: {err}")

    return msg[:-1]


if __name__ == "__main__":
    print("----------夸克网盘开始签到----------")
    main()
    print("----------夸克网盘签到完毕----------")
