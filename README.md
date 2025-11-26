# 🎤 周杰倫種族分類 PK 大賽

基於蔡炎龍老師的 AI Demo 專案改編，使用 InsightFace 進行人臉辨識，與 AI 一起 PK 誰比較會認人！

## 📋 專案說明

這是一個互動式人臉辨識遊戲，您可以：
- 訓練 AI 辨識不同的人物（目前包含：Cookies 呂、何呂、周杰倫）
- 與 AI 進行 PK 比賽，看誰的辨識能力更強
- 使用 Streamlit 建立友善的網頁介面

## 🚀 快速開始

### 1. 安裝相依套件

```bash
pip install -r requirements.txt
```

### 2. 準備訓練資料

在 `photos/` 資料夾中建立子資料夾，每個子資料夾代表一個分類：

```
photos/
  ├── category1/
  │   ├── image1.jpg
  │   ├── image2.jpg
  │   └── ...
  ├── category2/
  │   ├── image1.jpg
  │   └── ...
  └── ...
```

### 3. 準備測試資料

在 `test_photos/` 資料夾中建立相同的子資料夾結構：

```
test_photos/
  ├── category1/
  │   ├── test1.jpg
  │   └── ...
  ├── category2/
  │   ├── test1.jpg
  │   └── ...
  └── ...
```

### 4. 執行應用程式

```bash
streamlit run app.py
```

應用程式將在瀏覽器中自動開啟（預設：http://localhost:8501）

## 📂 專案結構

```
周杰倫種族分類PK/
├── app.py                 # Streamlit 主程式
├── face_recognition.py    # 人臉辨識核心模組
├── requirements.txt       # Python 相依套件
├── README.md             # 專案說明文件
├── photos/               # 訓練照片資料夾
│   └── [分類名稱]/
├── test_photos/          # 測試照片資料夾
│   └── [分類名稱]/
└── .streamlit/           # Streamlit 設定
    └── config.toml
```

## 🎮 遊戲玩法

1. **初始化**：系統會自動載入訓練資料並建立人臉特徵資料庫
2. **開始遊戲**：點擊「下一題」按鈕開始新回合
3. **選擇答案**：查看照片後選擇您認為的答案
4. **查看結果**：系統會顯示正確答案以及您和 AI 的得分
5. **繼續挑戰**：持續進行直到測試照片用完

## 🛠️ 技術架構

- **人臉辨識**：InsightFace (buffalo_l 模型)
- **前端框架**：Streamlit
- **影像處理**：OpenCV, Pillow
- **深度學習**：ONNX Runtime
- **數據處理**：NumPy

## 📝 自訂專案

### 修改分類名稱

在 `app.py` 中修改 `CATEGORIES_DISPLAY` 變數：

```python
CATEGORIES_DISPLAY = {
    'cookieslu': 'Cookies 呂',
    'helu': '何呂',
    'jay': '周杰倫',
    # ... 新增更多分類
}
```

### 調整辨識閾值

在 `face_recognition.py` 中修改 `recognize_face` 函數的 `threshold` 參數：

```python
def recognize_face(image_path, threshold=0.6):  # 降低閾值讓辨識更寬鬆
    # ...
```

## 🙏 致謝

本專案參考自蔡炎龍老師的 [AI-Demo](https://github.com/yenlung/AI-Demo) 專案，特別是：
- [【Demo03v】和AI_PK看誰比較會認IVE成員](https://github.com/yenlung/AI-Demo/blob/master/%E3%80%90Demo03v%E3%80%91%E5%92%8CAI_PK%E7%9C%8B%E8%AA%B0%E6%AF%94%E8%BC%83%E6%9C%83%E8%AA%8DIVE%E6%88%90%E5%93%A1.ipynb)

感謝老師提供的優秀教學範例！

## 📄 授權

本專案僅供學習使用。
