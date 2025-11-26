#!/bin/bash

# 周杰倫種族分類 PK 專案啟動腳本

echo "🎤 周杰倫種族分類 PK 大賽"
echo "========================="
echo ""

# 檢查 Python 環境
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 未找到 Python3"
    echo "請先安裝 Python 3.8 或更高版本"
    exit 1
fi

echo "✅ Python 版本:"
python3 --version
echo ""

# 檢查是否有虛擬環境
if [ ! -d "venv" ]; then
    echo "📦 建立虛擬環境..."
    python3 -m venv venv
    echo "✅ 虛擬環境建立完成"
    echo ""
fi

# 啟動虛擬環境
echo "🔧 啟動虛擬環境..."
source venv/bin/activate

# 檢查並安裝相依套件
if [ ! -f "venv/.installed" ]; then
    echo "📥 安裝相依套件..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        touch venv/.installed
        echo "✅ 相依套件安裝完成"
    else
        echo "❌ 安裝失敗，請檢查錯誤訊息"
        exit 1
    fi
    echo ""
fi

# 檢查照片資料夾
echo "📂 檢查資料夾..."

if [ ! -d "photos" ] || [ -z "$(ls -A photos 2>/dev/null | grep -v '^\.')" ]; then
    echo "⚠️  警告: photos/ 資料夾為空"
    echo "請在 photos/ 資料夾中準備訓練照片"
    echo ""
fi

if [ ! -d "test_photos" ] || [ -z "$(ls -A test_photos 2>/dev/null | grep -v '^\.')" ]; then
    echo "⚠️  警告: test_photos/ 資料夾為空"
    echo "請在 test_photos/ 資料夾中準備測試照片"
    echo ""
fi

# 啟動 Streamlit
echo "🚀 啟動應用程式..."
echo "瀏覽器將自動開啟 http://localhost:8501"
echo "按 Ctrl+C 停止程式"
echo ""

streamlit run app.py
