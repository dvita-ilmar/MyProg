'''
Задание 3: Работа с API

Пример 1: Выведите в консоль категории товаров, представленных на https://fakestoreapi.com.
Запросите у пользователя, товары какой категории он желает просмотреть.
Выведите информацию о соответствующих товарах в отформатированном для чтения виде в консоль.
Используйте API https://fakestoreapi.com/docs.
'''
import requests

#Запрос категорий товаров с сайта
url = 'https://fakestoreapi.com/products/categories'
response = requests.get(url).json()
print('На сайте "https://fakestoreapi.com" имеются следующие категории товаров:')

#Демонстрация пользователю списка категорий товаров сайта
for count,value in enumerate(response):
    print(count+1,value)

#Запрос выбора кактегории товаров у пользователя (с некоторой защитой от "дурака")
result = False
while not result:
    value = int(input('\nВведите номер желаемой категории товаров: '))
    if value < 1 or value > len(response):
        print('Введен неверный номер пункта')
    else:
        result = True
value-=1 #т.к. в меню сайта нумерация объектов начинается с 0-ля

#показ пользователю подробного списка товаров выбранной им категории
print(f'В категории "{response[value]}" имеются следующие категории товаров:\n')
url = 'https://fakestoreapi.com/products/category/'+response[value]
response = requests.get(url).json()
for item in response:
    print(f'Код товара: {item["id"]}\nНаименование: {item["title"]}\nЦена: {item["price"]}\nОписание: {item["description"]}\nСсылка на фото товара: {item["image"]}\nРейтинг товара: {item["rating"]["rate"]}\nВ наличии (кол-во,шт.): {item["rating"]["count"]}\n')
