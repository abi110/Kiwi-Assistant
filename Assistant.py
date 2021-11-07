import speech_recognition as sr
import pyttsx3
import pywhatkit

# initialise the speech engine
engine = pyttsx3.init()
# set words per min rate of speech engine
engine.setProperty("rate", 170)


engine.say("I am your assistant")
engine.runAndWait()

listener = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            engine.say("What can I help you with")
            print('listening for you...')
            engine.say("listening")
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
    finally:
        pass
    return command


def run_engine():
    command = take_command()
    if "play" in command:
        print(command)
        song = command.replace("play", "")
        engine.say("playing" + song)
        engine.runAndWait()
        pywhatkit.playonyt(song)
    elif "what" or "who" or "why" or "when" or "where" in command:
        print(command)
        engine.say("fetching" + command)
        engine.runAndWait()
        wiki_answer = pywhatkit.info(command, 2, True)
        engine.say(f"Here...{wiki_answer}")
        engine.runAndWait()
    elif "no" or "go away" or "shut up" or "be quiet" or "off" or "turn off" in command:
        engine.say("Ok, speak soon")
        engine.runAndWait()
        exit()
    elif "help" in command:
        engine.say("""
        You can ask me to search for you using a who, what, when, where, or why question. 
        If you would like me to play a song please say 'play' followed by the song title or artist
        """)
        print("""
        You can ask me to search for you using a who, what, when, where, or why question. 
        If you would like me to play a song please say 'play' followed by the song title or artist
        """)
        engine.runAndWait()
    else:
        engine.say("sorry, I did not understand that, please try again, "
                   "if you want to know what I can do please say help")
        engine.runAndWait()


run_engine()
