import logging

from .models import DynamicSetting
from .settings_registry import settings_registry

logger = logging.getLogger(__name__)


def init_setting_if_not_exist():
    for settings in settings_registry.list_item():
        category = settings.get_name()
        for field_name, field in settings.get_setting_fields().items():
            _, created = DynamicSetting.objects.get_or_create(
                category=category,
                name=field_name,
                defaults={
                    'value': field.default,
                    'description': field.description,
                    'is_public': field.is_public,
                }
            )
            if created:
                logger.info(f'Created setting: {category} - {field_name}')
