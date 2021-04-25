from django.apps import AppConfig


class BdAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bd_app'
    verbose_name = 'Тест БД'