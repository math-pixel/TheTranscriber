import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QStackedWidget
from window.scene.MainScene import MainScene
from window.scene.VideoTranscribedScene import VideoTranscribedScene

# To be clearer, i consider in this object, every QWidget who looks like a scene are a scene
# Here, we do a system like UnityScene for example, every scene have a lifecycle but cannot be instanciated
# with different params
class SceneManager(QMainWindow):
    instance = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Transcriber")
        self.setGeometry(100, 100, 1280, 720)

        # Here, we instantiate the stackedwidget where we will place every new scene created 
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Setup every scene
        self.scenes = {
            # https://www.youtube.com/watch?v=z9w6tO4d90U
            "mainScene": MainScene(), 
            "videoTranscribedScene": VideoTranscribedScene(),
        }

        for scene in self.scenes.values():
            self.stacked_widget.addWidget(scene)

    def goToScene(self, sceneName: str):
        self.stacked_widget.currentWidget().endScene()
        self.stacked_widget.setCurrentWidget(self.scenes[sceneName])
        self.stacked_widget.currentWidget().startScene()

    @staticmethod
    def getInstance():
        if SceneManager.instance == None:
            SceneManager.instance = SceneManager()
        return SceneManager.instance


