# TheTranscriber

## How to simply run the program ?

### Docker

```bash
docker compose up -d
```

## Installing youtube-dl

`youtube-dl` is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform-specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

### Installation

#### Brew

```bash
brew install youtube-dl
```

#### Ubuntu

```bash
sudo apt-get install youtube-dl
```

#### Windows

Download the Windows executable from [here](https://youtube-dl.org/downloads/latest/youtube-dl.exe) and put it on your `PATH`.

## Installing libmagic

`libmagic` is a versatile library for identifying file types by analyzing their content, akin to the Unix file command. Compatible with Python versions 2.6, 2.7, and 3.2+, it operates seamlessly across Unix, Windows, and macOS systems. It's open for modification, redistribution, or any use, adhering to a public domain license. Ideal for validating uploaded files or classifying file types in diverse applications, libmagic offers a robust solution for file management challenges.

### Installation

#### Brew

```bash
brew install libmagic
```

#### Ubuntu

```bash
sudo apt-get install libmagic1
```

#### Windows

Install with the requirements.txt
