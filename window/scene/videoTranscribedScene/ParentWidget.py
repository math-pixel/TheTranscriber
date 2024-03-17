import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSlider, \
    QSizePolicy, QStyle, QListWidget, QListWidgetItem, QScrollArea, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
from window.scene.videoTranscribedScene.VideoWidget import VideoWidget
from window.scene.videoTranscribedScene.ListWidget import ListWidget

class ParentWidget(QWidget):
    def __init__(self, result, video_path, parent=None):
        super().__init__(parent)
        self.result = result
        self.video_path = video_path

        # Créer des widgets
        self.videoWidget = VideoWidget()
        self.listWidget = ListWidget(self.result, self.videoWidget)

        # Charger la vidéo
        self.videoWidget.open_file(self.video_path)

        # Connecter les signaux et les slots
        self.listWidget.listWidget.itemClicked.connect(self.on_list_item_clicked)
        self.videoWidget.mediaPlayer.positionChanged.connect(self.on_video_position_changed)

        # Mise en page
        layout = QHBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(self.listWidget)
        self.setLayout(layout)

    def on_list_item_clicked(self, item):
        # Lorsqu'un élément de la liste est cliqué, déplacez la vidéo à la position correspondante
        self.videoWidget.set_position(int(item.get_value() * 1000))

    def on_video_position_changed(self, position):
        # Lorsque la position de la vidéo change, mettez en surbrillance l'élément de liste correspondant
        for i in range(self.listWidget.listWidget.count()):
            item = self.listWidget.listWidget.item(i)
            if item:
                start = int(item.get_value() * 1000)
                end = int((item.get_value() + 5) * 1000)  # Ajustez la fin comme vous le souhaitez
                if start <= position <= end:
                    self.listWidget.listWidget.setCurrentItem(item)
                    break
