import requests
import json
import tkinter as tk
from dotenv import load_dotenv
import os
load_dotenv()

root = tk.Tk()  # создание главного окна приложения
root.geometry("300x300")  # задание размера окна
root.title("Погода")  # задание заголовка окна

def get_weather(city):
    api_key = os.getenv("API_KEY")  # получение значения переменной API_KEY из файла .env
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # формирование URL-адреса для запроса погоды
    response = requests.get(url)  # выполнение запроса к API OpenWeatherMap
    if response.status_code != 200:  # проверка статус-кода ответа на запрос
        label['text'] = "Ошибка"  # вывод сообщения об ошибке в метку
    else:
        data = json.loads(response.text)  # преобразование ответа в формат JSON и сохранение данных в переменной data
        temperature = data['main']['temp']  # получение температуры из данных ответа
        description = data['weather'][0]['description']  # получение описания погоды из данных ответа
        label['text'] = f"Температура: {temperature}°C\nОписание: {description}"  # вывод информации о погоде в метку

entry = tk.Entry(root)  # создание виджета ввода для ввода названия города
entry.pack()  # размещение виджета на форме
button = tk.Button(root, text="Получить погоду", command=lambda: get_weather(entry.get()))  # создание кнопки и привязка функции get_weather к ее событию нажатия
button.pack()  # размещение кнопки на форме

label = tk.Label(root, text="")  # создание метки для вывода информации о погоде
label.pack()  # размещение метки на форме

root.mainloop()  # запуск главного цикла обработки событий приложения
