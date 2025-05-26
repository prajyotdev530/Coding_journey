import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Capture from mic
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)


    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
    except:
        print("Sorry, could not recognize your voice.")