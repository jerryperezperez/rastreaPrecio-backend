from flask_apscheduler import scheduler
from flask_apscheduler import APScheduler

@scheduler.task('interval', id='my_job', seconds=7)
def my_job():
        # ArticuloList.get()
        # print(funcionUtil(1))
        print('This job is executed every 10 seconds.')