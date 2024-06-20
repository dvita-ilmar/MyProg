import requests

url = 'https://api.vk.com/method/users.get?user_ids=743784474&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.199 HTTP/1.1'
response = requests.get(url)
