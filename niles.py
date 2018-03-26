import speech_recognition as sr
import string
import webbrowser
import os

os.system("say Hallo Master. Wie darf ich Ihnen weiterhelfen?")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='de-DE')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def niles(data):
    data = data.lower()
    if "mach die musik an" in data:
        os.system("say ich mach den plattenspieler an.")
        os.system("spotify play")

    if "mach die musik aus" in data:
        os.system("say natürlich.")
        os.system("spotify pause")

    if "suche was im internet" in data:
        os.system("say was soll ich denn suchen?")
        thing = recordAudio().lower()
        os.system("say ich suche im internet nach {}".format(thing))
        webbrowser.open("https://www.google.com/search?q={}".format(thing))


go = True
while go:
    data = recordAudio()
    if data == "tschüss":
        os.system("say auf wiedersehen master.")
        go = False
    else:
        niles(data)


