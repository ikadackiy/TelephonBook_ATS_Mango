from mysql.connector import connect, Error
import config

# Подключение к БД с проверкой


def mysql_connection():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            return connection
    except Error as e:
        print(f'Ошибка!!!{e}')


# Создание своей базы данных mango_users
def mysql_create_database():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            create_db_mango_users = "CREATE DATABASE mango_users"
            with connection.cursor() as cursor:
                cursor.execute(create_db_mango_users)
                print('База успешно создана!')
    except Error as e:
        print(f'Ошибка!!!{e}')


# Создание таблиц в своей базе данных mango_users
def mysql_create_table():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
            database="mango_users"
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            create_table_management = """
            CREATE TABLE management (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_sales = """
            CREATE TABLE sales (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_store = """
            CREATE TABLE store (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_production = """
            CREATE TABLE production (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_accounting = """
            CREATE TABLE accounting (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_purchasing = """
            CREATE TABLE purchasing (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_regions_phone = """
            CREATE TABLE regions_phone (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (30),
                extension CHAR (10),
                mobile CHAR (15)
            )
            """
            create_table_hr = """
            CREATE TABLE hr (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_it = """
            CREATE TABLE it (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_prog1c = """
            CREATE TABLE prog1c (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_spb = """
            CREATE TABLE spb (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_ekb = """
            CREATE TABLE ekb (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_krs = """
            CREATE TABLE krs (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_none_class = """
            CREATE TABLE none_class (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_marketing = """
            CREATE TABLE marketing (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_transport = """
            CREATE TABLE transport (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_executive = """
            CREATE TABLE executive (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_drivers = """
            CREATE TABLE drivers (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_web = """
            CREATE TABLE web (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_production_led = """
            CREATE TABLE production_led (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_table_management)
            with connection.cursor() as cursor:
                cursor.execute(create_table_drivers)
            with connection.cursor() as cursor:
                cursor.execute(create_table_production_led)
            with connection.cursor() as cursor:
                cursor.execute(create_table_web)
            with connection.cursor() as cursor:
                cursor.execute(create_table_sales)
                # print('Таблица Продажи успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_store)
                # print('Таблица Склад успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_production)
                # print('Таблица Производство успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_accounting)
                # print('Таблица Бухгалтерия успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_purchasing)
                # print('Таблица Закупки успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_it)
                # print('Таблица IT успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_prog1c)
                # print('Таблица 1c успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_hr)
                # print('Таблица Кадры успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_none_class)
                # print('Таблица Для не категоризированых успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_marketing)
                # print('Таблица Маркетинг успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_transport)
                # print('Таблица с для телефонов транспортный успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_executive)
                # print('Таблица с для телефонов исполнительный успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_spb)
                # print('Таблица с для телефонов СПБ успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_ekb)
                # print('Таблица с для телефонов ЕКБ успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_krs)
                # print('Таблица с для телефонов КРС успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_regions_phone)
                print('Все таблицы успешно созданы!')
    except Error as e:
        print(f'Ошибка!!!{e}')


# Создание таблиц в существующей DB см. config 'DB_NAME': 'test_db'
def mysql_create_table_old_db():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
            database=config.mysql_dict['DB_NAME']
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            create_table_management = """
            CREATE TABLE management (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_sales = """
            CREATE TABLE sales (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_store = """
            CREATE TABLE store (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_production = """
            CREATE TABLE production (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_accounting = """
            CREATE TABLE accounting (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_purchasing = """
            CREATE TABLE purchasing (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
                )
                """
            create_table_regions_phone = """
            CREATE TABLE regions_phone (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (30),
                extension CHAR (10),
                mobile CHAR (15)
            )
            """
            create_table_hr = """
            CREATE TABLE hr (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_it = """
            CREATE TABLE it (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_prog1c = """
            CREATE TABLE prog1c (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_spb = """
            CREATE TABLE spb (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_ekb = """
            CREATE TABLE ekb (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_krs = """
            CREATE TABLE krs (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_none_class = """
            CREATE TABLE none_class (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_marketing = """
            CREATE TABLE marketing (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_transport = """
            CREATE TABLE transport (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_executive = """
            CREATE TABLE executive (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_drivers = """
            CREATE TABLE drivers (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_web = """
            CREATE TABLE web (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            create_table_production_led = """
            CREATE TABLE production_led (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name CHAR (150),
                email CHAR (200),
                department CHAR (150),
                position CHAR (150),
                extension CHAR (10),
                mobile CHAR (20)
            )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_table_management)
            with connection.cursor() as cursor:
                cursor.execute(create_table_drivers)
            with connection.cursor() as cursor:
                cursor.execute(create_table_production_led)
            with connection.cursor() as cursor:
                cursor.execute(create_table_web)
            with connection.cursor() as cursor:
                cursor.execute(create_table_sales)
                # print('Таблица Продажи успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_store)
                # print('Таблица Склад успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_production)
                # print('Таблица Производство успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_accounting)
                # print('Таблица Бухгалтерия успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_purchasing)
                # print('Таблица Закупки успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_it)
                # print('Таблица IT успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_prog1c)
                # print('Таблица 1c успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_hr)
                # print('Таблица Кадры успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_none_class)
                # print('Таблица Для не категоризированых успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_marketing)
                # print('Таблица Маркетинг успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_transport)
                # print('Таблица с для телефонов транспортный успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_executive)
                # print('Таблица с для телефонов исполнительный успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_spb)
                # print('Таблица с для телефонов СПБ успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_ekb)
                # print('Таблица с для телефонов ЕКБ успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_krs)
                # print('Таблица с для телефонов КРС успешно создана!')
            with connection.cursor() as cursor:
                cursor.execute(create_table_regions_phone)
                print('Все таблицы успешно созданы!')
    except Error as e:
        print(f'Ошибка!!!{e}')


# Удаление таблиц в существующей DB см. config 'DB_NAME': 'test_db'
def mysql_drop_tables_old_db():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
            database=config.mysql_dict['DB_NAME']
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            drop_tables_store = "DROP TABLE store"
            drop_tables_sales = "DROP TABLE sales"
            drop_tables_purchasing = "DROP TABLE purchasing"
            drop_tables_prog1c = "DROP TABLE prog1c"
            drop_tables_production = "DROP TABLE production"
            drop_tables_management = "DROP TABLE management"
            drop_tables_it = "DROP TABLE it"
            drop_tables_hr = "DROP TABLE hr"
            drop_tables_accounting = "DROP TABLE accounting"
            drop_tables_none_class = "DROP TABLE none_class"
            drop_tables_marketing = "DROP TABLE marketing"
            drop_tables_regions_phone = "DROP TABLE regions_phone"
            drop_tables_regions_spb = "DROP TABLE spb"
            drop_tables_regions_ekb = "DROP TABLE ekb"
            drop_tables_regions_krs = "DROP TABLE krs"
            drop_tables_executive = "DROP TABLE executive"
            drop_tables_transport = "DROP TABLE transport"
            drop_tables_production_led = "DROP TABLE production_led"
            drop_tables_web = "DROP TABLE web"
            drop_tables_drivers = "DROP TABLE drivers"
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_web)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_drivers)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_production_led)
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
                cursor.execute(drop_tables_executive)
            with connection.cursor() as cursor:
                cursor.execute(drop_tables_transport)
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
                print('Все таблицы успешно удалены!')
    except Error as e:
        print(f'Ошибка!!!{e}')


# Удаление своей базы данных mango_users
def mysql_drop_database():
    try:
        with connect(
            host=config.mysql_dict['HOST'],
            user=config.mysql_dict['USER_NAME'],
            password=config.mysql_dict['PASSWORD'],
            # database=config.mysql_dict['DB_NAME']
        ) as connection:
            # print(f'Подключение прошло успешно!!!{connection}')
            create_db_mango_users = "DROP DATABASE mango_users"
            with connection.cursor() as cursor:
                cursor.execute(create_db_mango_users)
                print('База успешно удалена!')
    except Error as e:
        print(f'Ошибка!!!{e}')


# Интерактив по скрипту
def user_question():
    print('создать новую базу данных с необходимыми таблицами? y/n')
    q_create_db = input()
    if q_create_db == 'y' or q_create_db == 'n':
        if q_create_db == 'y':
            mysql_create_database()
            mysql_create_table()
            print("База и таблицы успешно созданы!")
        if q_create_db == 'n':
            print('создать необходимые таблицы в существующей базе? y/n')
            q_create_table_old_db = input()
            if q_create_table_old_db == 'y' or q_create_table_old_db == 'n':
                if q_create_table_old_db == 'y':
                    mysql_create_table_old_db()
                    print("Таблицы успешно созданы!")
                if q_create_table_old_db == 'n':
                    print('Удалить созданные таблицы в вашей базе? y/n')
                    q_drop_tables = input()
                    if q_drop_tables == 'y' or q_drop_tables == 'n':
                        if q_drop_tables == 'y':
                            mysql_drop_tables_old_db()
                            print('Таблицы удалены!')
                            return True
                        if q_drop_tables == 'n':
                            print('Удалить созданую базу данных? y/n')
                            q_drop_db = input()
                            if q_drop_db == 'y' or q_drop_db == 'n':
                                if q_drop_db == 'y':
                                    mysql_drop_database()
                                    print('База данных успешно удалена!')
                                    return True
                                if q_drop_db == 'n':
                                    print("Выход из диалога")
                    else:
                        print('Ошибка ввода')
                        return True
            else:
                print('Ошибка ввода')
                return True
    else:
        print('Ошибка ввода')
        return True
