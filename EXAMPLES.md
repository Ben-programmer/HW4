# 專案範例：周杰倫時期分類

## 建議的分類結構

### 方案一：按時期分類

```
photos/
  ├── jay_2000_2003/      # 早期（范特西、八度空間時期）
  │   ├── 01.jpg
  │   ├── 02.jpg
  │   └── 03.jpg
  ├── jay_2004_2007/      # 中期（七里香、十一月的蕭邦時期）
  │   └── ...
  ├── jay_2008_2012/      # 成熟期（我很忙、跨時代時期）
  │   └── ...
  └── jay_2013_now/       # 近期
      └── ...
```

### 方案二：按風格/造型分類

```
photos/
  ├── jay_casual/         # 日常便服
  ├── jay_formal/         # 正式場合
  ├── jay_stage/          # 舞台演出
  ├── jay_movie/          # 電影角色
  └── jay_mv/             # MV造型
```

### 方案三：按專輯時期分類

```
photos/
  ├── jay_fantasy/        # 范特西時期
  ├── jay_octave/         # 八度空間時期
  ├── jay_common_jasmin/  # 七里香時期
  ├── jay_november/       # 十一月的蕭邦時期
  └── ...
```

## 照片準備建議

### 訓練照片 (photos/)

每個分類建議準備 5-10 張照片，要求：

1. **清晰度**：人臉清晰可見
2. **多角度**：正面、側面、微側面
3. **光線**：不同光線條件
4. **表情**：不同表情
5. **背景**：盡量簡單或多樣化

### 測試照片 (test_photos/)

每個分類建議準備 3-5 張照片，要求：

1. 與訓練照片不同
2. 具有代表性
3. 清晰可辨識

## 照片來源建議

### 合法來源

1. **官方網站**：華納音樂、杰威爾音樂官網
2. **官方社群**：官方 Instagram、Facebook
3. **新聞媒體**：公開報導照片（注意版權）
4. **演唱會錄影**：截圖使用

### 注意事項

⚠️ **重要提示**：
- 本專案僅供教育學習使用
- 請尊重著作權和肖像權
- 不要用於商業用途
- 建議使用公開可取得的照片

## 照片處理技巧

### 1. 裁切與調整

```bash
# 建議使用圖片編輯工具：
- macOS: 預覽程式
- Windows: 相片應用程式
- 跨平台: GIMP (免費)
```

### 2. 統一格式

建議將所有照片統一為：
- 格式：JPG
- 解析度：不小於 640x640
- 檔案大小：500KB - 2MB

### 3. 命名規則

```
photos/
  └── jay_young/
      ├── jay_young_01.jpg
      ├── jay_young_02.jpg
      └── jay_young_03.jpg
```

## 實際操作步驟

### 1. 建立資料夾

```bash
cd /Users/benlu/Desktop/Applications/周杰倫種族分類PK

# 建立訓練照片資料夾
mkdir -p photos/jay_young
mkdir -p photos/jay_middle
mkdir -p photos/jay_recent

# 建立測試照片資料夾
mkdir -p test_photos/jay_young
mkdir -p test_photos/jay_middle
mkdir -p test_photos/jay_recent
```

### 2. 放入照片

將準備好的照片分別放入對應的資料夾。

### 3. 修改顯示名稱

編輯 `app.py`：

```python
CATEGORIES_DISPLAY = {
    'jay_young': '年輕時期 (2000-2005)',
    'jay_middle': '中期 (2006-2012)',
    'jay_recent': '近期 (2013-現在)',
}
```

### 4. 執行測試

```bash
# 先測試辨識準確度
python face_recognition.py

# 如果準確度滿意，啟動遊戲
./run.sh
# 或
streamlit run app.py
```

## 進階玩法

### 多人辨識

可以混合不同藝人：

```
photos/
  ├── jay/                # 周杰倫
  ├── jolin/              # 蔡依林
  ├── wang/               # 王力宏
  └── jj/                 # 林俊傑
```

### 角色辨識

電影角色分類：

```
photos/
  ├── jay_kungfu/         # 功夫灌籃
  ├── jay_secret/         # 不能說的秘密
  ├── jay_green/          # 青蜂俠
  └── jay_mermaid/        # 美人魚
```

## 效能優化建議

1. **照片數量**：每個分類 5-10 張訓練照片即可
2. **照片大小**：不要過大（建議 < 2MB）
3. **分類數量**：建議 3-6 個分類
4. **測試照片**：每個分類 3-5 張即可

祝您使用愉快！🎤
