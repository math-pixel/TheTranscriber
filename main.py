from TranscriberContext import *
from transcription.TranscriptionController import *
from GUI.Application import *
from GUI.UI import *
from DLog import *
from Utils import Utils


def tempCallback(result):
    DLog.errorbiglog("Callback function for transcription isn't set")
    

def launchTranscription(url, callback = tempCallback):
    TranscriptionController.getInstance().startTranscription(url, callback)


app = Application.getInstance()
app.setActualPage(UIDragAndDrop(launchTranscription))
app.launchApplication()

''' 
result = [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 5.6000000000000005, 'text': " We're introducing three revolutionary products of this class.", 'tokens': [50364, 492, 434, 15424, 1045, 22687, 3383, 295, 341, 1508, 13, 50644], 'temperature': 0.0, 'avg_logprob': -0.40571454366048176, 'compression_ratio': 1.17, 'no_speech_prob': 0.002564801834523678}, {'id': 1, 'seek': 0, 'start': 5.6000000000000005, 'end': 15.1, 'text': ' The first one is a widescreen iPod with touch controls.', 'tokens': [50644, 440, 700, 472, 307, 257, 21516, 66, 1492, 5180, 378, 365, 2557, 9003, 13, 51119], 'temperature': 0.0, 'avg_logprob': -0.40571454366048176, 'compression_ratio': 1.17, 'no_speech_prob': 0.002564801834523678}, {'id': 2, 'seek': 1510, 'start': 15.1, 'end': 40.1, 'text': ' The second is a revolutionary mobile camera.', 'tokens': [50364, 440, 1150, 307, 257, 22687, 6013, 2799, 13, 51614], 'temperature': 0.0, 'avg_logprob': -0.5153783957163492, 'compression_ratio': 0.8461538461538461, 'no_speech_prob': 0.009670082479715347}, {'id': 3, 'seek': 4010, 'start': 40.1, 'end': 50.1, 'text': ' And the third is a breakthrough Internet communications device.', 'tokens': [50364, 400, 264, 2636, 307, 257, 22397, 7703, 15163, 4302, 13, 50864], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 4, 'seek': 4010, 'start': 50.1, 'end': 60.1, 'text': ' These are not three separate devices. This is one device.', 'tokens': [50864, 1981, 366, 406, 1045, 4994, 5759, 13, 639, 307, 472, 4302, 13, 51364], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 5, 'seek': 4010, 'start': 60.1, 'end': 66.1, 'text': ' And we are calling it iPhone.', 'tokens': [51364, 400, 321, 366, 5141, 309, 7252, 13, 51664], 'temperature': 0.0, 'avg_logprob': -0.22980055937895905, 'compression_ratio': 1.3130434782608695, 'no_speech_prob': 0.09138037264347076}, {'id': 6, 'seek': 6610, 'start': 66.1, 'end': 74.1, 'text': ' Today Apple is going to reinvent the phone.', 'tokens': [50364, 2692, 6373, 307, 516, 281, 33477, 264, 2593, 13, 50764], 'temperature': 0.0, 'avg_logprob': -0.22366726398468018, 'compression_ratio': 0.8431372549019608, 'no_speech_prob': 0.20343056321144104}]
        
app.setActualPage(UIResult(result, Utils.getDirectoryAbsolutePath() +"/export/video.mp4"))
'''


