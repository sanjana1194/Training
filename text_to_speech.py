import pyttsx3
engine = pyttsx3.init()
text = input("Enter something to speak: ")
engine.say(text)
engine.runAndWait()
