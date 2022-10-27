import requests
import datetime
from pprint import pprint
from config import Config


def get_weather(city, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        request = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )

        data = request.json()
        pprint(data)

        city = data['name']
        current_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не пойму, что там за погода!'
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        day_length = sunset_timestamp - sunrise_timestamp

        return f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n' \
               f'Погода в городе: {city}\n'\
               f'Температура: {current_weather}°С {wd}\n'\
               f'Влажность: {humidity}%\n'\
               f'Давление: {pressure} мм.рт.c\n'\
               f'Скорость ветра: {wind_speed} м/с\n'\
               f'Восход солнца: {sunrise_timestamp}\n'\
               f'Закат солнца: {sunset_timestamp}\n'\
               f'Продолжительность дня: {day_length}'
    except Exception as ex:
        print(ex)
        return 'Проверьте название города'

