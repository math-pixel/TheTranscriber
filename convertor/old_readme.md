# How to use ?

## The base : 

### Basic example
Basically, you will need a TranscriberContext instance
```py
# TranscriberContext.getContextWithVideo() is the factory method to get a transcriber context with an input path, here it is a video path for this example
trContextVideoInput = TranscriberContext.getContextWithVideo()

# ConversionCoordinator.getConversionCoordinator() is a factory method that returns a basic ConversionCoordinator instance with the basic constructor params
converterCoordinator = ConversionCoordinator.getConversionCoordinator()

# ConversionCoordinator.convert() will fill audio path and video path of the transcriber context and returns a boolean if the convertion success or failed
wasConverted = converterCoordinator.convert(trContextVideoInput)
```

### More explanation
ConversionCoordinator is the main object that will convert the TranscriberContext, 
we don't really need more explanation
```
ConversionCoordinator.convert(TranscriberContext)
```

# The Structure

## The Convert Coordinator Class

This is the class that will coordinate everything; it's the one we instantiate if we want to execute a conversion.


---

## The Conversion Analyzer Class

#### Why not just an Analyzer class instead of Conversion Analyzer?
I imagined that it might be necessary to add an Analyzer in another part of the application, so simply defining this class as an Analyzer in a more generic way could cause issues if we had to, for example, analyze the URL at the very beginning.

#### What does it do
The purpose of the class is to analyze the "path" of the file (hence the file) to determine the strategy that the Convertor will use to convert the said file.

---

## The Convertor Class

#### Convertor Strategy, hmm?
The Convertor class contains a strategy, which will be executed when we want to convert. However, it is not the Convertor class that sets the strategy but rather the class just below in the README (the Conversion Analyzer class, somewhat).

---

## The Convertor Strategy Class

#### Ahem?
The goal is to have a "protocol" that will allow defining many strategies, and from there, we can execute it, and it will do different things depending on what it is (like if it's MP4ToMP3, it does stuff related to converting MP4 to MP3).

---

## The UaImAiLeuh (UML)

It may not be the best UML; if there are questions about the clarity of this thing, no worries, haha.
![](./'uml'rig_convertor.png)