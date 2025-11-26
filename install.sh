#!/bin/bash

# 安裝相依套件腳本

echo "🎤 周杰倫種族分類 PK - 安裝相依套件"
echo "========================================"
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

# 詢問是否使用虛擬環境
read -p "是否建立虛擬環境？(建議使用) [Y/n]: " use_venv
use_venv=${use_venv:-Y}

if [[ $use_venv =~ ^[Yy]$ ]]; then
    if [ ! -d "venv" ]; then
        echo "📦 建立虛擬環境..."
        python3 -m venv venv
        echo "✅ 虛擬環境建立完成"
        echo ""
    fi
    
    echo "🔧 啟動虛擬環境..."
    source venv/bin/activate
    echo ""
fi

# 升級 pip
echo "⬆️  升級 pip..."
pip install --upgrade pip
echo ""

# 安裝相依套件
echo "📥 安裝相依套件..."
echo "這可能需要幾分鐘時間，請耐心等待..."
echo ""

pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 安裝完成！"
    echo ""
    echo "接下來您可以："
    echo "1. 測試辨識功能: python face_recognition.py"
    echo "2. 啟動應用程式: streamlit run app.py"
    echo "3. 或直接執行: ./run.sh"
    echo ""
    
    if [[ $use_venv =~ ^[Yy]$ ]]; then
        echo "💡 提示: 下次使用前請先啟動虛擬環境"
        echo "   source venv/bin/activate"
        echo ""
    fi
else
    echo ""
    echo "❌ 安裝失敗"
    echo "請檢查錯誤訊息並重試"
    exit 1
fi
