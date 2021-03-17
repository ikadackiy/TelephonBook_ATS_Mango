import mysql_creating_db
import request_users_mango
import from_mysql_parsing
import cron_job


# простенькое меню для установки всего необходимого
def main():
    while True:
        # Запуск напоминания о необходимости заполнить конфиг файл
        if not menu_warning():
            break
        print("Начинаем установку!")
        # Создаем таблицы
        if mysql_creating_db.user_question():
            continue
        # Запрос к API
        if not menu_request():
            break
        # Парсинг из манговского json и запись а SQL
        if not menu_pars_and_write_to_db():
            break
        # Парсинг из своего json и запись а SQL
        if not menu_local_pars_and_write_to_db():
            break
        if not cron_tassks():
            break
        break


def menu_warning():
    while True:
        print("""ПРЕДУПРЕЖДЕНИЕ! Перед выполнением скрипта проверьте корректность
        зполнения файла config. Данные скрипт следует выполнить ОДИН РАЗ!""")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ВЫ ВЫПОЛНИЛИ ВСЕ ПОДГОТОВИТЕЛЬНЫЕ ЭТАПЫ?")
        user_warning_input = input()
        if user_warning_input == 'y' or user_warning_input == 'n':
            if user_warning_input == 'y':
                warning_return = True
                break
            else:
                print("ОПЕРАЦИЯ ПРЕРВАНА!")
                warning_return = False
                break
        else:
            print('Ошибка ввода')
    return warning_return


def menu_request():
    while True:
        print("Отправить запрос в МангоТелеком?")
        user_request_input = input()
        if user_request_input == 'y' or user_request_input == 'n':
            if user_request_input == 'y':
                request_menu_return = True
                print("Отправляем запрос в МангоТелеком")
                request_users_mango.mango_json_write()
                break
            else:
                request_menu_return = False
                break
        else:
            print('Ошибка ввода')
    return request_menu_return


def menu_pars_and_write_to_db():
    while True:
        print("Записть данные из запроса в mySQL DB?")
        user_write_input = input()
        if user_write_input == 'y' or user_write_input == 'n':
            if user_write_input == 'y':
                menu_pars_and_write_to_db_return = True
                from_mysql_parsing.json_parsing_to_mysql()
                break
            else:
                menu_pars_and_write_to_db_return = False
                break
        else:
            print('Ошибка ввода')
    return menu_pars_and_write_to_db_return


def menu_local_pars_and_write_to_db():
    while True:
        print("Записть данные из локального json в mySQL DB?")
        user_write_local_input = input()
        if user_write_local_input == 'y' or user_write_local_input == 'n':
            if user_write_local_input == 'y':
                menu_local_pars_and_write_to_db_return = True
                from_mysql_parsing.json_local_users_parsing_to_mysql()
                break
            else:
                menu_local_pars_and_write_to_db_return = False
                break
        else:
            print('Ошибка ввода')
    return menu_local_pars_and_write_to_db_return


def cron_tassks():
    while True:
        print("Создать задание CRONTAB?")
        user_cron_input = input()
        if user_cron_input == 'y' or user_cron_input == 'n':
            if user_cron_input == 'y':
                menu_user_cron_input_return = True
                cron_job.cron_job()
                break
            else:
                menu_user_cron_input_return = False
                break
        else:
            print('Ошибка ввода')
    return menu_user_cron_input_return


if __name__ == '__main__':
    main()