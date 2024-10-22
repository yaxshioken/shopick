from django.db.models import TextChoices


class SizeChoice(TextChoices):
    NONE = "", "None"
    SMALL = "small", "Small"
    MEDIUM = "medium", "Medium"
    LARGE = "large", "Large"


class ColorChoice(TextChoices):
    NONE = "", "None"
    RED = "red", "Red"
    GREEN = "green", "Green"
    YELLOW = "yellow", "Yellow"
    BLUE = "blue", "Blue"
    PURPLE = "purple", "Purple"
    PINK = "pink", "Pink"
    WHITE = "white", "White"
    BLACK = "black", "Black"
class BrandChoice(TextChoices):
    NONE = "", "None"
    NIKE = 'NIKE', 'Nike'
    ADIDAS = 'ADIDAS', 'Adidas'
    PUMA = 'PUMA', 'Puma'
    UNDER_ARMOUR = 'UNDER_ARMOUR', 'Under Armour'
    REEBOK = 'REEBOK', 'Reebok'
    HM = 'H&M', 'H&M'
    ZARA = 'ZARA', 'Zara'
    UNIQLO = 'UNIQLO', 'Uniqlo'
    LEVI_STRAUSS = 'LEVI_STRAUSS', 'Levi Strauss'
    GAP = 'GAP', 'Gap'