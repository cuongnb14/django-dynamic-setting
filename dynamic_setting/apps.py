from django.apps import AppConfig


class DynamicSettingConfig(AppConfig):
    name = 'dynamic_setting'
    verbose_name = "Settings"

    def ready(self):
        pass
