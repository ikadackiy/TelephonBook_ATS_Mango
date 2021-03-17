from crontab import CronTab
import config


# Создание задания для CRONTAB Linux
def cron_job():
    my_cron = CronTab(user=config.system['USER_NAME'])
    files = 'task_for_update.py'
    command = ('python3 ' + config.system['WORK_DIRECTORY'] + files)
    job = my_cron.new(command=command)
    job.setall(config.system['CRON_JOB'])
    my_cron.write()
