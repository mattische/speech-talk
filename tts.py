# /w virtualenvwrapper:
# mkvirtualenv myFolderOfMyNewVenv
# cd into folder
# source bin/activate
# do installs /w pip and so forth
# work
# deactivate
##############################################
#pip install gtts
from gtts import gTTS 

# requirements for SpeechRecognition (install first);
# sudo apt-get install python3-dev portaudio19-dev python-all-dev flac
# pip install SpeechRecognition
# possibly also;
#  apt-get install python-pyaudio 
import speech_recognition as sr 
import os
import sys
import time
import _thread



def play(txt):
    tts = gTTS(text=txt, lang="sv")
    tts.save("tts.mp3")
    os.system("cvlc -q tts.mp3")

def speech2Txt():
    try:
        print("Please talk to me")
        r = sr.Recognizer()
        
        with sr.Microphone(sample_rate = 44100) as source:
            audio = r.listen(source)

        t = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")

def speech2Str():
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        st = input("Enter text? ")
        _thread.start_new_thread(play, (st,))
    except Exception:
        print("duh")
    



while 1:
    q = input("Text to speech or speech to text? (t/s): ")
    if q == "t":
        speech2Str()
    elif q == "s":
        speech2Txt()
    else:
        print("bye") 
        sys.exit()

