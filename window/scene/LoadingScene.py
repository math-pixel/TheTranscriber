from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
import threading


# This is the loading scene called after the MainScene, this will need some improvements
class LoadingScene(QWidget):
    def __init__(self):
        super().__init__()
        # Create a QLabel widget
        label = QLabel("Loading scene")
        # Create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(label)
        # Set the layout for the widget
        self.setLayout(layout)



