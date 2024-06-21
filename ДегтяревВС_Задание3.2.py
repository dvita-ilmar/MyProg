'''
Задание 3: Работа с API

Пример 2. Выведите информацию о всех корзинах пользователей (Cart), представленных на https://fakestoreapi.com.
Проанализируйте данные и устно ответьте на вопрос, что из себя представляют эти корзины и какая информация в них находится - 
что означает каждое поле в полученном json. 
* По желанию доработайте программу: запросите у пользователя его имя (или идентификатор), в соответствии с этим выведите содержание
 всех корзин этого пользователя в отформатированном для чтения виде в консоль. Используйте API https://fakestoreapi.com/docs. 
'''
import requests, datetime

#Запрос информации о всех корзинах пользователей (Cart)
url = 'https://fakestoreapi.com/carts'
responseCart = requests.get(url).json()

#Дополнительное задание - показать корзины выбранного пользователя
#Запрашиваем всех пользователей сайта
url = 'https://fakestoreapi.com/users'
responseUsers = requests.get(url).json()

#Показываем список пользователей
print('На сайте "https://fakestoreapi.com" обретаются следующие пользователи:\n(номер имя фамилия пользователя)')

#Демонстрация пользователю списка пользователей сайта
for item in responseUsers:
    print(f'{item["id"]} {item["name"]["firstname"]} {item["name"]["lastname"]}')

#Запрос выбора идентификатора пользователя у пользователя (с некоторой защитой от "дурака" - в отличие от примера 3.1
#здесь она не зависит от непрерывной числовой последовательности)
result = False
while not result:
    value = int(input('\nВведите номер пользователя, у которого желаете заглянуть в корзины товаров: '))
    for item in responseUsers:
        if value == item["id"]:
            user_first_name = item["name"]["firstname"]
            user_last_name = item["name"]["lastname"]
            result = True
            break       
    if not result:
        print('Введен неверный номер пользователя')

#Демонстрация содержимого корзин выбранного пользователя
print(f'У пользователя {user_first_name} {user_last_name} есть корзины со следующими товарами:')
for item in responseCart: #У пользователя может быть несколько корзин
    if item["userId"] == value:
        print(f'\nНомер корзины: {item["id"]}\nДата создания: {datetime.datetime.strptime(item["date"],"%Y-%m-%dT%H:%M:%S.%fZ")}\nВ корзине находятся следующие товары:')
        for itemProduct in item["products"]: #У пользователя может быть несколько товаров в корзине
            url = 'https://fakestoreapi.com/products/'+str(itemProduct["productId"])
            responseProduct = requests.get(url).json()
            print(f'- {responseProduct["title"]} - Цена: {responseProduct["price"]} - Количество: {itemProduct["quantity"]}')