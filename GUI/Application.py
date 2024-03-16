import sys
from PyQt5.QtWidgets import QApplication
from GUI.UI import *
from GUI.GUI import *
from DLog import *

class Application:

    instance = None

    def __init__(self):
        # Initialise l'application
        self.app = QApplication(sys.argv)
        
        self.page1 = None
        self.page2 = None

        self.actualPage = None

    def setActualPage(self):
        pass

    def launchApplication(self):
        pass
'''
    def startFirstPage(self, callback):
        
        self.page1 = UIDragAndDrop(callback)
        self.page1.show()
        
        sys.exit(self.app.exec_())


    def startSecondPage(self, result, video_path):
        
        if self.page1 == None:
            DLog.errorbiglog("The first page has not been created.")
            sys.exit(self.app.exec_())
            
        print("Page 1 hide")
        self.page1.close()
        
        
        print("Show page 2")
        self.page2 = UIResult(result, video_path)
        print("Page loadings")
        self.page2.show()
        
        print("Page  2 showed")
        
        sys.exit(self.app.exec_())
'''

    @staticmethod
    def getInstance():
        if Application.instance == None:
            Application.instance = Application()
        return Application.instance
        