import pyttsx3
import speech_recognition as sr
import json
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
voiceRate = 165
engine.setProperty('rate', voiceRate)


def speak(audio):
    engine.say(audio)
    print(audio)

    now = datetime.datetime.now()
    time = now.strftime("%Y-%b-%d, %A %I:%M:%S")
    data = {}
    data['desktop'] = []
    data['desktop'].append(
        {
            'spoken': audio,
            'time': time
        }
    )

    with open('History.json', 'a') as outfile:
        json.dump(data, outfile)
        data = []


    engine.runAndWait()


def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recoginizing...")
        query = r.recognize_google(audio, language='en-in')
        puthistory(query)

    except Exception as e:
        speak("Please say Again,")
        listener()
        return "Nothing"

    return query



def puthistory(query):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%b-%d, %A %I:%M:%S")
    data = {}
    data['user'] = []
    data['user'].append(
        {
            'usermsg': query,
            'time': time
        }
    )

    with open('History.json', 'a') as outfile:
        json.dump(data, outfile)
        data = []






