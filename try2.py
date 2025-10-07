import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import sys
import pyautogui
import urllib.parse
import subprocess
from faker import Faker

speaker = win32com.client.Dispatch("SAPI.SpVoice")
selected_voice_index = 1


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold = 0.1
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            user_query = r.recognize_google(audio, language="en-in")
            print("Recognizing...")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Something went wrong. Please check the code."


def wishMe():
    query = ""
    # --------------------------------BIRTHDAY----------------------------------------
    if "tejesh birthday" in query.lower() or "birthday tejesh" in query.lower():
        print()
        print("-------------------------------")
        print("Tejesh birthday is on 02/03/2005")
        print("-------------------------------")
        print()
    elif "jayesh birthday" in query.lower() or "birthday jayesh" in query.lower():
        print()
        print("-------------------------------")
        print("Jayesh birthday is on 02/03/2005")
        print("-------------------------------")
        print()
    elif "shakuntala birthday" in query.lower() or "birthday shakuntala" in query.lower():
        print()
        print("-------------------------------")
        print("Shakuntala birthday is on 16/06/1985")
        print("-------------------------------")
        print()
    # --------------------------------------------------------------------------------


    # ------------------------------------DEVELOPER-----------------------------------
    if "developer" in query.lower():
        print()
        print("'''")


while True:
    timenow = wishMe()
    speaker.Voice = speaker.GetVoices().Item(selected_voice_index)
    print('''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            Welcome Sir
                                                                                           -------------

Hello sir I am jarvis I am your A.I Assistance
Please Let me know If I can help you

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''')
    print()
    speaker.Speak(f"{timenow} Sir Please let me know If I can help you")


    while True:
        password_correct = False
        while not password_correct:
            print("Listening...")
            query = takeCommand()