import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QStackedWidget
from window.scene.MainScene import MainScene
from window.scene.VideoTranscribedScene import VideoTranscribedScene


# Here, the "SceneManager", is just the QMainWindow, but with capabilities to manage scenes, the name
# isn't good imo, i don't have other idea for now
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
        
        self.stacked_widget.addWidget(MainScene())

    def newScene(self, scene):
        self.removeScene()
        self.stacked_widget.addWidget(scene)
        self.stacked_widget.setCurrentWidget(scene)

    def removeScene(self):
        # Remove other scenes from memory but keep 1 scene in the stacked widget, in that manner, we can
        # keep the thread from the widget before the first one !
        if self.stacked_widget.count() > 1:
            removed_widget = self.stacked_widget.currentWidget()
            self.stacked_widget.removeWidget(removed_widget)
            removed_widget.deleteLater()

    @staticmethod
    def getInstance():
        if SceneManager.instance == None:
            SceneManager.instance = SceneManager()
        return SceneManager.instance


