


import pyttsx3

engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.say("hello my name is khan shoab akhtar vakil ahmad")
engine.runAndWait()