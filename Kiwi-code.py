import speech_recognition as sr
import pyttsx3
import pywhatkit


kiwi = pyttsx3.init()
kiwi.setProperty("rate", 178)

kiwi.say("I am your kiwi")
kiwi.say("What can I help you with")
kiwi.runAndWait()

listener = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening for you...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'kiwi' in command:
                command = command.replace("kiwi", "")
                print(command)
    finally: pass
    return command


def run_kiwi():
    command = take_command()
    if "play" in command:
        print(command)
        song = command.replace("play", "")
        kiwi.setProperty("rate", 178)
        kiwi.say("playing" + song)
        pywhatkit.playonyt(song)


run_kiwi()
