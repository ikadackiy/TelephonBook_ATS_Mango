import datetime
import config


# Лог для отслеживания выполнения cron задания
def log_cron():
    with open(config.system['WORK_DIRECTORY'] + 'log.txt', 'a') as outFile:
        outFile.write('\n{0}'.format(str(datetime.datetime.now())))