import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class InputButtonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Créer des widgets
        self.inputText = QLineEdit(self)
        self.button = QPushButton("Click here", self)

        # Evennement au clic
        self.button.clicked.connect(self.buttonClicked)

        # Mise en page
        layout = QHBoxLayout()
        layout.addWidget(self.inputText)
        layout.addWidget(self.button)


        # Mise en page
        self.setLayout(layout)


    # Functions
    def buttonClicked(self):
        print(f"Le bouton à été cliqué. Voilà le contenu de l'input : {self.inputText.text()}")


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        # Créer des widgets
        self.inputButtonWidget = InputButtonWidget(self)
        self.label = QLabel("Test de texte")


        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.inputButtonWidget)
        layout.addWidget(self.label)


        # Mise en page
        self.setLayout(layout)


        # Configure la fenêtre principale
        self.setWindowTitle("Interface")
        self.setGeometry(100, 100, 400, 200)

if __name__ == '__main__':
    # Initialise l'application
    app = QApplication(sys.argv)

    # Crée et affiche la fenêtre
    interface = GUI()
    interface.show()

    # Lance l'application
    sys.exit(app.exec_())
