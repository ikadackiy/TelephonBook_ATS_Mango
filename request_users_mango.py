import hashlib
import json
import requests
import config


# Запрос в манго для получения списка пользователей
def mango_request():
    url = config.config_dict['URL']  # адрес для отправки json-запросов
    mango_api_key = config.config_dict['MANGO_API_KEY']  # данные авторизации
    mango_salt = config.config_dict['MANGO_SALT']
    # тело запроса
    mango_json = {}
    # генерируем подпись
    sha = (mango_api_key + json.dumps(mango_json) + mango_salt).encode('utf8')
    sign = hashlib.sha256(sha).hexdigest()
    # структура входных данных (словарь)
    data = {
        'vpbx_api_key': mango_api_key,
        'sign': sign,
        'json': json.dumps(mango_json)
    }
    # отправка запроса
    response = (requests.post(url, data=data))
    # вывести результат
    response = response.json()
    return response


# Запись в json файл пользователей
def mango_json_write():
    response = mango_request()
    with open(config.system['WORK_DIRECTORY'] + 'mango_users.json', 'w') as file:
        json.dump(response, file, indent=3)
    print('Запрос выполнен успешно!')
