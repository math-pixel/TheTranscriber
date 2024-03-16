import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSlider, \
    QSizePolicy, QStyle, QListWidget, QListWidgetItem, QScrollArea, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont

class VideoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Créer le lecteur vidéo et le widget vidéo
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        # Créer le slider pour contrôler la position de la vidéo
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Créer le label pour afficher les informations
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Créer le bouton pour jouer/pause la vidéo
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play_video)

        self.printButton = QPushButton()
        self.printButton.clicked.connect(self.set_value)

        # Créer la liste pour stocker les lignes de texte avec les valeurs non affichées
        self.text_lines = []

        # Connecter les signaux du lecteur vidéo
        self.mediaPlayer.stateChanged.connect(self.media_state_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        # Mise en page
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.playButton)
        hboxLayout.addWidget(self.slider)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.videoWidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def open_file(self, filename):
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playButton.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def media_state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playButton.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def get_value(self):
        sliderValue = self.slider.value()
        print(sliderValue)

    def set_value(self):
        # Définir la position du slider sur la valeur spécifiée (29195 dans cet exemple)
        self.set_position(29195)

    def add_text_line(self, text, value):
        # Ajouter une ligne de texte avec une valeur non affichée à la liste
        self.text_lines.append((text, value))
