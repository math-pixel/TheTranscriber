from PyQt5.QtWidgets import QWidget, QHBoxLayout
from window.scene.videoTranscribedScene.VideoWidget import VideoWidget
from window.scene.videoTranscribedScene.ListWidget import ListWidget

class ParentWidget(QWidget):
    def __init__(self, result, video_path, parent=None):
        super().__init__(parent)
        self.result = result
        self.video_path = video_path

        self.videoWidget = VideoWidget()
        self.listWidget = ListWidget(self.result, self.videoWidget)
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
        self.videoWidget.set_position(int(item.get_value() * 1000))

    def on_video_position_changed(self, position):
        for i in reversed(range(self.listWidget.listWidget.count())):
            item = self.listWidget.listWidget.item(i)
            if item:
                start = int(item.get_value() * 1000)
                if position >= start:
                    item.setSelected(True)
                    break
