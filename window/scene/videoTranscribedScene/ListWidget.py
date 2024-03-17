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
