import speech_recognition as sr

sample_rate = 44100 

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = sample_rate) as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Audio UnknownValueError"
    except sr.RequestError as e:
        return "Cannot obtain result; {0}".format(e)
