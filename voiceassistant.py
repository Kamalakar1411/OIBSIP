import speech_recognition as sprc
import wikipedia
import pyttsx3
import datetime

from va import speak

# The voice assistant name is Babji
babji = pyttsx3.init()
speechrecognizer = sprc.Recognizer()

with sprc.Microphone() as source:
    speak('Hello, I am Babji. How can I help you?')
    speechrecognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your command...')
    recordedaudio = speechrecognizer.listen(source)
    print('Command received')

try:
    print('Working on your command...')
    text = speechrecognizer.recognize_google(recordedaudio, language='en-US')
    print(f'Your Command: {text}')

    if "hello" in text.lower():
        babji.say('Hello! How can I assist you today?')
        babji.runAndWait()
    elif "current date" in text.lower():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        babji.say(f'Today\'s date is {current_date}')
        babji.runAndWait() 
    elif "current time" in text.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        babji.say(f'The current time is {current_time}')
        babji.runAndWait()
    else:
        wikisearch = wikipedia.summary(text)
        print('Wikipedia Summary:', wikisearch)
        babji.say(wikisearch)
        babji.runAndWait()

except Exception as ex:
    print(ex)
    babji.say('I encountered an error. Please try again.')
    babji.runAndWait()
