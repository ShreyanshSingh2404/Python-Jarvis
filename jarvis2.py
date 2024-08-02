import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import datetime
import os
import ctypes
import subprocess
import tkinter
import json
import operator
import random
import smtplib
import requests
import shutil
import pyjokes
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir")
    speak("I am Jarvis. Please tell how may i help you Shreyansh sir")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 10000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please..")
        return "none"
    return query

if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'open youtube' in query:
            speak("opening youtube sir enjoy")
            webbrowser.open("youtube.com")
        elif'open chrome' in query:
            speak("opening chrome for you sir")
            webbrowser.open("chrome.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is (strTime)")
        elif 'lock window' in query:
            speak("locking the operator")
            ctypes.windll.user32.lockworkstation()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif"Who invented you" in query or "who created you" in query:
            speak("i am invented by Mister shreyansh sir.")
        elif 'how are you' in query:
            speak("I am fine, Thank you sir.")
            speak("how are you, sir.")
        elif 'fine' in query or "good" in query:
            speak("It's good to know sir.")
        elif "change your name" in query:
            speak(" whhat would you like to call me,sir.")
            assname = takeCommand()
            speak("Thanks for my new name.")
            
        
            
            
            
            
            
