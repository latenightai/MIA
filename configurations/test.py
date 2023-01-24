import warnings
import pyttsx3
import speech_recognition as sr

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        audio = recog.listen(source)
    
    data = " "
    try:
        data = recog.recognize_google(audio)
        print("You said: "+data)
    
    except sr.RequestError as ex:
        print("Request Error from Googele Speech")
    except sr.UnknownValueError:
        print("Assistant could not recognized the audio")
    return data

rec_audio()