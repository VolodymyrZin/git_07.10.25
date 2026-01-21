import random
import requests
import json

url = 'https://images-api.nasa.gov/search?q=mars&media_type=image'
response = requests.get(url)
data = response.json()
photo_url = data['collection']['items']
photos = random.sample(photo_url, 3)

for i, item in enumerate(photos, start=1):
    img_url = item['links'][0]['href']  # беремо URL першого зображення
    img_data = requests.get(img_url).content  # завантажуємо байти зображення

    filename = f'mars_{i}.jpg'  # створюємо ім’я файлу
    with open(filename, 'wb') as f:  # відкриваємо файл для запису
        f.write(img_data)  # записуємо зображення
