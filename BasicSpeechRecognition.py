import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognizer.recognize_sphinx()

print("Input: ")

while(True):
    ff7 = sr.AudioFile('')
    with ff7 as source:
        audio = recognizer.record(source)
    with microphone as source:
        audio = recognizer.listen(source)
        tempInput = recognizer.recognize_google(audio)
        print(tempInput)
        if(tempInput == 'exit'):
            break

