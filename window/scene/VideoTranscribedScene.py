import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSlider, \
    QSizePolicy, QStyle, QListWidget, QListWidgetItem, QScrollArea, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
from window.scene.videoTranscribedScene.ParentWidget import ParentWidget

# The Video Transcribed Scene
class VideoTranscribedScene(QWidget):
    # TODO : retire this stupid None
    def __init__(self, result, video_path):
        super().__init__()
        self.result = result
        self.video_path = video_path

        # Créer et afficher le widget parent
        self.parentWidget = ParentWidget(self.result, self.video_path)
        self.button = QPushButton("RETURN MAIN MENU")
        self.button.clicked.connect(self.goToMainScene)
        self.button.setStyleSheet(f"background-color: #FFA1A1; border-radius: 20px; padding: 10px 20px;")
        

        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.parentWidget)
        layout.addWidget(self.button)
        self.setLayout(layout)


    def goToMainScene(self):
        print("go to main scene")
        from window.SceneManager import SceneManager
        from window.scene.MainScene import MainScene
        SceneManager.getInstance().newScene(MainScene())
        pass
