# 使用說明文檔

## 📸 準備照片資料

### 1. 訓練照片 (photos/)

在 `photos/` 資料夾中為每個分類建立子資料夾：

```
photos/
  ├── category1/        # 分類1（例如：jay_young）
  │   ├── img1.jpg
  │   ├── img2.jpg
  │   ├── img3.jpg
  │   └── ...
  ├── category2/        # 分類2（例如：jay_middle）
  │   ├── img1.jpg
  │   └── ...
  └── category3/
      └── ...
```

**重要提示**：
- 每個分類建議至少準備 3-5 張照片
- 照片中應包含清晰的人臉
- 支援格式：JPG, JPEG, PNG, BMP
- 資料夾名稱會作為分類 ID（使用英文命名）

### 2. 測試照片 (test_photos/)

在 `test_photos/` 資料夾中建立與訓練照片相同的資料夾結構：

```
test_photos/
  ├── category1/
  │   ├── test1.jpg
  │   └── ...
  ├── category2/
  │   └── ...
  └── ...
```

**重要提示**：
- 測試照片用於 PK 遊戲
- 每個分類建議準備 3-10 張測試照片
- 測試照片應與訓練照片不同

## 🎨 自訂分類顯示名稱

編輯 `app.py` 中的 `CATEGORIES_DISPLAY` 字典：

```python
CATEGORIES_DISPLAY = {
    'jay_young': '年輕時期',
    'jay_middle': '中年時期',
    'jay_movie': '電影造型',
    # 新增更多分類
}
```

如果不設定，系統會直接使用資料夾名稱。

## 🚀 執行步驟

### 1. 安裝相依套件

```bash
pip install -r requirements.txt
```

### 2. 準備照片資料

按照上述說明準備訓練和測試照片。

### 3. 執行應用程式

```bash
streamlit run app.py
```

### 4. 開始遊戲

1. 在瀏覽器中開啟應用程式（通常是 http://localhost:8501）
2. 點擊「開始初始化」按鈕
3. 等待模型載入和特徵資料庫建立
4. 點擊「開始遊戲」開始 PK！

## ⚙️ 進階設定

### 調整辨識閾值

在 `face_recognition.py` 中修改 `recognize_face` 方法的 `threshold` 參數：

```python
def recognize_face(self, image_path: str, threshold: float = 0.6):
    # threshold 值越高，辨識越嚴格
    # 建議範圍：0.4 - 0.7
```

### 修改模型偵測尺寸

在 `face_recognition.py` 中修改：

```python
self.app.prepare(ctx_id=0, det_size=(640, 640))
# 增大尺寸可提高準確度但會變慢
# 減小尺寸可加快速度但準確度可能下降
```

## 🐛 常見問題

### Q: 初始化時顯示「無法建立人臉特徵資料庫」

A: 請檢查：
- `photos/` 資料夾是否存在
- 資料夾內是否有子資料夾
- 子資料夾內是否有圖片檔案
- 圖片中是否包含清晰的人臉

### Q: 辨識準確度不高

A: 可以嘗試：
- 增加每個分類的訓練照片數量
- 使用更清晰、角度更多樣的照片
- 調整辨識閾值
- 確保照片中人臉清晰可見

### Q: 程式執行很慢

A: 可以嘗試：
- 減少偵測尺寸（det_size）
- 減少訓練照片數量
- 使用較小的圖片檔案

### Q: 無法偵測到人臉

A: 請確保：
- 照片中人臉清晰可見
- 人臉大小適中（不要太小）
- 照片解析度足夠
- 照片未損壞

## 📊 測試模式

可以直接執行 `face_recognition.py` 來測試辨識準確度：

```bash
python face_recognition.py
```

這會自動測試所有測試照片並顯示準確率統計。

## 💡 專案範例

### 周杰倫不同時期分類

```
photos/
  ├── jay_young/          # 年輕時期（2000-2005）
  ├── jay_prime/          # 巔峰時期（2006-2010）
  ├── jay_mature/         # 成熟時期（2011-2015）
  └── jay_recent/         # 近期（2016-現在）
```

### 電影角色分類

```
photos/
  ├── jay_kungfu/         # 功夫片造型
  ├── jay_modern/         # 現代劇造型
  ├── jay_fantasy/        # 奇幻片造型
  └── jay_real/           # 本人日常
```

## 🎓 學習資源

- [InsightFace 官方文檔](https://github.com/deepinsight/insightface)
- [Streamlit 官方文檔](https://docs.streamlit.io/)
- [蔡炎龍老師的 AI-Demo](https://github.com/yenlung/AI-Demo)
