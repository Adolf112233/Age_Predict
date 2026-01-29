########## Environment #########
import os

from torch import layout 
imagePath = os.path.join("..", "image")
inPath  = os.path.join("..","input")
outPath = os.path.join("..","output")
dataPath = os.path.join("..","dataset")
modelPath = os.path.join("..", "model")
imagePath_MNIST = os.path.join("..", "image_MNIST")
codeFileName= os.path.splitext(os.path.basename(__file__))[0]

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QSize,Qt, pyqtSignal
from PIL import Image
import tensorflow as tf
#from PIL import Image
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QSizePolicy
)

class AgePredictionApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.model = None
        self.model_path = None
        self.initUI()

    
    def initUI(self):
        self.setFont(QFont('Arial', 20))
        self.setWindowTitle('Age Prediction App')
        self.setGeometry(100, 100, 520, 720)
        
        layout = QVBoxLayout()

        # Step 1: 顯示目前模型（先顯示未選）
        self.model_label = QLabel("Step 1: Select model (not selected)")
        layout.addWidget(self.model_label)

        self.btn_select_model = QPushButton("Select Model", self)
        self.btn_select_model.clicked.connect(self.select_model)
        # layout.addWidget(self.btn_select_model)
        
        #提示使用者選擇圖片
        self.label = QLabel('No image selected')
        layout.addWidget(self.label)
        
        #顯示選擇的圖片
        self.image_label = QLabel()
        layout.addWidget(self.image_label)
        
        #按鈕用來打開圖片
        self.btn_openimg = QPushButton('Open Image', self)
        self.btn_openimg.clicked.connect(self.open_image)
        self.btn_openimg.setEnabled(False)  # Disable button until model is selected
        # layout.addWidget(self.btn_openimg)

        #顯示預測結果
        self.result_label = QLabel('Prediction result will be shown here')
        # self.result_label.setFont(QFont('Arial', 14))  # Setting a larger font size
        layout.addWidget(self.result_label)

        # 1) 建一個水平按鈕列（底部）
        btn_row = QHBoxLayout()

        # 2) 先把「Select Model」按鈕加入左邊
        btn_row.addWidget(self.btn_select_model)

        # 3) 再把「Open Image」按鈕加入右邊（你的 self.btn）
        btn_row.addWidget(self.btn_openimg)

        # 4) 最後，把水平按鈕列加到主垂直 layout 的最底部
        layout.addStretch(1)   # 把多出來的垂直空間推到上方區域
        layout.addLayout(btn_row)
        
        #設定整體佈局
        self.setLayout(layout)
    
    def select_model(self):
        options = QFileDialog.Options()
        model_file, _ = QFileDialog.getOpenFileName( self, "Select Model File", "", "Keras Models (*.keras *.h5);;All Files (*)", options=options )
        if not model_file:
            return
        
         # 載入模型
        self.model_path = model_file

        #提示使用者正在載入模型
        self.result_label.setText("Model loading ...")
        self.repaint()                    # 或者 self.result_label.repaint()
        QApplication.processEvents()       # 強制先刷新一次 UI

        self.model = tf.keras.models.load_model(self.model_path)

        model_name = os.path.basename(self.model_path)
        self.model_label.setText(f"Step 1: Model selected: {model_name}")

        # Model ready → 開放選圖
        self.btn_openimg.setEnabled(True)
        self.label.setText("Step 2: Select image")

        # 清空上一次結果（可選）
        self.result_label.setText("Prediction result will be shown here")

    def open_image(self):

        # 保險：如果沒載入模型，直接提示（避免 self.model 為 None）
        if self.model is None:
            self.result_label.setText("Please select model first.")
            return
        
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.xpm *.jpg)', options=options)

        if file_name:
            self.label.setText(f"FileName: {file_name}")
            # self.label.setText(model_name)
            pixmap_original = QPixmap(file_name)
            display_size = QSize(1280, 720)  # QSize now correctly imported from QtCore
            pixmap_resized = pixmap_original.scaled(display_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap_resized)
            self.predict_age(file_name)

    def predict_age(self, image_path):
        # Load and preprocess image
        img = Image.open(image_path).resize((200, 200))
        img = np.asarray(img, dtype=np.float32)   # 關鍵：固定成 float32 ndarray

        # img = np.array(img) / 255.0 #如果模型沒有自動正規化，打開

        img = np.expand_dims(img, axis=0)
        
        # Predict age
        prediction = self.model.predict(img)
        predicted_age = prediction[0][0]
        
        # Show prediction result
        self.result_label.setText(f'Your Predicted Age:  {predicted_age:.2f} years old')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AgePredictionApp()
    ex.show()
    sys.exit(app.exec_())
