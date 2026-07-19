# Horizon 企業 AI 情報雷達：試運行交接

本版本是一個低成本試運行配置：每天北京時間 07:00 生成最多 15 條中文摘要，發布到 GitHub Pages。它只需要一個由你保管的 `DEEPSEEK_API_KEY`；不使用 LWN、郵件、Twitter/X、Webhook 或付費聊天推送。

## 你需要親自完成

### 1. Fork 並取得自己的倉庫

1. 登入 GitHub；尚未註冊可前往 <https://github.com/signup>。
2. 建議在 GitHub 的 **Settings → Password and authentication** 開啟雙因素驗證。
3. 打開 <https://github.com/Thysrael/Horizon>，點擊右上角 **Fork**，建立公開 Fork。
4. 將這個本機版本中的修改提交並推送到你的 Fork。不要把任何 API Key 寫入檔案或提交紀錄。

### 2. 建立 DeepSeek API Key

1. 前往 <https://platform.deepseek.com/> 註冊或登入。
2. 依平台當前要求完成帳戶或儲值設定。
3. 在 API Keys 頁面建立一枚專供 Horizon 使用的 Key。
4. 只在建立時複製它，存入公司的密碼管理器；不要貼到聊天、Issue、程式碼或截圖。

### 3. 將 Key 存為 GitHub Actions Secret

在你的 Fork 依次打開：

**Settings → Secrets and variables → Actions → New repository secret**

- Name：`DEEPSEEK_API_KEY`
- Secret：貼上剛建立的 DeepSeek Key

GitHub 工作流程只會以環境變數讀取該 Secret。`GITHUB_TOKEN` 由 GitHub Actions 自動提供，不需要另外建立 Personal Access Token。

### 4. 啟用 Actions 與 Pages

1. 打開 Fork 的 **Actions** 頁面；如有提示，點擊啟用工作流程。
2. 選擇 **Daily Horizon Summary**，點擊 **Run workflow** 做首次手動試運行。
3. 等待執行成功後，打開 **Settings → Pages**。
4. 在 **Build and deployment** 將 Source 設為 **Deploy from a branch**，選擇 `gh-pages` 分支與 `/ (root)`。
5. 保存後，GitHub 會顯示 Pages 網址。之後排程會在每天 `23:00 UTC` 執行，即北京時間次日 07:00；GitHub 排程有時可能延遲。

## 首次驗收

- Actions 執行紀錄沒有洩露 Key，也沒有缺少 `DEEPSEEK_API_KEY` 的錯誤。
- `gh-pages` 分支和 Pages 網址已生成。
- 頁面中的摘要為中文，每天最多 15 條。
- 新聞來源包含 RSS、Hacker News、GitHub 與公開 Telegram；不發送郵件或 Webhook。

## 下一輪企業化所需資料

提供行業、關注國家或地區、競爭對手、技術主題、排除詞，以及老闆每天最想回答的三個問題後，再調整來源和篩選規則。第一階段不要在公開倉庫配置客戶名稱、未發布產品或其他機密情報。
