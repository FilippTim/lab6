from PyQt6.QtWidgets import QComboBox, QSlider, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Изображения")
        self.setGeometry(50, 50, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image_layout = QVBoxLayout()
        self.layout.addLayout(self.image_layout)

        self.image_label1 = QLabel()
        # self.label1_title = QLabel('До обработки')
        self.image_label2 = QLabel()
        # self.label2_title = QLabel('После обработки')

        #self.update_images1("stuff/images/white.jpg")
        #self.update_images2("stuff/images/white.jpg")

        # self.image_layout.addWidget(self.label1_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label1, alignment=Qt.AlignmentFlag.AlignCenter)
        # self.label1_title.hide()
        # self.image_layout.addWidget(self.label2_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)
        self.update_button()

        self.img_hide()
        self.show()

    def update_images1(self, image_path1):
        #self.label1_title.show()
        pixmap1 = QPixmap(image_path1)
        scaled_pixmap1 = pixmap1.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label1.setPixmap(scaled_pixmap1)
        self.image_label1.show()
        self.update()

    def img_hide(self):
        # self.label1_title.hide()
        self.image_label1.hide()
        # self.label2_title.hide()
        self.image_label2.hide()

    def update_images2(self, image_path2):
        # self.label2_title.show()
        pixmap2 = QPixmap(image_path2)
        scaled_pixmap2 = pixmap2.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label2.setPixmap(scaled_pixmap2)
        self.image_label2.show()
        self.update()


    def update_button(self):
        #Кнопка для загрузки видео
        self.button_video = QPushButton("Выбрать видео")
        self.button_video.clicked.connect(self.on_button_video_clicked)
        self.button_layout.addWidget(self.button_video)
        #Кнопка для вебки
        self.button_web = QPushButton("Использовать камеру")
        self.button_web.clicked.connect(self.on_button_web_clicked)
        self.button_layout.addWidget(self.button_web)
