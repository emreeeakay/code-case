from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .getData import getDataProcess


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getDataProcess, 'interval', seconds=5)
    scheduler.start()
