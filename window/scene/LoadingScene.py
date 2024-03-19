from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget, QSizePolicy, QProgressBar
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from DLog import *
from window.scene.Scene import *
from transcription.TranscriptionController import *
from transcription.TranscriptionController import TranscriptionState
import threading
import math

# This is the loading scene called after the MainScene, this will need some improvements
class LoadingScene(Scene):
    def __init__(self):
        super().__init__()

        
        self.labelState = QLabel("Loading...")
        self.labelState.setStyleSheet("color: white; font-size: 20px;")
        
        self.labelState.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.labelState.setAlignment(Qt.AlignCenter)
        
        
        self.progress = QProgressBar(self)
        self.progress.setStyleSheet("""
            .QProgressBar {
                background-color: #76CA62;
                border-radius: 15px;
                height: 30px;
                margin: 0 10px;
                text-align: center;
                color: white; 
                font-size: 20px;
            }

            .QProgressBar::chunk {
                background-color: #A8DD9B;
                border-radius: 15px;
            }
        """)
        
        self.completed = 0
        self.stateCount = len(TranscriptionState)
        
        
        self.layout = QVBoxLayout()
        
        self.layout.setContentsMargins(200, 200, 200, 200)

        self.layout.minimumHeightForWidth(300)
        
        self.layout.addWidget(self.labelState)
        self.layout.addWidget(self.progress)
        
        
        self.setLayout(self.layout)
        
        self.showIdleState()
        self.showDownloadState()

    # Here it is the function update that came from the TranscriptionObserver
    def updateState(self, state):
        if state == TranscriptionState.IDLE:
            self.showIdleState()
            pass
        elif state == TranscriptionState.DOWNLOADINGVIDEO:
            self.showDownloadState()
            pass
        elif state == TranscriptionState.CONVERTINGVIDEO:
            self.showConvertState()
            pass
        elif state == TranscriptionState.LOADINGMODEL:
            self.showLoadModelState()
            pass
        elif state == TranscriptionState.TRANSCRIBING:
            self.showTranscribeState()
            pass
        elif state == TranscriptionState.FAILED:
            self.showFailedState()
            pass
        else:
            raise Exception("State isn't implemented in the Loading Scene")

    def start(self):
        pass

    def end(self):
        pass


    def showFailedState(self):
        self.labelState.setText("FAILED...")
        button = QPushButton('Retourner à la page principale !', self)
        button.setGeometry(100, 100, 200, 50)
        button.clicked.connect(self.returnMainMenuScene)
        button.setStyleSheet("background-color: #FFA1A1; border-radius: 10px; padding: 10px; color: #fff;")
        self.layout.addWidget(button)

    def returnMainMenuScene(self):
        from window.SceneManager import SceneManager
        from window.scene.MainScene import MainScene
        SceneManager.getInstance().newScene(MainScene())

    def showIdleState(self):
        self.setProgressBarValue();
        self.labelState.setText("Idle...")
    
    
    def showDownloadState(self):
        self.setProgressBarValue();
        self.labelState.setText("Downloading media...")
    
    
    def showConvertState(self):
        self.setProgressBarValue();
        self.labelState.setText("Converting...")
    
    
    def showLoadModelState(self):
        self.setProgressBarValue();
        self.labelState.setText("Loading model...")
    
    
    def showTranscribeState(self):
        self.setProgressBarValue();
        self.labelState.setText("Transcribing...")
    
    def setProgressBarValue(self):
        self.completed += 1
        value = math.floor(self.completed / self.stateCount * 100)
        self.progress.setValue(value)

