from mysql.connector import connect, Error
import mysql.connector
import config
import json


# Очищаем таблицы созданные нами таблицы перед заполнением или перезаписью
def mysql_clear_table():
    try:
        with connect(
                host=config.mysql_dict['HOST'],
                user=config.mysql_dict['USER_NAME'],
                password=config.mysql_dict['PASSWORD'],
                database=config.mysql_dict['DB_NAME']
        ) as connection:
            drop_tables_store = "TRUNCATE TABLE store"
            drop_tables_sales = "TRUNCATE TABLE sales"
            drop_tables_purchasing = "TRUNCATE TABLE purchasing"
            drop_tables_prog1c = "TRUNCATE TABLE prog1c"
            drop_tables_production = "TRUNCATE TABLE production"
            drop_tables_management = "TRUNCATE TABLE management"
            drop_tables_it = "TRUNCATE TABLE it"
            drop_tables_hr = "TRUNCATE TABLE hr"
            drop_tables_accounting = "TRUNCATE TABLE accounting"
            drop_tables_none_class = "TRUNCATE TABLE none_class"
            drop_tables_marketing = "TRUNCATE TABLE marketing"
            drop_tables_regions_phone = "TRUNCATE TABLE regions_phone"
            drop_tables_regions_spb = "TRUNCATE TABLE spb"
            drop_tables_regions_ekb = "TRUNCATE TABLE ekb"
            drop_tables_regions_krs = "TRUNCATE TABLE krs"
            drop_tables_executive = "TRUNCATE TABLE executive"
            drop_tables_transport = "TRUNCATE TABLE transport"
            drop_tables_production_led = "TRUNCATE TABLE production_led"
            drop_tables_web = "TRUNCATE TABLE web"
            drop_tables_drivers = "TRUNCATE TABLE drivers"
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_web)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_drivers)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_production_led)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_executive)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_transport)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_store)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_sales)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_purchasing)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_prog1c)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_production)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_management)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_it)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_hr)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_accounting)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_none_class)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_marketing)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_regions_phone)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_regions_spb)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_regions_ekb)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_regions_krs)
    except Error as e:
        print(f'Ошибка!!!{e}')


# Парсим полученый от API Json в mysql
def json_parsing_to_mysql():
    mysql_clear_table()
    # Открываем файл mango_users.json в котором ответ на запрос
    # из файла request_users_mango и записываем его в переменную response
    with open(config.system['WORK_DIRECTORY'] + 'mango_users.json', 'r') as file:
        response = json.load(file)
    # Подключаемся к базе данных SQL
    conndb = mysql.connector.connect(
        host=config.mysql_dict['HOST'],
        user=config.mysql_dict['USER_NAME'],
        password=config.mysql_dict['PASSWORD'],
        database=config.mysql_dict['DB_NAME'])
    cur = conndb.cursor()
    # Запускаем цикл по переменной response
    for general in response['users']:
        # Переменная для хранения мобильного телефона general['telephony']['numbers'][1]['number']
        # try используется для обхода ошибки индекса в случае
        # если general['telephony']['numbers'][1]['number'] не существует
        try:
            # Делаем выборку мобильных из json
            mobile = general['telephony']['numbers'][1]['number']
            # Проверка на случай если место мобильного записана сип учетка
            # записываем место него НЕТ
            if mobile.find("mangosip.ru") != -1:
                mobile = 'НЕТ'
        except IndexError:
            mobile = 'НЕТ'
        # Вычленяем Номера относящиеся к регионам без представительств
        # и сразу кладём в таблицу regions_phone
        if int(general['telephony']['extension']) % 1000 == 0:
            regions = general['general']['name'], general['telephony']['extension'], \
                      general['telephony']['outgoingline']
            regions_phone = "INSERT INTO regions_phone VALUES (NULL, %s, %s, %s)"
            cur.executemany(regions_phone, (regions,))
            continue
        # Если какое-то значение пустое записываем в него НЕТ
        # Сделано скорее для того чтобы привести в соответствие данные в АТС
        if general['general']['email'] == '':
            general['general']['email'] = 'НЕТ'
        if general['general']['department'] == '':
            general['general']['department'] = 'НЕТ'
        if general['general']['position'] == '':
            general['general']['position'] = 'НЕТ'
        # проверяем соответствие принадлежности к тому или иному отделу
        # создаем кортеж из необходимых данных и записываем в SQL
        if general['general']['department'] == 'Производство':
            production = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            production_table = "INSERT INTO production VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(production_table, (production,))
        if general['general']['department'] == 'Управление':
            management = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            management_table = "INSERT INTO management VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(management_table, (management,))
        if general['general']['department'] == 'Отдел продаж':
            sales = general['general']['name'], general['general']['email'], general['general']['department'], \
                    general['general']['position'], general['telephony']['extension'], mobile
            sales_table = "INSERT INTO sales VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(sales_table, (sales,))
        if general['general']['department'] == 'Склад':
            store = general['general']['name'], general['general']['email'], general['general']['department'], \
                    general['general']['position'], general['telephony']['extension'], mobile
            store_table = f"INSERT INTO store VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(store_table, (store,))
        if general['general']['department'] == 'Бухгалтерия':
            accounting = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            accounting_table = "INSERT INTO accounting VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(accounting_table, (accounting,))
        if general['general']['department'] == 'IT отдел':
            it = general['general']['name'], general['general']['email'], general['general']['department'], \
                 general['general']['position'], general['telephony']['extension'], mobile
            it_table = "INSERT INTO it VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(it_table, (it,))
        if general['general']['department'] == 'Отдел кадров':
            hr = general['general']['name'], general['general']['email'], general['general']['department'], \
                 general['general']['position'], general['telephony']['extension'], mobile
            hr_table = "INSERT INTO hr VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(hr_table, (hr,))
        if general['general']['department'] == 'Разработка 1с':
            prog1c = general['general']['name'], general['general']['email'], general['general']['department'], \
                     general['general']['position'], general['telephony']['extension'], mobile
            prog1c_table = "INSERT INTO prog1c VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(prog1c_table, (prog1c,))
        if general['general']['department'] == 'Отдел закупок':
            purchasing = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            purchasing_table = "INSERT INTO purchasing VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(purchasing_table, (purchasing,))
        if general['general']['department'] == 'СПБ':
            spb = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            spb_table = "INSERT INTO spb VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(spb_table, (spb,))
        if general['general']['department'] == 'ЕКБ':
            ekb = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            ekb_table = "INSERT INTO ekb VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(ekb_table, (ekb,))
        if general['general']['department'] == 'КРС':
            krs = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            krs_table = "INSERT INTO krs VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(krs_table, (krs,))
        if general['general']['department'] == 'Исполнительный отдел':
            isp = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            isp_table = "INSERT INTO executive VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(isp_table, (isp,))
        if general['general']['department'] == 'Транспортный отдел':
            tran = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            tran_table = "INSERT INTO transport VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(tran_table, (tran,))
        if general['general']['department'] == 'Светодиодное производство':
            led = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            led_table = "INSERT INTO production_led VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(led_table, (led,))
        if general['general']['department'] == 'Водители':
            drivers = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            drivers_table = "INSERT INTO drivers VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(drivers_table, (drivers,))
        if general['general']['department'] == 'WEB разработка':
            web = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            web_table = "INSERT INTO web VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(web_table, (web,))
        if general['general']['department'] == 'НЕТ':
            none_class = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            none_class_table = "INSERT INTO none_class VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(none_class_table, (none_class,))
            continue
    # Закрываем соединение с SQL DB
    if cur.close():
        print(f'Парсинг и запись в Базу прошли успешно!')
    conndb.commit()


# на случай парсинга самописного json
def json_local_users_parsing_to_mysql():
    # Открываем файл local_users.json файл созданный нашими руками
    # и записываем его в переменную response
    with open(config.system['WORK_DIRECTORY'] + 'local_users.json', 'r', encoding='utf-8') as file:

        response = json.load(file)
    # Подключаемся к базе данных SQL
    conndb = mysql.connector.connect(
        host=config.mysql_dict['HOST'],
        user=config.mysql_dict['USER_NAME'],
        password=config.mysql_dict['PASSWORD'],
        database=config.mysql_dict['DB_NAME'])
    cur = conndb.cursor()
    # Запускаем цикл по переменной response
    for general in response['users']:
        # Переменная для хранения мобильного телефона general['telephony']['numbers'][1]['number']
        # try используется для обхода ошибки индекса в случае
        # если general['telephony']['numbers'][1]['number'] не существует
        try:
            # Делаем выборку мобильных из json
            mobile = general['telephony']['numbers'][1]['number']
            # Проверка на случай если место мобильного записана сип учетка
            # записываем место него НЕТ
            if mobile.find("mangosip.ru") != -1:
                mobile = 'НЕТ'
        except IndexError:
            mobile = 'НЕТ'
        # Если какое-то значение пустое записываем в него НЕТ
        if general['general']['email'] == '':
            general['general']['email'] = 'НЕТ'
        if general['general']['department'] == '':
            general['general']['department'] = 'НЕТ'
        if general['general']['position'] == '':
            general['general']['position'] = 'НЕТ'
        # проверяем соответствие принадлежности к тому или иному отделу
        # создаем кортеж из необходимых данных и записываем в SQL
        if general['general']['department'] == 'Производство':
            production = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            production_table = "INSERT INTO production VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(production_table, (production,))
        if general['general']['department'] == 'Управление':
            management = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            management_table = "INSERT INTO management VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(management_table, (management,))
        if general['general']['department'] == 'Отдел продаж':
            sales = general['general']['name'], general['general']['email'], general['general']['department'], \
                    general['general']['position'], general['telephony']['extension'], mobile
            sales_table = "INSERT INTO sales VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(sales_table, (sales,))
        if general['general']['department'] == 'Склад':
            store = general['general']['name'], general['general']['email'], general['general']['department'], \
                    general['general']['position'], general['telephony']['extension'], mobile
            store_table = "INSERT INTO store VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(store_table, (store,))
        if general['general']['department'] == 'Бухгалтерия':
            accounting = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            accounting_table = "INSERT INTO accounting VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(accounting_table, (accounting,))
        if general['general']['department'] == 'IT отдел':
            it = general['general']['name'], general['general']['email'], general['general']['department'], \
                 general['general']['position'], general['telephony']['extension'], mobile
            it_table = "INSERT INTO it VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(it_table, (it,))
        if general['general']['department'] == 'Отдел кадров':
            hr = general['general']['name'], general['general']['email'], general['general']['department'], \
                 general['general']['position'], general['telephony']['extension'], mobile
            hr_table = "INSERT INTO hr VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(hr_table, (hr,))
        if general['general']['department'] == 'Разработка 1с':
            prog1c = general['general']['name'], general['general']['email'], general['general']['department'], \
                     general['general']['position'], general['telephony']['extension'], mobile
            prog1c_table = "INSERT INTO prog1c VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(prog1c_table, (prog1c,))
        if general['general']['department'] == 'Отдел закупок':
            purchasing = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            purchasing_table = "INSERT INTO purchasing VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(purchasing_table, (purchasing,))
        if general['general']['department'] == 'СПБ':
            spb = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            spb_table = "INSERT INTO spb VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(spb_table, (spb,))
        if general['general']['department'] == 'ЕКБ':
            ekb = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            ekb_table = "INSERT INTO ekb VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(ekb_table, (ekb,))
        if general['general']['department'] == 'КРС':
            krs = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            krs_table = "INSERT INTO krs VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(krs_table, (krs,))
        if general['general']['department'] == 'Исполнительный отдел':
            isp = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            isp_table = "INSERT INTO executive VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(isp_table, (isp,))
        if general['general']['department'] == 'Транспортный отдел':
            tran = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            tran_table = "INSERT INTO transport VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(tran_table, (tran,))
        if general['general']['department'] == 'Светодиодное производство':
            led = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            led_table = "INSERT INTO production_led VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(led_table, (led,))
        if general['general']['department'] == 'Водители':
            drivers = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            drivers_table = "INSERT INTO drivers VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(drivers_table, (drivers,))
        if general['general']['department'] == 'WEB разработка':
            web = general['general']['name'], general['general']['email'], general['general']['department'], \
                  general['general']['position'], general['telephony']['extension'], mobile
            web_table = "INSERT INTO web VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(web_table, (web,))
        if general['general']['department'] == 'НЕТ':
            none_class = general['general']['name'], general['general']['email'], general['general']['department'], \
                         general['general']['position'], general['telephony']['extension'], mobile
            none_class_table = "INSERT INTO none_class VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            cur.executemany(none_class_table, (none_class,))
            continue
    # Закрываем соединение с SQL DB
    if cur.close():
        print(f'Парсинг и запись в Базу своего файла json прошли успешно!')
    conndb.commit()

