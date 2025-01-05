# ⭐️ 夸克网盘自动签到  
![GitHub stars](https://img.shields.io/github/stars/Liu8Can/Quark_Auot_Check_In)  ![GitHub forks](https://img.shields.io/github/forks/Liu8Can/Quark_Auot_Check_In)  ![License](https://img.shields.io/github/license/Liu8Can/Quark_Auot_Check_In)  ![Last Commit](https://img.shields.io/github/last-commit/Liu8Can/Quark_Auot_Check_In)  ![GitHub Actions](https://github.com/Liu8Can/Quark_Auot_Check_In/actions/workflows/quark_signin.yml/badge.svg)


🎉 **本项目实现了夸克网盘的自动签到功能**，通过 GitHub Actions 自动执行，领取每日签到奖励空间，让用户无需手动操作！  

> 🛑 **警告**：本项目遵循 [MIT 协议](https://opensource.org/licenses/MIT)。任何对项目的修改和发布必须保留原作者署名。  
> 本仓库严厉谴责 [2pacJay/Quark_Auot_Check_In](https://github.com/2pacJay/Quark_Auot_Check_In) 仓库 **抹除原作者署名权的行为**，该行为严重违反 MIT 协议，侵害开源精神！  

---

## 🚀 功能简介  
- **每日自动签到**：定时运行脚本完成每日签到，领取成长奖励。  
- **GitHub Actions 托管**：一键配置后，脚本每天自动运行，实现真正的“一劳永逸”。
- 本项目基于 BNDou大佬的项目中夸克网盘自动签到的子功能 https://github.com/BNDou/Auto_Check_In 修改而来 

---

## 📋 使用指南  

### 1️⃣ Fork 项目  
点击右上角的 `Fork` 按钮，将本项目复制到自己的 GitHub 仓库。  

### 2️⃣ 配置 Cookie 信息  
通过 GitHub Secrets 配置用户的 Cookie 信息，具体步骤如下：  

#### 🛠️ 获取 COOKIE_QUARK  
使用手机抓包工具（推荐 [proxypin](https://proxypin.example)）获取 Cookie 信息：  
1. 打开手机抓包工具，访问夸克网盘签到页。  
2. 找到接口 `https://drive-m.quark.cn/1/clouddrive/capacity/growth/info` 的请求信息。  
3. 复制请求中的参数：`kps`、`sign` 和 `vcode`。  
4. 将参数整理为以下格式：  
   ```
   user=张三; kps=abcdefg; sign=hijklmn; vcode=111111111;
   ```
   > `user` 字段为用户名，可随意填写。多个账户可用 **回车或 && 分隔**。

#### 🔐 添加到 GitHub Secrets  
1. 打开 Fork 仓库，进入 **Settings -> Secrets and variables -> Actions**。  
2. 点击 **New repository secret** 按钮，创建 `COOKIE_QUARK`。  
3. 将整理好的 Cookie 信息粘贴到值中并保存。  

---

### 3️⃣ 启用 GitHub Actions  
1. 打开仓库的 **Actions** 选项卡。  
2. 启用 GitHub Actions，会看到 `Quark Sign-in` 工作流已配置完成。  
3. 脚本将每天定时运行并输出签到结果。  

### 4️⃣ 手动测试运行  
1. 进入 **Actions** 选项卡，点击 `Quark Sign-in` 工作流。  
2. 点击右侧的 **Run workflow** 按钮，手动触发任务以验证配置是否成功。  

---

## ❓ 常见问题  

1. **签到失败**：  
   - 确认 Cookie 信息准确无误且格式正确。  
   - 确保网络正常，并尝试重新抓取 Cookie。  

2. **GitHub Actions 未生效**：  
   - 确保已 Fork 项目并启用 GitHub Actions。  

---

## ⚠️ 注意事项  
- 本项目仅供学习交流，请勿用于非法用途。  
- 如夸克网盘更新接口，需重新获取 Cookie 并调整代码。  

---

## 📜 免责声明  
本项目为开源项目，作者不对任何因使用本项目产生的后果负责。  

---

### 🛡️ 防盗声明  
本项目严格遵守 MIT 协议，修改和分发时必须保留原作者署名及协议声明。  
若发现违反行为，请通过以下方式联系：  
📧 Email: [liucan01234@gmail.com](mailto:liucan01234@gmail.com)  

---  

🎉 **欢迎提交 PR 和 Star 支持项目发展！**  
