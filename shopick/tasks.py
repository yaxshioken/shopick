from account.choices import NotificationChoice
from account.models import Account, Notifications
from config.celery import app
from shopick.models import Product


@app.task(bind=True, ignore_result=True)
def create_notification_for_users(self, product_id):

    instance = Product.objects.get(id=product_id)
    users = Account.objects.all()
    notes = []
    for user in users:
        n = Notifications(
            message=str(instance.name + "\n " + instance.description),
            type=NotificationChoice.PRODUCT,
            account=user,
            url=instance.build_url,
        )
        notes.append(n)

    Notifications.objects.bulk_create(notes)
