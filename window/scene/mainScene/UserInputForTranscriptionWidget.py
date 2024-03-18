from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from Utils import Utils
from transcription.TranscriptionObserver import *
from window.scene.VideoTranscribedScene import *
from window.scene.LoadingScene import *


# This thread will also observe the transcription to signal to the UserInputForTranscriptionWidget that
# the state changed
class TranscribeVideoThread(QThread, TranscriptionObserver):
    # Here, we signal that the pyqtSignal take 1 arg and it is a list
    finished_signal = pyqtSignal(list)
    update_state_signal = pyqtSignal(TranscriptionState)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        trController = TranscriptionController.getInstance()
        trController.addSubscriber(self)
        result = trController.startTranscription(self.url);
        trController.removeSubscriber(self)
        self.finished_signal.emit(result["segments"])

    def update(self, state):
        self.update_state_signal.emit(state)

class UserInputForTranscriptionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        
        self.textColor = "#fff"
        self.url = ""
    
        self.vLayout = QVBoxLayout()
        self.vLayout.setAlignment(Qt.AlignCenter)

        self.divWidget = QWidget(self)
        self.divWidget.setContentsMargins(50, 50, 50, 50)
        self.divWidget.setStyleSheet(f"background-color: #76CA62; border-radius: 20px; font-size:20px; color: {self.textColor};")

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
        self.inputText.setStyleSheet(f"background-color: #A8DD9B; border-radius: 20px; padding: 10px 20px; color: {self.textColor};")

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

        self.loadingScene = None


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

        self.loadingScene = LoadingScene()
        self.transcribe_thread = TranscribeVideoThread(url)
        # Connect the callback to the finished signal !
        self.transcribe_thread.finished_signal.connect(self.nextPage)
        self.transcribe_thread.update_state_signal.connect(self.updateLoadingSceneState)
        # TODO : ADD A NEW UPDATE STATE SIGNAL AND CONNECT IT TO THE LOADING SCENE
        self.transcribe_thread.start()

        # To avoid circular import here lol
        from window.SceneManager import SceneManager
        SceneManager.getInstance().newScene(self.loadingScene)
        
    def updateLoadingSceneState(self, state):
        self.loadingScene.updateState(state)
        DLog.goodlog("STATE UPDATED IN THREAD")
        pass 

    def nextPage(self, result: list):
        # Cause of circular import, i can't import SceneManager at the module level (and it's normal lol)
        # So i do this x)
        from window.SceneManager import SceneManager
        SceneManager.getInstance().newScene(VideoTranscribedScene(result, Utils.getDirectoryAbsolutePath() + "/export/video.mp4"))
        
