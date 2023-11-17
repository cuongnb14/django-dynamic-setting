from rest_framework import generics

from .models import DynamicSetting
from .serializers import DynamicSettingSerializer


class DynamicSettingListAPIView(generics.ListAPIView):

    queryset = DynamicSetting.objects.filter(is_public=True)
    serializer_class = DynamicSettingSerializer
    filterset_field = ('category',)
