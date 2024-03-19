from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QSizePolicy, QStyle
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

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
        
        self.slider.setStyleSheet("""
            QSlider {
                background-color: #f0f0f0;
                border-radius: 10px;
                height: 20px;
                margin: 10px 0;
            }

            QSlider::groove:horizontal {
                background-color: #ddd;
                border-radius: 5px;
            }

            QSlider::handle:horizontal {
                background-color: #FFA1A1;
                border-radius: 8px;
                width: 16px;
                height: 16px;
                margin: -4px 0;
            }

            QSlider::handle:horizontal:hover {
                background-color: #dF8181;
            }
        """)

        # Créer le label pour afficher les informations
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Créer le bouton pour jouer/pause la vidéo
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play_video)
        
        self.playButton.setStyleSheet("background-color: #FFA1A1; border: none; border-radius: 5px; padding: 10px; color: #fff")

        # self.printButton = QPushButton()
        # self.printButton.clicked.connect(self.set_value)

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
