# ✅ 啟動前檢查清單

## 當前專案狀態

### 📸 照片資料
- ✅ **cookieslu** (Cookies 呂)
  - 訓練照片：8 張 ✓
  - 測試照片：3 張 ✓
  
- ✅ **helu** (何呂)
  - 訓練照片：8 張 ✓
  - 測試照片：3 張 ✓
  
- ✅ **jay** (周杰倫)
  - 訓練照片：8 張 ✓
  - 測試照片：3 張 ✓

### 📂 檔案結構
- ✅ `app.py` - Streamlit 主程式
- ✅ `face_recognition.py` - 人臉辨識模組
- ✅ `requirements.txt` - 相依套件清單
- ✅ `install.sh` - 安裝腳本
- ✅ `run.sh` - 啟動腳本
- ✅ 資料夾結構完整

### ⚙️ 設定檔
- ✅ 分類顯示名稱已設定
- ✅ Streamlit 設定檔已建立
- ✅ .gitignore 已設定

## 🚀 快速啟動步驟

### 選項 1：一鍵啟動（推薦新手）

```bash
cd "/Users/benlu/Desktop/Applications/周杰倫種族分類PK"
./run.sh
```

這會自動：
1. 檢查並建立虛擬環境
2. 安裝所有相依套件（第一次執行）
3. 啟動 Streamlit 應用程式

### 選項 2：分步驟執行（推薦進階使用者）

**步驟 1: 安裝相依套件**
```bash
cd "/Users/benlu/Desktop/Applications/周杰倫種族分類PK"
./install.sh
```

**步驟 2: 測試辨識功能（可選）**
```bash
source venv/bin/activate  # 如果使用虛擬環境
python face_recognition.py
```

**步驟 3: 啟動應用程式**
```bash
source venv/bin/activate  # 如果使用虛擬環境
streamlit run app.py
```

## 📋 系統需求檢查

### 必要條件
- ✅ macOS 系統
- ✅ Python 3.8 或更高版本
- ⬜ 已安裝相依套件（執行 `./install.sh`）

### 磁碟空間
- 相依套件：約 500 MB
- InsightFace 模型：約 280 MB
- 總計需求：約 800 MB

### 網路需求
- 首次執行需要網路連線（下載模型）
- 之後可以離線使用

## ⚡ 預期執行時間

### 首次執行
1. **安裝相依套件**: 3-5 分鐘
2. **下載 InsightFace 模型**: 1-2 分鐘（取決於網速）
3. **建立人臉特徵資料庫**: 30-60 秒
4. **啟動應用程式**: 10-20 秒

**總計**: 約 5-8 分鐘

### 之後執行
1. **載入模型**: 10-20 秒
2. **建立特徵資料庫**: 30-60 秒
3. **啟動應用程式**: 10-20 秒

**總計**: 約 1-2 分鐘

## 🎮 遊戲預期

- **總題目數**: 9 題（每個分類 3 張測試照片）
- **每題時間**: 自由選擇，無時間限制
- **分數計算**: 您和 AI 各自獨立計分
- **獲勝條件**: 得分高者獲勝

## 🔍 品質預期

基於當前資料配置：
- **訓練資料**: 每個分類 8 張照片（優良）
- **測試資料**: 每個分類 3 張照片（適中）
- **預期準確度**: 70-90%（取決於照片品質）

## ⚠️ 注意事項

### 首次執行
1. 需要網路連線下載模型
2. 安裝過程不要中斷
3. 模型下載後會快取，之後不需再下載

### 執行環境
1. 建議使用虛擬環境（避免套件衝突）
2. 確保 Python 版本 >= 3.8
3. macOS 系統可能需要安裝 Xcode Command Line Tools

### 照片品質
1. 確保人臉清晰可見
2. 光線充足
3. 避免過度模糊或遮擋

## 🐛 常見問題

### Q1: 執行 `./run.sh` 時顯示權限錯誤
```bash
chmod +x run.sh install.sh
```

### Q2: 找不到 Python3
```bash
# 檢查 Python 版本
python3 --version

# 如果沒有安裝，請從官網下載：
# https://www.python.org/downloads/
```

### Q3: 安裝相依套件時出錯
```bash
# 升級 pip
pip install --upgrade pip

# 重新安裝
pip install -r requirements.txt
```

### Q4: 模型下載失敗
- 檢查網路連線
- 如果使用代理，請設定環境變數
- 可以稍後重試

## 📊 成功指標

啟動成功後，您應該會看到：

1. ✅ Streamlit 應用程式在瀏覽器中開啟
2. ✅ 顯示「開始初始化」按鈕
3. ✅ 點擊後顯示「初始化成功！找到 9 張測試照片」
4. ✅ 可以開始遊戲

## 🎉 準備就緒！

所有檢查項目都已完成，現在可以執行：

```bash
cd "/Users/benlu/Desktop/Applications/周杰倫種族分類PK"
./run.sh
```

或查看詳細說明：
- [QUICKSTART.md](QUICKSTART.md) - 快速開始指南
- [DATA_INFO.md](DATA_INFO.md) - 資料資訊
- [USAGE.md](USAGE.md) - 詳細使用說明

祝您遊戲愉快！🎤✨
