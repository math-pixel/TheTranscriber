from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from DLog import *
from transcription.TranscriptionController import *
from transcription.TranscriptionController import TranscriptionState
import threading

# This is the loading scene called after the MainScene, this will need some improvements
class LoadingScene(QWidget, TranscriptionObserver):
    def __init__(self):
        super().__init__()

        
        self.labelState = QLabel("Loading...")
        
        self.labelState.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.labelState.setAlignment(Qt.AlignCenter)
        
        
        self.progress = QProgressBar(self)
        self.completed = 0
        self.stateCount = len(TranscriptionState)
        
        
        layout = QVBoxLayout()
        
        layout.setContentsMargins(200, 200, 200, 200)

        layout.minimumHeightForWidth(300)
        
        layout.addWidget(self.labelState)
        layout.addWidget(self.progress)
        
        
        self.setLayout(layout)
        
        self.showIdleState()
        self.showDownloadState()

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


    def showIdleState(self):
        self.completed += 1
        value = self.completed / self.stateCount * 100
        self.progress.setValue(value)
        
        self.labelState.setText("Idle...")
    
    
    def showDownloadState(self):
        self.completed += 1
        value = self.completed / self.stateCount * 100
        self.progress.setValue(value)
        
        self.labelState.setText("Downloading media...")
    
    
    def showConvertState(self):
        self.completed += 1
        value = self.completed / self.stateCount * 100
        self.progress.setValue(value)
        
        self.labelState.setText("Converting...")
    
    
    def showLoadModelState(self):
        self.completed += 1
        value = self.completed / self.stateCount * 100
        self.progress.setValue(value)
        
        self.labelState.setText("Loading model...")
    
    
    def showTranscribeState(self):
        self.completed += 1
        value = self.completed / self.stateCount * 100
        self.progress.setValue(value)
        
        self.labelState.setText("Transcribing...")
    
