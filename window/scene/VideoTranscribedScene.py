from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
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
