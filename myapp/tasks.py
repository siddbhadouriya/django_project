from celery import shared_task
from .moduls import Student
import time

@shared_task
def create_student():
    time.sleep(100)
    Student.objects.create(name="student")
    print("student create.......")