from transcriber.TranscriberManager import *
from TranscriberContext import *
from DLog import *
import unittest

def runTranscribtion(tsContext):
    def myEndedFunctionDamour(result):
        tsContext.transcribeText = result["segments"]

    contextTranscriber = IATranscriberContext("small")
    myManager = TranscriberManager()
    myManager.setCurrentAI(ListAI.WHISPER, contextTranscriber)
    myManager.transcribe(tsContext.audioPath, myEndedFunctionDamour)

class TranscriberTest(unittest.TestCase):
    def test_transcriber(self):
        tsContext = TranscriberContext.getContextWithVideoAndAudio()
        runTranscribtion(tsContext)
        self.assertIsNotNone(tsContext.transcribeText)

if __name__ == '__main__':
    unittest.main()