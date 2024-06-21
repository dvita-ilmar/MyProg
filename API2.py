import requests

access_token = 'vk1.a.IXR5IdDKDvNUSEil-QJhmcY9DMaa7eHrFKueN5tvIkXky8gNEm3QAsmHJVczTLKAkLHl5Fz_H-uhpVQ7IEfeGesyyCLKIEKBLYI921TXGAQd-Ktsqbv3dMbxP_mY8sqrQt6QgtolEMgEPcGP2oibJ2cgy_Ubn2unk4KQlVRqzgYLIcG3UMnShiMWkZ3dsvEe'
user_input = 'milli_d'

# Формируем URL для запроса
url = "https://api.vk.com/method/users.get"
 
# Параметры запроса и их значения
params = {
    # Идентификатор или ник VK пользователя
    "user_ids": user_input,
    # Список полей, которые необходимо получить
    "fields": "city,career",
    # Ваш access_token
    "access_token": access_token,
    # Версия API
    "v": "5.199"
}
 
# Отправляем GET-запрос
response = requests.get(url, params)

# Получаем ответ в формате JSON
user_info = response.json()["response"][0]
print(user_info)
# Выводим информацию о пользователе в читабельном виде
'''
print("Имя:", user_info["first_name"])
print("Фамилия:", user_info["last_name"])
print("Город:", user_info["city"]["title"])
print("Карьера:")
'''
