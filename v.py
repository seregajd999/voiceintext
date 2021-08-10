import speech_recognition as sr

def record_volume():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        print('Слушаю...')
        audio = r.listen(source)

    query = r.recognize_google(audio, language = 'ru-RU')
    print(f'Вы сказали: {query.lower()}')

record_volume()
