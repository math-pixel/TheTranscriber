from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QListWidget, QListWidgetItem, QScrollArea


class CustomQListWidgetItem(QListWidgetItem):
    def __init__(self, text, value, parent=None):
        super().__init__(text, parent)
        self.value = value

    def get_value(self):
        return self.value

class ListWidget(QWidget):
    # Tab is the result from the transcriber in this case
    def __init__(self, tab, videoDisplay, parent=None):
        super().__init__(parent)
        
        self.tab = tab
        self.videoWidget = videoDisplay
        
        
        self.layout = QVBoxLayout()
        
        self.listWidget = QListWidget()
        self.listWidget.setStyleSheet("""
            QListWidget {
                padding: 10px;
                border-radius: 5px;
                background-color: #76CA62;
                color: #fff;
                font-size: 20px;
                border: solid 4px #A8DD9B;
            }
        """)
        
         # Custom scrollbar
        self.setStyleSheet("""
            QScrollBar {
                background-color: #A8DD9B;
                border-radius: 5px;
                width: 10px;
            }

            QScrollBar::handle {
                background-color: #76CA62;
                border-radius: 5px;
            }
        """)
        
        self.items = self.setItems(self.tab)
        for item in self.items:
            self.listWidget.addItem(item)

        self.listWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.listWidget)

        self.layout.addWidget(self.scrollArea)
        self.setLayout(self.layout)


    def setItems(self, tab):
        items = []
        for item in tab:
            items.append(CustomQListWidgetItem(item["text"], item["start"]))
        return items
