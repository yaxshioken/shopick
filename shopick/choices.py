from click import Choice
from django.db.models import TextChoices


class SizeChoice(TextChoices):
    NONE = "", "None"
    SMALL = 'small', "Small"
    MEDIUM = 'medium', "Medium"
    LARGE = 'large', "Large"


class ColorChoice(TextChoices):
    NONE = '', 'None'
    RED = 'red', "Red"
    GREEN = 'green', "Green"
    YELLOW = 'yellow', "Yellow"
    BLUE = 'blue', "Blue"
    PURPLE = 'purple', "Purple"
    PINK = 'pink', "Pink"
    WHITE = 'white', "White"
    BLACK = 'black', "Black"


class NotificationChoice(TextChoices):
    PRODUCT = "product", 'Product'
    CHAT_MESSAGE = "chat message", 'Chat message'
    OTHER = "other", 'Other'
