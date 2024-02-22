import sys
from PyQt5.QtWidgets import QApplication
from UI import *



if __name__ == '__main__':
    # Initialise l'application
    app = QApplication(sys.argv)

    # Crée et affiche la fenêtre
    # interface = UI()

    
    interface = UIDragAndDrop()
    interface.show()

    # Lance l'application
    sys.exit(app.exec_())
