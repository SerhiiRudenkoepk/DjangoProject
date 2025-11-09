from django.apps import AppConfig


class ShopConfig(AppConfig):
    
    # 2 attributes: default_auto_field and name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
