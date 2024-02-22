from convertor.ConversionCoordinator import *
from TranscriberContext import *
import time

trContextVideoInput = TranscriberContext.getContextWithVideo()
converterCoordinator = ConversionCoordinator.getConversionCoordinator()
conversionResult = converterCoordinator.convert(trContextVideoInput)
# Ça va print toujours le même truc ici, y pas vraiment de type de conversion
# C'est simplement un exemple pour montrer le squelette de l'idée
DLog.goodlog(trContextVideoInput.audioPath)
DLog.goodlog("====================")
DLog.goodlog("====================")
DLog.goodlog("==========VIDEO TEST CONVERSION PASSED==========")
DLog.goodlog("====================")
DLog.goodlog("====================")

time.sleep(2)

trContextAudioInput = TranscriberContext.getContextWithInputAudio()
converterCoordinator = ConversionCoordinator.getConversionCoordinator()
conversionResult = converterCoordinator.convert(trContextAudioInput)
# Ça va print toujours le même truc ici, y pas vraiment de type de conversion
# C'est simplement un exemple pour montrer le squelette de l'idée
DLog.goodlog(trContextAudioInput.audioPath)
DLog.goodlog("====================")
DLog.goodlog("====================")
DLog.goodlog("==========AUDIO TEST CONVERSION PASSED==========")
DLog.goodlog("====================")
DLog.goodlog("====================")