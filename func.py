import datetime
import os
import sys
import time
import webbrowser
import keyboard
import pyttsx3
import speech_recognition as sr
import json
import pyautogui
import subprocess
import clipboard
from PIL import Image, ImageGrab
import random

from engine import *
from difflib import get_close_matches 
  
def closeMatches(patterns, word): 
    return get_close_matches(word, patterns)

    
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)   

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Sir!,")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!,")
    else:
        speak("Good Evening, Sir!")

    speak("I am Your Desktop Astistance.")
    speak("Press Ctrl+Alt+D To Give Me Command Any Time")

def split(word):
    return [char for char in word]

def hello():
    speak("Hello How May I Help You?")

def whoareyou():
    speak("I am Your Desktop Astistance. Give Me Command")

def whatistime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The Time is : " + strTime)

def opengoogle():
    speak("Opening Google")
    os.system("start chrome google.com")

def openyoutube():
    speak("Opening Youtube,")
    os.system("start chrome youtube.com")


def installpythonpackageusingpip():
    speak("Which Python Package You Want to Install?") 
    packageName = listener()
    speak("Have You Said " + packageName)
    packageinstallsure = listener().lower()
    if packageinstallsure == "yes":
        speak("Installing Package")
        os.system("pip install " + packageName)
        speak("Package Installing Proccess Completed")
    elif packageinstallsure == "no":
        speak("Ok Sir Please tell Me Package Name")
        installpythonpackageusingpip()

def openvscode():
    speak("Opening V s Code")
    os.system("code")

def shutdown(): 
    speak("Bye Sir. Have a Good Day. Just Press Ctrl+Alt+d To Call Me. I will Come.")
    print("Exited System. Press Ctrl+Alt+d To call Again")

def ok():
    speak("That's My Pleasure")

def thanksorthankyou():
    speak("That's My Pleasure")

def youtubelivecomment():
    speak("Opening youtube Live Stream Commenter")
    os.system("cd ../Youtube Live Voice Chat && python main.py")

def searchinyoutube():
    speak("What You Want to Search?")
    tosearch = listener()
    speak("You Search text is " + tosearch)
    speak("are you sure you want to search")
    searchsure = listener().lower()
    if "yes" in searchsure:
        tosearch = tosearch.replace(" ", "%20")
        os.system("start chrome https://www.youtube.com/results?search_query=" + tosearch)

    elif "no" in searchsure:
        searchinyoutube()

def file_check_at_location(path, filename):
    return os.path.exists(path + str(filename))

def takescreenshot(indexforscreenshot):
    speak("Capturing Screenshot")
    screenshot = ImageGrab.grab()
    speak("Screenshot Captured")
    speak("Saving Screenshot")
    path = 'D:\\Screenshots\\'
        
    savefile(indexforscreenshot, path, screenshot)

    
def savefile(indexforscreenshot, path, screenshot):
    now = datetime.datetime.now()
    timeofimage = now.strftime("%d-%m")
    now = datetime.datetime.now()
    imagename = str(indexforscreenshot) + ") " + timeofimage + ".png"
    savelocation = path + imagename
    if file_check_at_location(path, imagename):
        indexforscreenshot += 1
        savefile(indexforscreenshot, path, screenshot)
    elif not file_check_at_location(path, imagename):
        screenshot.save(savelocation)
        speak("Screenshot Saved")
        indexforscreenshot += 1


def searchingoogle():
    speak("What You Want to Search?")
    tosearch = listener()
    speak("You Search text is " + tosearch)
    speak("are you sure you want to search")
    searchsure = listener().lower()
    if "yes" in searchsure:
        tosearch = tosearch.replace(" ", "%20")
        os.system("start chrome https://www.google.com/search?q=" + tosearch)
        speak("Searching Proccess Completed")
        
    elif "no" in searchsure:
        searchingoogle()
    
def getposition():
    while True:
        print(pyautogui.position())

def sendmessageinwhatsapp():
    username = getusernameforsendmessageinwhatsapp()
    msg = getmsgforsendmessageinwhatsapp()
    speak("Starting Whatsapp")
    pyautogui.moveTo(398, 746)
    pyautogui.click()
    speak("the Sending Proccess Started Please Don't Do anything")
    time.sleep(random.randint(15, 20))
    pyautogui.moveTo(351, 110)
    pyautogui.click()
    username = split(username)
    for i in range(len(username)):
        pyautogui.keyDown(username[i])
    pyautogui.keyDown('enter')
    pyautogui.moveTo(1235, 700)
    pyautogui.click()
    msg = split(msg)
    for i in range(len(msg)):
        pyautogui.keyDown(msg[i])
    pyautogui.keyDown("enter")
    speak("Message Sent Successfully")

def getusernameforsendmessageinwhatsapp():
    speak("Please Speak The User Name")
    username = listener().lower()
    if username == "" or username == "Nothing":
        getusernameforsendmessageinwhatsapp()
    else:
        speak("The Username is " + username)
        speak("Are You Sure To Set This Username?")
        sure = listener().lower()
        if "yes" in sure:
            return username
        else:
            getusernameforsendmessageinwhatsapp()

def getmsgforsendmessageinwhatsapp():
    speak("Please Speak The Message You Want to Send")
    msg = listener()
    if msg == "" or msg == "Nothing":
        getmsgforsendmessageinwhatsapp()
    else:
        speak("The Message is " + msg)
        speak("Are You Sure To Set This Message?")
        suremsg = listener().lower()
        if "yes" in suremsg:
            return msg
        else:
            getmsgforsendmessageinwhatsapp()