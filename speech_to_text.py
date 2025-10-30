import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something...")
	audio = r.listen(source)
try:
	text = r.recognize_google(audio)
	print("The Audio you spoke is: ", text)
except sr.UnknownValueError:
	print("Audio is unable to understand.")
except sr.RequestError:
	print("Error in converting given speech into text.")
