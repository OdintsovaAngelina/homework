import requests
#импорт requests
from .read_json import read_json
#импорт read_json
import json
#импорт json
data_api = read_json(name_file= 'config_api.json')
#Чтение данных из файла config_api.json и сохранение их в переменной data_api
API_KEY = data_api['api_key']
#Извлечение API ключа для доступа к OpenWeather API из словаря data_api
CITY_NAME = data_api['city_name']
#Извлечение названия города из словаря data_api для запроса прогноза погоды
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Формирование URL для запроса к OpenWeather API с указанием названия города и API ключа
response = requests.get(URL)
#Отправка GET-запроса к OpenWeather API для получения данных о погоде
if response.status_code == 200:
    #Проверка, что запрос успешен
    data_dict = json.loads(response.content)
    #Преобразование ответа в формате JSON в словарь Python
    print(json.dumps(data_dict, indent= 4))