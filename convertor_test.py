from convertor.ConversionCoordinator import *
from TranscriberContext import *
import time



def testConversion(transcriberContext, testName):
    DLog.goodbiglog(f"==========TEST : {testName} STARTED==========")
    try:
        converterCoordinator = ConversionCoordinator.getConversionCoordinator()
        conversionResult = converterCoordinator.convert(transcriberContext)
        DLog.goodlog(f"Audio path : {transcriberContext.audioPath}")
        DLog.goodlog(f"Video path : {transcriberContext.videoPath}")
        DLog.goodbiglog(f"==========TEST : {testName} PASSED==========")
    except:
        DLog.errorbiglog(f"==========TEST : {testName} ERROR==========")


time.sleep(2)
trContextAudioInput = TranscriberContext.getContextWithInputAudio()
testConversion(trContextAudioInput, "Transcriber with audio")
time.sleep(2)
trContextVideoInput = TranscriberContext.getContextWithVideo()
trContextVideoInput.audioPath = None
testConversion(trContextVideoInput, "Transcriber without audio path")
