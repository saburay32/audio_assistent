import speech_recognition as sr


def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5)  #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: ', text)#{query.lower()}
    except:
        print('Error')


while True:
    record_volume()