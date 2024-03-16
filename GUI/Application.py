import sys
from PyQt5.QtWidgets import QApplication, QWidget
from DLog import *

class Application:

    instance = None

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.actualPage = None

    # Where we set the actual page
    def setActualPage(self, page: QWidget):
        if self.actualPage != None:
            self.actualPage.close()
            pass
        self.actualPage = page;
        self.actualPage.show()
        pass

    # Where we launch the application, we need to set the atual page before launching the application
    def launchApplication(self):
        if self.actualPage == None:
            DLog.errorbiglog("Actual page isn't set")
            return
        
        sys.exit(self.app.exec_())
        pass

    @staticmethod
    def getInstance():
        if Application.instance == None:
            Application.instance = Application()
        return Application.instance
        