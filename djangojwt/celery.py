from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'test1.setting')
app = Celery('test1')
app.config_from_object('django.conf:setting', namespace ='CELERY')
app.autodiscover_task()