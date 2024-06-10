import cv2
import sys
from window import ImageWindow
from PyQt6.QtWidgets import QApplication, QFileDialog

save_process_path = 'stuff/saved/save_proc.jpg'

class Mywindow(ImageWindow):
    def __init__(self):
        super().__init__()
        self.initial_path = ''
        self.video_source = None
        self.capture = None
        self.frame = None
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2(history=1000, varThreshold=32, detectShadows=True)
        self.cap = None
    
    def on_button_video_clicked(self):
        self.download_video(1)
        self.video_process1()
    
    def on_button_web_clicked(self):
        self.cap = cv2.VideoCapture(0)
        self.video_process1()
    
    def download_video(self, i):
        try:
            self.initial_path, _ = QFileDialog.getOpenFileName(self, "Выберите видео", "", "Видео (*.mp4)")
            if not self.initial_path:
                raise FileNotFoundError("Путь к видео не был выбран.")
            if i == 1:
                self.cap = cv2.VideoCapture(self.initial_path)
                _, img = self.cap.read()
                cv2.imwrite(save_process_path, img)
                self.update_images1(save_process_path)
            else:
                raise FileNotFoundError("Куда ты хочешь картинку?")
        except Exception as e:
            print("Ошибка при загрузке видео", e)
            return None

    def video_process1(self):
        # Создание объекта для вычитания фона

        while True:
            ret, frame = self.cap.read()
            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            cv2.imwrite(save_process_path, frame)
            self.update_images1(save_process_path)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fg_mask = self.background_subtractor.apply(gray_frame)
            fg_mask = cv2.threshold(fg_mask, 240, 255, cv2.THRESH_BINARY)[1]
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 300:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            original_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite(save_process_path, frame)
            self.update_images2(save_process_path)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    sys.exit(app.exec())
