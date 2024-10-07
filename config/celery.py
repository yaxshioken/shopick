import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("shopick_project")


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = "redis://localhost:6379/0"
# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = "redis://localhost:6379/0"
app.conf.timezone = "Asia/Tashkent"
app.conf.beat_schedule = {
    "send-sms-every-day-at-18": {
        "task": "apps.account.tasks.mark_as_read_lastweek_notifications",
        "schedule": crontab(minute=38, hour=17),
    },
    # Load task modules from all registered Django apps.
}
app.autodiscover_tasks()
