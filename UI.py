from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

from StatePage import *



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
        self.button.clicked.connect(lambda: self.buttonClicked(self.inputText.text()))
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
    def buttonClicked(self, url):
        self.url = url
        self.nextPage()
    
    
    def nextPage(self):
        print("page suivante")
        print(self.url)






# ---------------------------------------------------------------------------- #
#                                    Window                                    #
# ---------------------------------------------------------------------------- #
class UIDragAndDrop(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface")
        self.resize(1280, 556)
        self.center()

        self.dragDiv = DragAndDrop()
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.dragDiv) 

        self.setLayout(hLayout)

    
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    
    # ---------------------------------------------------------------------------- #
    #                                    States                                    #
    # ---------------------------------------------------------------------------- #
    
    
    # def showDragPage(self):
    #     self.current_state.showDragPage()
    
    # def showLoadingPage(self):
    #     self.current_state.showLoadingPage()

    # def showResultPage(self):
    #     self.current_state.showResultPage()

    
    
    # ---------------------------------------------------------------------------- #
    #                                 Update State                                 #
    # ---------------------------------------------------------------------------- #
    def updateState(self, new_state):
        print(f"Previous state: {self.current_state}")
        self.current_state = new_state
        print(f"New state: {new_state}")







class UI:
    def __init__(self) -> None:
        pass


