import random
import speech_recognition as sr
import playsound
from gtts import gTTS


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Google Speech Recognition thinks you said "+ r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError as e:
        print("Could not request result from Google Speech Recognition service; {0}".format(e))
        return 'request error'

def say(text):
    voice = gTTS(text,lang="ru")
    unique_filename = "audio_"+str(random.randint(0,100000))+".mp3"
    voice.save(unique_filename)
    playsound.playsound(unique_filename)
    print('Assistent: ',text)


def handle_message(message):
    if "хай" in message:
        say("И тебе не хворать боярин")
    elif "прощай"  in message:
        finish()
    else:
        say("Моя твоя не понимать")

def finish():
    say("Пока")
    exit()

if __name__ == '__main__':
    print('Test')

    while True:
        command = listen()
        handle_message(command)