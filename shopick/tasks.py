from django.db.models import Q

from config.celery import app


@app.task(bind=True, ignore_result=True)
def create_notification_for_users(self, product_id):

    from shopick.choices import NotificationChoice
    from shopick.models import Notifications, Product, User

    instance = Product.objects.get(id=product_id)
    users = User.objects.all()
    notes = []
    for user in users:
        n = Notifications(
            message=str(instance.name+"\n "+instance.description),
            type=NotificationChoice.PRODUCT,
            account=user,
            url=instance.build_url,
        )
        notes.append(n)

    Notifications.objects.bulk_create(notes)
