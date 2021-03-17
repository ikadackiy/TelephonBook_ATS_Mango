# файл для автоматического обновления всех данных
# припомощи crontab задания

import time
import request_users_mango
import from_mysql_parsing
import log_cron

request_users_mango.mango_json_write()
time.sleep(10)
from_mysql_parsing.json_parsing_to_mysql()
time.sleep(10)
from_mysql_parsing.json_local_users_parsing_to_mysql()
time.sleep(10)
log_cron.log_cron()
exit()
