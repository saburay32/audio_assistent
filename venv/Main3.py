#-------------------------------------
# Program by Smolyak EW
#
# Version Date Information
# 1.0 2019 13/06
#
#-------------------------------------
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser

# настройки
opts = {
    "alias": ('алик', 'аллик', 'ал', 'алл', 'аллл', 'аля',
              'аа', 'аль', 'алъ', 'ал л', 'лик','алек', 'аллек', 'синебот','бот', 'ботулизм', 'ебот' ,'элит', 'оля'),
    "tbr": ('скажи', 'скаажи','скажии', 'скаажии','расскажи', 'покажи', 'сколько', 'произнеси','сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час','время'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('анекдот''расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "open website": ('открой веб сайт','открой сайт', 'открой страницу'),
        "weather": ('погода', 'открой погоду', 'покажи погоду', 'открой яндекс погоду')
    }
}


# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Алику
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmds'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
        speak("Алик слушает")

    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")



def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # воспроизвести радио
        #os.system("D:\\Jarvis\\res\\radio_record.m3u")
        os.startfile('E:\Audio\ASash! - Adelante.mp3')
    elif cmd =='open website':
        speak('Уже открываю')
        #url = "http://pythontutor.ru/lessons/lists/"
        webbrowser.open("http://pythontutor.ru/lessons/lists/",new=0, autoraise=True)
    elif cmd == 'weather':
        speak('Минуточку')
        url = 'https://yandex.ru/pogoda/'
        webbrowser.open(url,new=1, autoraise=True)

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... хотя... Научился ёжик жопой дышать, сел на пенёк и задохнулся... Ха ха ха")

    else:
        print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

#v Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

# forced cmd test
speak(" ... .. я Алик синебот ")

speak("Добрый день, повелитель")
speak("Алик слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop