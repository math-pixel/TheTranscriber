import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QSlider, \
    QSizePolicy, QStyle, QListWidget, QListWidgetItem, QScrollArea, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont


class CustomQListWidgetItem(QListWidgetItem):
    def __init__(self, text, value, parent=None):
        super().__init__(text, parent)
        self.value = value

    def get_value(self):
        return self.value

class ListWidget(QWidget):
    def __init__(self, tab, videoDisplay, parent=None):
        super().__init__(parent)

        self.listWidget = QListWidget()
        self.tab = tab
        items = self.setItems(self.tab)
        for item in items:
            self.listWidget.addItem(item)

        # Augmenter la taille du texte
        font = self.listWidget.font()
        font.setPointSize(14)  # Taille de police de 14 points, ajustez-la selon vos besoins
        self.listWidget.setFont(font)

        # Faire en sorte que la liste prenne toute la hauteur de sa section
        self.listWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.listWidget)

        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        self.setLayout(layout)

        self.listWidget.itemSelectionChanged.connect(self.get_selected_item_value)

        self.videoWidget = videoDisplay

    def get_selected_item_value(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            self.videoWidget.set_position(int(selected_item.get_value() * 1000))

    def setItems(self, tab):
        items = []
        for item in tab:
            items.append(CustomQListWidgetItem(item["text"], item["start"]))
        return items

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

class ParentWidget(QWidget):
    def __init__(self, result, parent=None):
        super().__init__(parent)
        self.result = result

        # Créer des widgets
        self.videoWidget = VideoWidget()
        self.listWidget = ListWidget(self.result, self.videoWidget)

        # Charger la vidéo
        self.videoWidget.open_file("export/video.mp4")

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


class UIResult(QWidget):
    def __init__(self, result):
        super().__init__()
        self.result = result

        # Créer et afficher le widget parent
        self.parentWidget = ParentWidget(self.result)

        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.parentWidget)
        self.setLayout(layout)

        # Configure la fenêtre principale
        self.setWindowTitle("Interface")
        self.resize(1280, 556)



result = [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 5.6000000000000005, 'text': " We're introducing three revolutionary products of this class.", 'tokens': [50364, 492, 434, 15424, 1045, 22687, 3383, 295, 341, 1508, 13, 50644], 'temperature': 0.0, 'avg_logprob': -0.40571454366048176, 'compression_ratio': 1.17, 'no_speech_prob': 0.002564801834523678}, {'id': 1, 'seek': 0, 'start': 5.6000000000000005, 'end': 15.1, 'text': ' The first one is a widescreen iPod with touch controls.', 'tokens': [50644, 440, 700, 472, 307, 257, 21516, 66, 1492, 5180, 378, 365, 2557, 9003, 13, 51119], 'temperature': 0.0, 'avg_logprob': -0.40571454366048176, 'compression_ratio': 1.17, 'no_speech_prob': 0.002564801834523678}, {'id': 2, 'seek': 1510, 'start': 15.1, 'end': 40.1, 'text': ' The second is a revolutionary mobile camera.', 'tokens': [50364, 440, 1150, 307, 257, 22687, 6013, 2799, 13, 51614], 'temperature': 0.0, 'avg_logprob': -0.5153783957163492, 'compression_ratio': 0.8461538461538461, 'no_speech_prob': 0.009670082479715347}, {'id': 3, 'seek': 4010, 'start': 40.1, 'end': 50.1, 'text': ' And the third is a breakthrough Internet communications device.', 'tokens': [50364, 400, 264, 2636, 307, 257, 22397, 7703, 15163, 4302, 13, 50864], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 4, 'seek': 4010, 'start': 50.1, 'end': 60.1, 'text': ' These are not three separate devices. This is one device.', 'tokens': [50864, 1981, 366, 406, 1045, 4994, 5759, 13, 639, 307, 472, 4302, 13, 51364], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 5, 'seek': 4010, 'start': 60.1, 'end': 66.1, 'text': ' And we are calling it iPhone.', 'tokens': [51364, 400, 321, 366, 5141, 309, 7252, 13, 51664], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 6, 'seek': 6610, 'start': 66.1, 'end': 74.1, 'text': ' Today Apple is going to reinvent the phone.', 'tokens': [50364, 2692, 6373, 307, 516, 281, 33477, 264, 2593, 13, 50764], 'temperature': 0.0, 'avg_logprob': -0.22366726398468018, 'compression_ratio': 0.8431372549019608, 'no_speech_prob': 0.20343056321144104}]


if __name__ == '__main__':
    # Initialise l'application
    app = QApplication(sys.argv)

    # Crée et affiche la fenêtre
    interface = UIResult(result)
    interface.show()

    # Lance l'application
    sys.exit(app.exec_())

