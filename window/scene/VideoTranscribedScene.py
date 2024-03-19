from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer
from window.scene.videoTranscribedScene.ParentWidget import ParentWidget
from window.scene.Scene import *

# The Video Transcribed Scene
class VideoTranscribedScene(Scene):
    # TODO : retire this stupid None
    def __init__(self, result, video_path):
        super().__init__()
        self.result = result
        self.video_path = video_path

        # Créer et afficher le widget parent
        self.parentWidget = ParentWidget(self.result, self.video_path)
        self.button = QPushButton("RETURN MAIN MENU")
        self.button.clicked.connect(self.goToMainScene)
        self.button.setStyleSheet("background-color: #FFA1A1; border-radius: 10px; padding: 10px; color: #fff;")
        

        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.parentWidget)
        layout.addWidget(self.button)
        self.setLayout(layout)


    def goToMainScene(self):
        from window.SceneManager import SceneManager
        from window.scene.MainScene import MainScene
        SceneManager.getInstance().newScene(MainScene())

    def start(self):
        pass

    def end(self):
        if self.parentWidget.videoWidget.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.parentWidget.videoWidget.mediaPlayer.pause()
        pass