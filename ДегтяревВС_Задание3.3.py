'''
Задание 3: Работа с API

Пример 3. Запросите у пользователя идентификатор аккаунта VK, у которого он желает просмотреть список друзей.
Выведите только общее количество друзей пользователя в консоль. Для этого Вам необходимо, как и при работе с любым API,
найти необходимый метод и изучить его описание, параметры и их значения, которыми можно варьировать. Также для работы с
API VK Вам потребуется access token, процедуру получения которого мы разбирали на практике.
Используйте API VK https://dev.vk.com/ru/method 
* По желанию доработайте программу: выведите основную информацию о каждом друге и дополнительно информацию о последнем
его заходе в сеть. В полученном json друзья сразу должны быть отсортированы имени.
'''
import requests, datetime

# Мой access_token для доступа к API VK
access_token = 'vk1.a.IXR5IdDKDvNUSEil-QJhmcY9DMaa7eHrFKueN5tvIkXky8gNEm3QAsmHJVczTLKAkLHl5Fz_H-uhpVQ7IEfeGesyyCLKIEKBLYI921TXGAQd-Ktsqbv3dMbxP_mY8sqrQt6QgtolEMgEPcGP2oibJ2cgy_Ubn2unk4KQlVRqzgYLIcG3UMnShiMWkZ3dsvEe'
# Запрашиваем у пользователя идентификатор VK
user_input = int(input('Введите идентификатор пользователя'))

# Формируем URL для запроса
url = "https://api.vk.com/method/friends.get"

# Параметры запроса и их значения
params = {
    # Идентификатор или ник VK пользователя
    "user_id": user_input,
    # Список полей, которые необходимо получить
    "fields": "last_seen",
    "order": "name",
    # access_token
    "access_token": access_token,
    # Версия API
    "v": "5.199"
}
 
# Отправляем GET-запрос
response = requests.get(url, params)
# Получаем ответ в формате JSON
user_info = response.json()

# Выводим информацию о количестве друзей
print(f'Всего друзей у данного пользователя в ВК: {user_info["response"]["count"]}')
# Выводим информацию о пользователе в читабельном виде
for item in user_info["response"]["items"]:
    print(f'ID:{item["id"]} имя: {item["first_name"]} фамилия: {item["last_name"]} последний вход: {datetime.datetime.utcfromtimestamp(item["last_seen"]["time"]).strftime("%Y-%m-%d %H:%M:%S")}')