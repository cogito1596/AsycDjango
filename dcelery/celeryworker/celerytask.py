from celery import Celery

app = Celery("celerytask")
app.config_from_object("celeryconfig", namespace="CELERY")
