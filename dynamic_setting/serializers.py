from rest_framework import serializers

from .models import DynamicSetting


class DynamicSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DynamicSetting
        fields = ('name', 'value')
