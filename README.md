# ⭐️ 夸克网盘自动签到

![GitHub stars](https://img.shields.io/github/stars/Liu8Can/Quark_Auot_Check_In) ![GitHub forks](https://img.shields.io/github/forks/Liu8Can/Quark_Auot_Check_In) ![License](https://img.shields.io/github/license/Liu8Can/Quark_Auot_Check_In) ![Last Commit](https://img.shields.io/github/last-commit/Liu8Can/Quark_Auot_Check_In) ![GitHub Actions](https://github.com/Liu8Can/Quark_Auot_Check_In/actions/workflows/quark_signin.yml/badge.svg)

🎉 **本项目实现了夸克网盘的自动签到功能**，通过 GitHub Actions 自动执行，领取每日签到奖励空间，让用户无需手动操作！

> 🛑 **警告**：本项目遵循 [MIT 协议](https://opensource.org/licenses/MIT)。任何对项目的修改和发布必须保留原作者署名。
>
> **本项目禁止传播，有缘人自会看到。**
>
> 本仓库严厉谴责 [2pacJay/Quark_Auot_Check_In](https://github.com/2pacJay/Quark_Auot_Check_In) 仓库 **抹除原作者署名权的行为**，该行为严重违反 MIT 协议，侵害开源精神！

---

## 🚀 功能简介

- **每日自动签到**：定时运行脚本完成每日签到，领取成长奖励。
  - **新增：每日两次签到尝试**：分别在北京时间早上 9 点和下午 1 点左右尝试签到，增加成功率。
  - **新增：防止重复签到**：脚本会记录当日成功签到状态，避免不必要的重复执行。
  - **新增：随机延迟执行**：每次签到前加入随机延迟，模拟人工操作，降低被检测风险。
- **GitHub Actions 托管**：一键配置后，脚本每天自动运行，实现真正的“一劳永逸”。
  - **新增：自动保持仓库活跃**：通过空提交防止 GitHub因仓库不活跃而禁用 Actions。
  - **新增：自动清理旧记录**：自动删除旧的 Workflow 运行记录，保持 Actions 页面整洁。
- 本项目基于 BNDou大佬的项目中夸克网盘自动签到的子功能 https://github.com/BNDou/Auto_Check_In 修改而来
- 感谢  [Spectrollay](https://github.com/Spectrollay) 对工作流的优化

---

## 📋 使用指南

### 1️⃣ Fork 项目

点击右上角的 `Fork` 按钮，将本项目复制到自己的 GitHub 仓库。

### 2️⃣ 配置 Cookie 信息

通过 GitHub Secrets 配置用户的 Cookie 信息，具体步骤如下：

#### 🛠️ 获取 COOKIE_QUARK

使用手机抓包工具（小白推荐 [proxypin](https://github.com/wanghongenpin/proxypin)）获取 Cookie 信息：

1. 打开手机抓包工具，访问夸克网盘签到页。
2. 找到接口 `https://drive-m.quark.cn/1/clouddrive/capacity/growth/info` 的请求信息。
3. 复制请求中的参数：`kps`、`sign` 和 `vcode`。【初步测试发现这个 Key 的值有效期在两个月左右】
4. 将参数整理为以下格式：
   ```
   user=张三; kps=abcdefg; sign=hijklmn; vcode=111111111;
   ```

   > `user` 字段为用户名，可随意填写。多个账户可用 **回车或 && 分隔**。
   >

#### 🔐 添加到 GitHub Secrets

1. 打开 Fork 后的仓库，进入 **Settings -> Secrets and variables -> Actions**。
2. 点击 **Repository secrets** 分区下的 **New repository secret** 按钮。
3. 创建名为 `COOKIE_QUARK` 的 Secret。
4. 将整理好的 Cookie 信息粘贴到 "Secret" 输入框中并保存。

---

### 3️⃣ 启用 GitHub Actions 及设置权限

1. 打开 Fork 后的仓库，进入 **Actions** 选项卡。如果看到黄色的提示条 "Workflows aren't right ....... enable them"，点击 **"I understand my workflows, go ahead and enable them"** 按钮启用 Actions。
2. **重要：设置 Workflow 权限**
   * 进入仓库的 **Settings -> Actions -> General** 页面。
   * 在 "Workflow permissions" 部分，选择 **"Read and write permissions"**。
   * 点击 "Save" 保存。
   * **此步骤是必需的**，以便 Actions 能够执行“保持仓库活跃”（空提交）和“清理旧的工作流记录”等操作。
3. 启用后，你会看到名为 `Quark签到` (或 `Quark Sign-in`) 的工作流已配置完成。
4. 脚本将按预设时间（北京时间每日约 9:00 和 13:00）自动运行。
   * **运行时间说明**：默认设置在北京时间上午 9 点和下午 1 点左右运行。由于 GitHub Actions 的计划任务调度机制，实际运行时间可能会有几分钟到几十分钟的延迟，这是正常现象。随机延迟的加入也会影响确切的启动时间。
   * **执行逻辑**：脚本会先检查当天是否已成功签到。如果已签到，则跳过后续的签到操作。

### 4️⃣ 手动测试运行

1. 进入 **Actions** 选项卡，点击左侧的 `Quark签到` (或 `Quark Sign-in`) 工作流。
2. 点击右侧的 **Run workflow** 按钮，然后再次点击绿色 **Run workflow** 按钮，手动触发任务以验证配置是否成功。
3. 你可以点击运行中的 workflow 查看其执行日志和状态。

---

## ❓ 常见问题

1. **签到失败**：

   * 确认 `COOKIE_QUARK` Secret 中的信息准确无误且格式正确。
   * Cookie 可能已过期，请尝试重新抓取并更新 Secret。
   * 检查 Actions 日志，看是否有具体的错误信息。
2. **GitHub Actions 未生效或报错 `Permission denied` / `GH006`**：

   * 确保已按照【3️⃣ 启用 GitHub Actions 及设置权限】中的步骤启用了 Actions。
   * **最常见原因：** 确保在仓库的 "Settings -> Actions -> General" 中，"Workflow permissions" 已设置为 **"Read and write permissions"**。如果权限不足，空提交和清理记录步骤会失败。
   * 检查 Actions 运行日志，查看具体的错误信息。
3. **Workflow 显示跳过 (Skipped)**：

   * 这是新版功能的正常行为。如果当天的第一次签到尝试（例如早上9点的任务）已经成功，那么下午1点的任务在检查时会发现已签到，从而跳过实际的签到步骤。你可以在 `check-if-already-signed` job 的日志中看到类似 "今天已成功签到，跳过执行" 的信息。

---

## ⚠️ 注意事项

- 本项目仅供学习交流，请勿用于非法用途。
- 如夸克网盘更新接口，需重新获取 Cookie 并调整代码（主要是 `checkIn_Quark.py` 脚本，Workflow 通常无需修改）。
- 频繁手动触发可能会被目标服务限制，请谨慎操作。

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
