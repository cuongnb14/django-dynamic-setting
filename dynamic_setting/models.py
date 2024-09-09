from django.core.exceptions import ValidationError
from django.db import models

class DynamicSetting(models.Model):

    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True, default=None)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = (
            ('name', 'category',)
        )

    def clean(self):
        self.validate_value()

    def validate_value(self):
        from .settings_registry import settings_registry

        self.value = str(self.value).strip()
        settings_class = settings_registry.get_class(self.category)
        settings_field = getattr(settings_class, self.name)
        try:
            settings_field.validate(self.value)
        except Exception as e:
            raise ValidationError(str(e))

    def save(self, *args, **kwargs):
        self.validate_value()
        super().save(*args, **kwargs)
