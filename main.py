import requests
import os

os.makedirs("images_requests", exist_ok=True)

for i in range(10):
    response = requests.get("НЕ СМОГ НАЙТИ НОРМАЛЬНЫЙ САЙТ ЧТОБЫ ПРОЙТИСЬ ЦИКЛОМ")
    if response.status_code == 200:
        with open(f"images_requests/image_{i}.jpg", "wb") as f:
            f.write(response.content)
##################################################################

import requests
from bs4 import BeautifulSoup

url = "https://yandex.kz/pogoda/astana"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_info = soup.find('div', class_='temp fact__temp fact__temp_size_s').get_text()
    print("Погода в Астане:", weather_info) #я когда тестил было 0 градусов и у меня вывело 0 ¯\_(ツ)_/¯
else:
    print("Не удалось получить данные о погоде.")
