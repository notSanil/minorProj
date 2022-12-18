# Image To Text To Speech
This is an image to text to speech made using tesseract library by google for OCR, and gTTS for speech generation. 

Part of minor project submission by group 18.


# Run the project

## Install tesseract
Install the tessract binaries from this link
```
https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows
```

Make sure that the installed binaries are added to the PATH variable of your computer

## Clone the project
Clone the project using
```
git clone https://github.com/notSanil/minorProj.git
```

## Install libraries
Run the ` init.bat ` script to create the virtual environment and install required libraries

## Run the server
Either run the `run.bat` script, or run the command
```
flask --app imageToSpeech --debug run
```
to run the server

## View the website
Open your browser and go to `127.0.0.1:5000` to view the website