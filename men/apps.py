from django.apps import AppConfig


class MenConfig(AppConfig):
    name = 'men'
    verbose_name = 'People of this world'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'