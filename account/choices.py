
from django.db.models import TextChoices


class NotificationChoice(TextChoices):
    PRODUCT = "product", "Product"
    CHAT_MESSAGE = "chat message", "Chat message"
    OTHER = "other", "Other"


class PaymentTypeChoice(TextChoices):
    USD = "usd", "USD"
    UZS = "uzs", "UZS"
    EUR = "eur", "EUR"


class PaymentStatusChoice(TextChoices):
    SUCCESS = "success", "Success"
    FAIL = "fail", "Fail"
    WAITING = "waiting", "Waiting"
    WRONG = "wrong", "Wrong"
    REJECTED = "rejected", "Rejected"
    REQUEUED = "requested", "Requested"
