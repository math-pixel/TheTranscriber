import sys
from PyQt5.QtWidgets import QApplication
from GUI.UI import *



def startUI(callback):
    # Initialise l'application
    app = QApplication(sys.argv)

    interface = UIDragAndDrop(callback)
    interface.show()
    
    # Lance l'application
    sys.exit(app.exec_())
