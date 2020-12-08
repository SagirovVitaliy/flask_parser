from celery import Celery

from webapp import create_app
from parser import avito_parser

from celery.schedules import crontab

flask_app = create_app()
celery_app = Celery('tasks_parser', broker='redis://localhost:6379/0')


@celery_app.task
def quantity_announcement():
    with flask_app.app_context():
        avito_parser()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour='*/1'), quantity_announcement.s())
