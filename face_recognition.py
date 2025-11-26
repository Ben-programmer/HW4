"""
人臉辨識核心模組
使用 InsightFace 進行人臉特徵提取和辨識
"""

import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis
import glob
from typing import Dict, List, Tuple, Optional


class FaceRecognizer:
    """人臉辨識器類別"""
    
    def __init__(self, photo_dir: str = 'photos', test_dir: str = 'test_photos'):
        """
        初始化人臉辨識器
        
        Args:
            photo_dir: 訓練照片資料夾路徑
            test_dir: 測試照片資料夾路徑
        """
        self.photo_dir = photo_dir
        self.test_dir = test_dir
        self.app = None
        self.face_database = {}
        self.category_names = []
        
    def initialize_model(self):
        """載入 InsightFace 模型"""
        print("🚀 正在載入 InsightFace 模型...")
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'])
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        print("✅ 模型載入完成！")
        
    def extract_face_features(self, image_path: str) -> Optional[np.ndarray]:
        """
        從圖片中提取人臉特徵
        
        Args:
            image_path: 圖片路徑
            
        Returns:
            人臉特徵向量，如果未偵測到人臉則返回 None
        """
        img = cv2.imread(image_path)
        if img is None:
            return None
            
        faces = self.app.get(img)
        if len(faces) == 0:
            return None
            
        # 取第一張臉的特徵
        return faces[0].embedding
        
    def build_face_database(self) -> int:
        """
        建立人臉特徵資料庫
        
        Returns:
            成功建立特徵的分類數量
        """
        if self.app is None:
            self.initialize_model()
            
        print("📸 正在建立人臉特徵資料庫...")
        
        # 獲取所有分類資料夾
        categories = [d for d in os.listdir(self.photo_dir) 
                     if os.path.isdir(os.path.join(self.photo_dir, d)) 
                     and not d.startswith('.')]
        
        if not categories:
            print("⚠️  警告: photos/ 資料夾中沒有找到分類子資料夾")
            return 0
            
        success_count = 0
        
        for category in categories:
            photo_path = os.path.join(self.photo_dir, category)
            
            # 獲取該分類的所有照片
            image_files = glob.glob(os.path.join(photo_path, '*'))
            image_files = [f for f in image_files 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
            
            if len(image_files) == 0:
                print(f"⚠️  警告: {category} 的資料夾中沒有找到照片")
                continue
                
            category_features = []
            successful_images = 0
            
            for img_path in image_files:
                features = self.extract_face_features(img_path)
                if features is not None:
                    category_features.append(features)
                    successful_images += 1
                    
            if len(category_features) > 0:
                # 計算平均特徵向量
                avg_features = np.mean(category_features, axis=0)
                self.face_database[category] = avg_features
                self.category_names.append(category)
                print(f"✅ {category}: 成功處理 {successful_images}/{len(image_files)} 張照片")
                success_count += 1
            else:
                print(f"❌ {category}: 無法從照片中提取人臉特徵")
                
        print(f"\n🎉 人臉特徵資料庫建立完成！成功建立 {success_count} 個分類的特徵資料")
        return success_count
        
    def recognize_face(self, image_path: str, threshold: float = 0.6) -> Tuple[Optional[str], float]:
        """
        辨識人臉
        
        Args:
            image_path: 待辨識圖片路徑
            threshold: 相似度閾值 (0-1)，越高越嚴格
            
        Returns:
            (分類名稱, 信心度)，如果無法辨識則返回 (None, 0.0)
        """
        features = self.extract_face_features(image_path)
        if features is None:
            return None, 0.0
            
        best_match = None
        best_similarity = -1
        
        # 計算與資料庫中每個分類的相似度
        for category, db_features in self.face_database.items():
            # 使用餘弦相似度
            similarity = np.dot(features, db_features) / (
                np.linalg.norm(features) * np.linalg.norm(db_features)
            )
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = category
                
        # 檢查是否超過閾值
        if best_similarity < threshold:
            return None, float(best_similarity)
            
        return best_match, float(best_similarity)
        
    def get_test_images(self) -> List[Dict[str, str]]:
        """
        獲取所有測試圖片
        
        Returns:
            測試圖片資訊列表，每個元素包含 'path' 和 'category'
        """
        test_images = []
        
        for category in self.category_names:
            test_path = os.path.join(self.test_dir, category)
            
            if not os.path.exists(test_path):
                continue
                
            image_files = glob.glob(os.path.join(test_path, '*'))
            image_files = [f for f in image_files 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
            
            for img_path in image_files:
                test_images.append({
                    'path': img_path,
                    'category': category
                })
                
        return test_images
        
    def test_accuracy(self) -> Dict[str, any]:
        """
        測試辨識準確度
        
        Returns:
            測試結果統計
        """
        test_images = self.get_test_images()
        
        if not test_images:
            return {
                'total': 0,
                'correct': 0,
                'accuracy': 0.0,
                'details': []
            }
            
        correct = 0
        details = []
        
        print("🔍 正在測試辨識準確度...")
        print("=" * 80)
        
        for img_info in test_images:
            img_path = img_info['path']
            true_category = img_info['category']
            
            predicted_category, confidence = self.recognize_face(img_path)
            
            is_correct = predicted_category == true_category
            if is_correct:
                correct += 1
                
            result = {
                'image': os.path.basename(img_path),
                'true_category': true_category,
                'predicted_category': predicted_category or '無法辨識',
                'confidence': confidence,
                'is_correct': is_correct
            }
            details.append(result)
            
            status = "✅ 正確" if is_correct else "❌ 錯誤"
            print(f"📷 {result['image']}")
            print(f"   實際: {true_category}")
            print(f"   預測: {result['predicted_category']} (信心度: {confidence:.2f})")
            print(f"   結果: {status}")
            print("-" * 50)
            
        accuracy = correct / len(test_images) if test_images else 0.0
        
        print("\n" + "=" * 80)
        print(f"📊 測試結果:")
        print(f"   總測試數: {len(test_images)}")
        print(f"   正確數: {correct}")
        print(f"   準確率: {accuracy:.2%}")
        print("=" * 80)
        
        return {
            'total': len(test_images),
            'correct': correct,
            'accuracy': accuracy,
            'details': details
        }


if __name__ == "__main__":
    # 測試程式
    recognizer = FaceRecognizer()
    recognizer.initialize_model()
    recognizer.build_face_database()
    
    if recognizer.category_names:
        results = recognizer.test_accuracy()
        print(f"\n最終準確率: {results['accuracy']:.2%}")
    else:
        print("\n請先在 photos/ 資料夾中準備訓練照片！")
