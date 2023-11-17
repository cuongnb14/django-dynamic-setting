from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from . import models


@admin.register(models.DynamicSetting)
class DynamicSettingAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'value', 'description', 'is_public', 'modified_at')
    list_display_links = ('name',)
    list_editable = ('value', 'is_public')
    list_filter = ('is_public', 'category')
    search_fields = ('name',)
    ordering = ('category', 'name')

    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }
