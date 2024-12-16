# Django Dynamic Setting
Django Dynamic Setting is a Django app, designed to help you manage your project settings, storage settings in database, provided admin UI to manage there settings.

# Setup
```sh
pip install git+https://github.com/cuongnb14/django-dynamic-setting@master#egg=django-dynamic-setting
```

**Add to install app**
```python
INSTALLED_APPS = [
    ...
    "dynamic_setting",
    ...
]
```

**Run migrate**
```sh
python3 manage.py migrate
```


**Define setting in your code**
```python
# your_app/setting.py
from dynamic_setting.base.fields import IntegerSettingField, BooleanSettingField, CharSettingField
from dynamic_setting.base.settings import Settings


class BotSettings(Settings):

    sell_enable = BooleanSettingField(default=1, description='enable sell action')
    title = CharSettingField(default="hello", is_public=True)
    version = CharSettingField(default=1, min_value=0, max_value=10, is_public=True)

    class Meta:
        name = 'bot'

# your_app/apps.py
from django.apps import AppConfig
from dynamic_setting.settings_registry import settings_registry

from .setting import BotSettings


class BotConfig(AppConfig):
    name = "cg_bot.bot"
    verbose_name = "Bots"

    def ready(self):
        settings_registry.register(BotSettings)
```

**Init setting**
```sh
python3 manage.py init_dynamic_setting
```

**Usage**
```python
setting = BotSettings()
print(setting.title)
```

**Add API get list public setting**
```python
path("settings", DynamicSettingListAPIView.as_view(), name="setting_list"),
```
