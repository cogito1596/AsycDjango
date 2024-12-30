from celery import shared_task
# Create your views here.


@shared_task
def sharedtask():
    return "Hello World"
