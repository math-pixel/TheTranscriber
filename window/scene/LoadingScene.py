from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar, QSizePolicy
from PyQt5.QtCore import Qt
from transcription.TranscriptionController import TranscriptionState
 

# This is the loading scene called after the MainScene, this will need some improvements
class LoadingScene(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a QLabel widget
        label = QLabel("Loading...")
        
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setAlignment(Qt.AlignCenter)
        
        
        self.labelState = QLabel("")
        
        self.labelState.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.labelState.setAlignment(Qt.AlignCenter)
        
        
        self.progress = QProgressBar(self)
        self.completed = 0
        self.stateCount = len(TranscriptionState)
        
        
        # Create a layout and add the label to it
        layout = QVBoxLayout()
        
        layout.addWidget(label)
        layout.addWidget(self.labelState)
        layout.addWidget(self.progress)
        
        # Set the layout for the widget
        self.setLayout(layout)
        
        
        self.showIdleState()
        self.showDownloadState()


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
    
