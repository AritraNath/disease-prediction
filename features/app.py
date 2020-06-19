import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=1)
    print("Speak Anything")
    audio = r.listen(source)
    text = ""

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))

    except:
        print("Sorry could not recognize your voice.")
