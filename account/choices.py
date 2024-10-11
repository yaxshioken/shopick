from click import Choice
from django.db.models import TextChoices


class NotificationChoice(TextChoices):
    PRODUCT = "product", "Product"
    CHAT_MESSAGE = "chat message", "Chat message"
    OTHER = "other", "Other"
