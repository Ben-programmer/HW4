"""
周杰倫種族分類 PK 大賽
使用 Streamlit 建立互動式人臉辨識遊戲
"""

import streamlit as st
import random
import os
from PIL import Image
from face_recognition import FaceRecognizer


# 分類顯示名稱對應（可根據需求修改）
CATEGORIES_DISPLAY = {
    'cookieslu': '粥餅倫',
    'helu': '黑倫',
    'jay': '周杰倫',
}


def initialize_session_state():
    """初始化 session state"""
    if 'recognizer' not in st.session_state:
        st.session_state.recognizer = None
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'test_images' not in st.session_state:
        st.session_state.test_images = []
    if 'current_image' not in st.session_state:
        st.session_state.current_image = None
    if 'current_answer' not in st.session_state:
        st.session_state.current_answer = None
    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
    if 'ai_score' not in st.session_state:
        st.session_state.ai_score = 0
    if 'round_count' not in st.session_state:
        st.session_state.round_count = 0
    if 'ai_prediction' not in st.session_state:
        st.session_state.ai_prediction = None
    if 'ai_confidence' not in st.session_state:
        st.session_state.ai_confidence = 0.0
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False


def initialize_recognizer():
    """初始化人臉辨識器"""
    if st.session_state.recognizer is None:
        with st.spinner('🚀 正在載入 AI 模型...'):
            recognizer = FaceRecognizer()
            recognizer.initialize_model()
            
        with st.spinner('📸 正在建立人臉特徵資料庫...'):
            success_count = recognizer.build_face_database()
            
        if success_count == 0:
            st.error("❌ 無法建立人臉特徵資料庫，請確認 photos/ 資料夾中有訓練照片！")
            return False
            
        st.session_state.recognizer = recognizer
        st.session_state.test_images = recognizer.get_test_images()
        
        if not st.session_state.test_images:
            st.warning("⚠️ test_photos/ 資料夾中沒有測試照片，請先準備測試資料！")
            return False
            
        random.shuffle(st.session_state.test_images)
        st.session_state.initialized = True
        st.success(f"✅ 初始化成功！找到 {len(st.session_state.test_images)} 張測試照片")
        return True
    return True


def get_display_name(category: str) -> str:
    """獲取分類的顯示名稱"""
    return CATEGORIES_DISPLAY.get(category, category)


def next_round():
    """開始下一回合"""
    if not st.session_state.test_images:
        st.info("🎊 所有照片都已完成！最終結果：")
        st.write(f"**👤 您的分數**: {st.session_state.user_score}")
        st.write(f"**🤖 AI 分數**: {st.session_state.ai_score}")
        
        if st.session_state.user_score > st.session_state.ai_score:
            st.balloons()
            st.success("🎉 恭喜您獲勝！您比 AI 更會認人！")
        elif st.session_state.user_score < st.session_state.ai_score:
            st.error("😅 AI 獲勝！再接再厲！")
        else:
            st.info("🤝 平手！勢均力敵！")
        return
        
    # 取出下一張照片
    current_img = st.session_state.test_images.pop(0)
    st.session_state.current_image = current_img
    st.session_state.current_answer = current_img['category']
    
    # AI 進行預測
    ai_pred, ai_conf = st.session_state.recognizer.recognize_face(current_img['path'])
    st.session_state.ai_prediction = ai_pred
    st.session_state.ai_confidence = ai_conf
    
    st.session_state.round_count += 1
    st.session_state.game_started = True
    st.session_state.show_result = False


def check_answer(user_choice: str):
    """檢查答案並更新分數"""
    correct_answer = st.session_state.current_answer
    ai_prediction = st.session_state.ai_prediction
    
    # 更新分數
    if user_choice == correct_answer:
        st.session_state.user_score += 1
        
    if ai_prediction == correct_answer:
        st.session_state.ai_score += 1
        
    st.session_state.show_result = True


def reset_game():
    """重置遊戲"""
    st.session_state.user_score = 0
    st.session_state.ai_score = 0
    st.session_state.round_count = 0
    st.session_state.current_image = None
    st.session_state.current_answer = None
    st.session_state.ai_prediction = None
    st.session_state.game_started = False
    st.session_state.show_result = False
    
    if st.session_state.recognizer:
        st.session_state.test_images = st.session_state.recognizer.get_test_images()
        random.shuffle(st.session_state.test_images)


def main():
    """主程式"""
    st.set_page_config(
        page_title="周杰倫種族分類 PK 大賽",
        page_icon="🎤",
        layout="wide"
    )
    
    # 初始化
    initialize_session_state()
    
    # 標題
    st.markdown("""
    <div style="text-align: center;">
        <h1>🎤 周杰倫種族分類 PK 大賽 🎤</h1>
        <p>和 AI 一起來辨識吧！看看誰比較厲害？</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 檢查是否已初始化
    if not st.session_state.initialized:
        st.info("👋 歡迎！請先初始化系統...")
        
        if st.button("🚀 開始初始化", type="primary", use_container_width=True):
            if initialize_recognizer():
                st.rerun()
        
        st.markdown("---")
        st.markdown("### 📋 使用說明")
        st.markdown("""
        1. 請確保已在 `photos/` 資料夾中準備訓練照片
        2. 請確保已在 `test_photos/` 資料夾中準備測試照片
        3. 點擊「開始初始化」按鈕
        4. 等待 AI 模型載入和特徵資料庫建立
        5. 開始遊戲！
        """)
        return
    
    # 顯示分數
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.metric("🎮 回合", st.session_state.round_count)
    with col2:
        st.metric("👤 您的分數", st.session_state.user_score)
    with col3:
        st.metric("🤖 AI 分數", st.session_state.ai_score)
    
    st.markdown("---")
    
    # 遊戲主區域
    if not st.session_state.game_started:
        st.info("👇 點擊下方按鈕開始遊戲！")
        if st.button("🎮 開始遊戲 / 下一題", type="primary", use_container_width=True):
            next_round()
            st.rerun()
    else:
        # 顯示當前圖片
        col_img, col_control = st.columns([2, 1])
        
        with col_img:
            st.subheader("🖼️ 猜猜這是誰？")
            if st.session_state.current_image:
                image = Image.open(st.session_state.current_image['path'])
                st.image(image, use_container_width=True)
        
        with col_control:
            st.subheader("👤 選擇你的答案")
            
            # 獲取所有分類選項
            categories = st.session_state.recognizer.category_names
            display_options = [get_display_name(cat) for cat in categories]
            
            user_choice_display = st.radio(
                "請選擇：",
                options=display_options,
                key="user_choice_radio"
            )
            
            # 轉換回原始分類名稱
            user_choice = categories[display_options.index(user_choice_display)]
            
            st.markdown("---")
            
            if not st.session_state.show_result:
                if st.button("✅ 提交答案", type="primary", use_container_width=True):
                    check_answer(user_choice)
                    st.rerun()
            else:
                # 顯示結果
                st.success("📊 本回合結果")
                
                correct_answer = st.session_state.current_answer
                ai_prediction = st.session_state.ai_prediction
                
                st.write(f"**正確答案**: {get_display_name(correct_answer)}")
                st.write(f"**您的答案**: {get_display_name(user_choice)}")
                st.write(f"**AI 預測**: {get_display_name(ai_prediction) if ai_prediction else '無法辨識'}")
                st.write(f"**AI 信心度**: {st.session_state.ai_confidence:.2%}")
                
                st.markdown("---")
                
                # 判斷結果
                user_correct = user_choice == correct_answer
                ai_correct = ai_prediction == correct_answer
                
                if user_correct and ai_correct:
                    st.info("🤝 你們都答對了！")
                elif user_correct:
                    st.success("🎉 只有你答對了！")
                elif ai_correct:
                    st.warning("🤖 只有 AI 答對了！")
                else:
                    st.error("😅 你們都答錯了！")
                
                st.markdown("---")
                
                # 下一題按鈕
                if st.button("➡️ 下一題", type="primary", use_container_width=True):
                    next_round()
                    st.rerun()
    
    # 側邊欄
    with st.sidebar:
        st.header("⚙️ 遊戲控制")
        
        if st.button("🔄 重新開始", use_container_width=True):
            reset_game()
            st.rerun()
            
        st.markdown("---")
        
        st.header("📊 遊戲資訊")
        if st.session_state.recognizer:
            st.write(f"**分類數量**: {len(st.session_state.recognizer.category_names)}")
            st.write(f"**剩餘題數**: {len(st.session_state.test_images)}")
            
            with st.expander("📝 分類列表"):
                for cat in st.session_state.recognizer.category_names:
                    st.write(f"- {get_display_name(cat)}")
        
        st.markdown("---")
        
        st.header("ℹ️ 關於")
        st.markdown("""
        本專案參考自蔡炎龍老師的 
        [AI-Demo](https://github.com/yenlung/AI-Demo) 專案
        
        使用技術：
        - InsightFace
        - Streamlit
        - OpenCV
        """)


if __name__ == "__main__":
    main()
