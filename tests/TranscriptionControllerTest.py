from transcription.TranscriptionController import *
from DLog import *
import unittest

class TranscriptionControllerTest(unittest.TestCase):
    # This test just check if the singleton function "getInstance" is properly implemented
    def test_singleton(self):
        trController1 = TranscriptionController.getInstance()
        trController2 = TranscriptionController.getInstance()
        self.assertEqual(trController1, trController2)


if __name__ == '__main__':
    unittest.main()