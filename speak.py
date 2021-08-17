



import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)
rate = engine.getProperty('rate') # getting details of current speaking rate
engine.setProperty('rate',0)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

speak("mr khan shoab akhtar wakil ahmad ")     