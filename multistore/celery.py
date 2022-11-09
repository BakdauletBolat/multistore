import os

from celery import Celery,Task
from celery.app.registry import TaskRegistry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multistore.settings')

app = Celery('multistore')

app.config_from_object('django.conf:settings', namespace='CELERY')







app.autodiscover_tasks()


class Hello(Task):
    queue = 'hipri'

    def run(self, to):
        return 'hello {0}'.format(to)
