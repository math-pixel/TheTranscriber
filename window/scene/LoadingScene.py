from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from DLog import *
from transcription.TranscriptionController import *
import threading


# This is the loading scene called after the MainScene, this will need some improvements
class LoadingScene(QWidget, TranscriptionObserver):
    def __init__(self):
        super().__init__()
        # Create a QLabel widget
        label = QLabel("Loading scene")
        # Create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(label)
        # Set the layout for the widget
        self.setLayout(layout)

    # Here it is the function update that came from the TranscriptionObserver
    def update(self, state):
        if state == TranscriptionState.IDLE:
            # Switch the idle text
            pass
        elif state == TranscriptionState.DOWNLOADINGVIDEO:
            # Switch the download video text
            pass
        elif state == TranscriptionState.CONVERTINGVIDEO:
            # Switch the converting text
            pass
        elif state == TranscriptionState.LOADINGMODEL:
            # Switch the loading model text
            pass
        elif state == TranscriptionState.TRANSCRIBING:
            # Switch the transcribing text
            pass
        DLog.errorbiglog(str(state) + "=========== IN THE LOADING SCENE")
        



