# 🚀 快速開始指南

## 立即開始使用

### 步驟 1️⃣：準備照片資料

✅ **您已經完成此步驟！**

當前資料狀態：
- **cookieslu**: 8 張訓練照片 + 3 張測試照片
- **helu**: 8 張訓練照片 + 3 張測試照片
- **jay**: 8 張訓練照片 + 3 張測試照片

詳細資訊請查看 [DATA_INFO.md](DATA_INFO.md)

### 步驟 2️⃣：安裝相依套件

**方法一：使用安裝腳本（推薦）**
```bash
./install.sh
```
腳本會自動：
- 建立虛擬環境
- 安裝所有相依套件

**方法二：使用啟動腳本（安裝+啟動）**
```bash
./run.sh
```
腳本會自動：
- 建立虛擬環境
- 安裝所有相依套件
- 啟動 Streamlit 應用程式

**方法三：手動安裝**
```bash
# 建立虛擬環境（建議）
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# 安裝相依套件
pip install -r requirements.txt

# 啟動應用程式
streamlit run app.py
```

⏱️ **預計時間**: 首次安裝約需 3-5 分鐘（包含下載 InsightFace 模型）

### 步驟 3️⃣：自訂分類顯示名稱（可選）

✅ **已設定完成！**

當前顯示名稱：
```python
CATEGORIES_DISPLAY = {
    'cookieslu': 'Cookies 呂',
    'helu': '何呂',
    'jay': '周杰倫',
}
```

如需修改，請編輯 `app.py` 檔案。

### 步驟 4️⃣：開始遊戲

1. 瀏覽器會自動開啟 http://localhost:8501
2. 點擊「🚀 開始初始化」按鈕
3. 等待 AI 模型載入（第一次會下載模型，需要一些時間）
4. 初始化完成後，點擊「🎮 開始遊戲」
5. 選擇答案，與 AI 一較高下！

## 📝 完整文檔

- **[README.md](README.md)** - 專案概述
- **[USAGE.md](USAGE.md)** - 詳細使用說明
- **[EXAMPLES.md](EXAMPLES.md)** - 範例與建議

## 🎯 常見問題快速解決

### Q: 執行 `./run.sh` 時出現權限錯誤
```bash
chmod +x run.sh
./run.sh
```

### Q: 初始化失敗「無法建立人臉特徵資料庫」
- 檢查 `photos/` 資料夾是否有子資料夾
- 檢查子資料夾內是否有圖片
- 確保圖片中有清晰的人臉

### Q: 第一次執行很慢
- 第一次執行會下載 InsightFace 模型（約 280MB）
- 模型會快取在 `~/.insightface/` 資料夾
- 之後執行就會很快

### Q: 想測試辨識準確度
```bash
python face_recognition.py
```

## 🎮 遊戲規則

1. AI 會隨機選擇一張測試照片
2. 您需要猜測照片屬於哪個分類
3. AI 也會同時進行預測
4. 答對得 1 分
5. 看誰的總分更高！

## 🛠️ 技術細節

- **人臉辨識**: InsightFace (buffalo_l 模型)
- **相似度計算**: 餘弦相似度
- **前端框架**: Streamlit
- **預設閾值**: 0.6（可在 `face_recognition.py` 中調整）

## 💡 小技巧

1. **提高準確度**：
   - 增加每個分類的訓練照片數量
   - 使用不同角度和光線的照片
   - 確保照片清晰度

2. **加快速度**：
   - 減少訓練照片數量（3-5 張即可）
   - 使用較小的圖片檔案

3. **更有趣的玩法**：
   - 混合不同藝人
   - 電影角色分類
   - 年代變化追蹤

## 🎓 學習資源

- [InsightFace GitHub](https://github.com/deepinsight/insightface)
- [Streamlit 文檔](https://docs.streamlit.io/)
- [蔡炎龍老師的 AI-Demo](https://github.com/yenlung/AI-Demo)

---

**開始享受與 AI 的 PK 吧！** 🎤✨
