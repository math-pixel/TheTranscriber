from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from transcription.TranscriptionController import *
from window.scene.VideoTranscribedScene import *
from window.scene.LoadingScene import *
import threading

class TranscribeVideoThread(QThread):
    # Here, we signal that the pyqtSignal take 1 arg and it is a list
    finished_signal = pyqtSignal(list)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        result = TranscriptionController.getInstance().startTranscription(self.url);
        self.finished_signal.emit(result["segments"])

class DragAndDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        
        self.textColor = "#fff"
        self.url = ""
    
        self.vLayout = QVBoxLayout()
        self.vLayout.setAlignment(Qt.AlignCenter)

        self.divWidget = QWidget(self)
        self.divWidget.setContentsMargins(50, 50, 50, 50)
        self.divWidget.setStyleSheet(f"background-color: #A8DD9B; border-radius: 20px; font-size:20px; color: {self.textColor};")

        # ---------------------------------------------------------------------------- #
        #                                  Adding text                                 #
        # ---------------------------------------------------------------------------- #
        self.label1 = QLabel("Drag & Drop")
        self.label2 = QLabel("OU")


        # ---------------------------------------------------------------------------- #
        #                                Input Url + Btn                               #
        # ---------------------------------------------------------------------------- #
        self.inputHLayout = QHBoxLayout()
        self.inputHLayout.setAlignment(Qt.AlignCenter)

        self.inputText = QLineEdit()
        self.inputText.setPlaceholderText("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        self.button = QPushButton("GO")
        self.button.clicked.connect(lambda: self.launchTranscription(self.inputText.text()))
        self.button.setStyleSheet(f"background-color: #FFA1A1; border-radius: 20px; padding: 10px 20px; color: {self.textColor};")
        
        self.inputHLayout.addWidget(self.inputText)
        self.inputHLayout.addWidget(self.button)


        # ---------------------------------------------------------------------------- #
        #                                 Create layout                                #
        # ---------------------------------------------------------------------------- #
        self.divLayout = QVBoxLayout(self.divWidget)
        self.divLayout.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.divLayout.addWidget(self.label2, alignment=Qt.AlignCenter)
        self.divLayout.addLayout(self.inputHLayout)

        self.vLayout.addWidget(self.divWidget)
        self.setLayout(self.vLayout)



    # ---------------------------------------------------------------------------- #
    #                               Drag and Drop events                           #
    # ---------------------------------------------------------------------------- #
    def dragEnterEvent(self, event: QDragEnterEvent):
        mime_data = event.mimeData()

        if mime_data.hasUrls() and len(mime_data.urls()) == 1:
            # Vérifiez si l'URL est un fichier vidéo (vous pouvez ajouter plus de vérifications)
            url = mime_data.urls()[0]
            if url.isLocalFile() and url.toString().endswith(('.mp4', '.avi', '.mkv')):
                event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        url = event.mimeData().urls()[0]
        file_path = url.toLocalFile()

        self.url = file_path
        self.nextPage()
        # Ajoutez ici le code pour traiter le fichier vidéo (par exemple, jouer la vidéo)
        print(f"Fichier vidéo ajouté : {file_path}")


    # ---------------------------------------------------------------------------- #
    #                                     Event                                    #
    # ---------------------------------------------------------------------------- #
    # This is the function called when we click on the button
    def launchTranscription(self, url):
        self.transcribe_thread = TranscribeVideoThread(url)
        # Connect the callback to the finished signal !
        self.transcribe_thread.finished_signal.connect(self.nextPage)
        self.transcribe_thread.start()

        # To avoid circular import here lol
        from window.SceneManager import SceneManager
        SceneManager.getInstance().newScene(LoadingScene())
        

    def nextPage(self, result: list):
        # Cause of circular import, i can't import SceneManager at the module level (and it's normal lol)
        # So i do this x)
        from window.SceneManager import SceneManager
        SceneManager.getInstance().newScene(VideoTranscribedScene(result, Utils.getDirectoryAbsolutePath() + "/export/video.mp4"))
        