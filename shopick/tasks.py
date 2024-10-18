from account.choices import NotificationChoice
from account.models import Account, Notifications
from config.celery import app
from shopick.models import Product
from django.core.exceptions import ObjectDoesNotExist

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


from django.db import transaction


@app.task(bind=True, ignore_result=True)
def create_notification_for_users(self, product_id):
    try:
        instance = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        self.retry(countdown=60, exc=ObjectDoesNotExist("Product not found."))

    batch_size = 1000
    users = Account.objects.all()
    notes = []

    for i in range(0, users.count(), batch_size):
        batch_users = users[i:i + batch_size]
        for user in batch_users:
            n = Notifications(
                message=f"{instance.name}\n{instance.description}",
                type=NotificationChoice.PRODUCT,
                account=user,
                url=instance.build_url,
            )
            notes.append(n)

        Notifications.objects.bulk_create(notes)
        notes.clear()
