# Тестовая отработка методики грязный файл
# Решил оставить его здесть для ознакомления
# и возможного использования программы c sql lite
import json
import sqlite3

# requestusersmango.mangoRequest()

# Открываем файл mango_users.json в котором ответ на запрос
# из файла requestusersmango и записываем его в переменную response
with open('mango_users.json', 'r') as file:
    response = json.load(file)
# Подключаемся к базе данных SQL
conndb = sqlite3.connect(r'mango_users.db')
cur = conndb.cursor()
# Очищаем таблицы telephone и regions_phone
cur.execute("DELETE FROM telephone;")
cur.execute("DELETE FROM regions_phone;")
# Запускаем цикл по переменной response


for general in response['users']:
    # print (type(general['telephony']['extension']))
    ss = ()
    try:
        ss = general['telephony']['numbers'][1]['number']
        if ss.find("vpbx400013576.mangosip.ru") != -1:
            ss = 'НЕТ'
    except IndexError:
        ss = 'НЕТ'
    # Вычленяем Номера относящиеся к регионам без представительств
    # и сразу кладём в таблицу regions_phone
    if int(general['telephony']['extension']) % 1000 == 0:
        regions = general['general']['name'], general['telephony']['extension'], general['telephony']['outgoingline']
        cur.executemany("INSERT INTO regions_phone VALUES(NULL, ?, ?, ?);", (regions,))
        continue
    # Если кокое-то значение пустое записываем в него none
    if general['general']['email'] == '':
        general['general']['email'] = 'НЕТ'
    if general['general']['department'] == '':
        general['general']['department'] = 'НЕТ'
    if general['general']['position'] == '':
        general['general']['position'] = 'НЕТ'
    # создаем кортеж users из необходимых данных
    users = general['general']['name'], general['general']['email'], general['general']['department'], \
            general['general']['position'], general['telephony']['extension'], ss
    print(users)
    # Записываем в SQL
    cur.executemany("INSERT INTO telephone VALUES(NULL, ?, ?, ?, ?, ?, ?);", (users,))
# Закрываем соединение с SQL DB
conndb.commit()
