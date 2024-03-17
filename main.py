from TranscriberContext import TranscriberContext
from transcription.TranscriptionController import TranscriptionController
from DLog import DLog
from Utils import Utils
from window.SceneManager import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    SceneManager.getInstance().show()
    sys.exit(app.exec_())


