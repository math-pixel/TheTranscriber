from convertor.ConversionCoordinator import *
from TranscriberContext import *
import unittest





class ConvertorTest(unittest.TestCase):
    def test_convertor_video_to_audio(self):
        trContextVideoInput = TranscriberContext.getContextWithVideo()
        trContextVideoInput.audioPath = None
        converterCoordinator = ConversionCoordinator.getConversionCoordinator()
        conversionResult = converterCoordinator.convert(trContextVideoInput)
        self.assertIsNotNone(trContextVideoInput.audioPath)


if __name__ == '__main__':
    unittest.main()
