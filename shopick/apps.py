from django.apps import AppConfig


class ShopickConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shopick"

    def ready(self):
        import shopick.signals
