# 📊 專案資料說明

## 當前分類資訊

本專案包含以下三個分類：

### 1. Cookies 呂 (cookieslu)
- **訓練照片**: 8 張
- **測試照片**: 3 張
- **資料夾**: `photos/cookieslu/` 和 `test_photos/cookieslu/`

### 2. 何呂 (helu)
- **訓練照片**: 8 張
- **測試照片**: 3 張
- **資料夾**: `photos/helu/` 和 `test_photos/helu/`

### 3. 周杰倫 (jay)
- **訓練照片**: 8 張
- **測試照片**: 3 張
- **資料夾**: `photos/jay/` 和 `test_photos/jay/`

## 資料夾結構

```
photos/                          # 訓練照片資料夾
├── cookieslu/
│   ├── cookieslu01.jpg
│   ├── cookieslu02.jpg
│   ├── cookieslu03.jpg
│   ├── cookieslu04.jpg
│   ├── cookieslu05.jpg
│   ├── cookieslu06.jpg
│   ├── cookieslu07.jpg
│   └── cookieslu08.jpg
├── helu/
│   ├── helu01.jpg
│   ├── helu02.jpg
│   ├── helu03.jpg
│   ├── helu04.jpg
│   ├── helu05.jpg
│   ├── helu06.jpg
│   ├── helu07.jpg
│   └── helu08.jpg
└── jay/
    ├── jay01.jpg
    ├── jay02.jpg
    ├── jay03.jpg
    ├── jay04.jpg
    ├── jay05.jpg
    ├── jay06.jpg
    ├── jay07.jpg
    └── jay08.jpg

test_photos/                     # 測試照片資料夾
├── cookieslu/
│   ├── test01.jpg
│   ├── test02.jpg
│   └── test03.jpg
├── helu/
│   ├── test01.jpg
│   ├── test02.jpg
│   └── test03.jpg
└── jay/
    ├── test01.jpg
    ├── test02.jpg
    └── test03.jpg
```

## 資料統計

- **總分類數**: 3 個
- **總訓練照片**: 24 張 (每個分類 8 張)
- **總測試照片**: 9 張 (每個分類 3 張)
- **照片格式**: JPG
- **照片大小**: 6 KB - 617 KB

## 使用建議

### 1. 照片品質
✅ 所有照片都包含人臉
✅ 照片解析度足夠
✅ 每個分類有足夠的訓練樣本

### 2. 資料平衡
✅ 三個分類的訓練照片數量相同（各 8 張）
✅ 三個分類的測試照片數量相同（各 3 張）
✅ 資料分布均衡

### 3. 預期效果
- **訓練速度**: 快速（24 張照片）
- **辨識準確度**: 預期良好（每個分類有 8 張訓練照片）
- **遊戲題目數**: 9 題

## 新增或修改分類

### 新增分類

1. 在 `photos/` 中建立新資料夾：
   ```bash
   mkdir -p photos/new_person
   ```

2. 放入 5-10 張訓練照片

3. 在 `test_photos/` 中建立相同名稱的資料夾：
   ```bash
   mkdir -p test_photos/new_person
   ```

4. 放入 3-5 張測試照片

5. 更新 `app.py` 中的 `CATEGORIES_DISPLAY`：
   ```python
   CATEGORIES_DISPLAY = {
       'cookieslu': 'Cookies 呂',
       'helu': '何呂',
       'jay': '周杰倫',
       'new_person': '新人物名稱',  # 新增這一行
   }
   ```

### 修改現有分類

只需要替換對應資料夾中的照片即可，系統會自動重新學習。

## 測試辨識效果

在啟動遊戲前，可以先測試辨識準確度：

```bash
python face_recognition.py
```

這會顯示：
- 每張測試照片的辨識結果
- 整體準確率統計
- 信心度分數

## 效能優化建議

目前的設定已經很好：
- ✅ 照片數量適中（不會太慢）
- ✅ 每個分類資料充足（準確度應該不錯）
- ✅ 測試照片數量適當（遊戲不會太短或太長）

## 備註

- 照片檔案包含 `.DS_Store` 檔案（macOS 系統檔案），程式會自動忽略
- 建議定期備份照片資料
- 如需更高準確度，可以增加每個分類的訓練照片至 10-15 張

---

**準備好開始遊戲了！** 🎮
執行 `./run.sh` 或 `streamlit run app.py` 啟動應用程式。
