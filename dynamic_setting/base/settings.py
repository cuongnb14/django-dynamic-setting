class Settings:

    def __init__(self):
        from ..models import DynamicSetting
        dynamic_settings = DynamicSetting.objects.filter(category=self.Meta.name).values('name', 'value')
        dynamic_settings = {x['name']: x['value'] for x in dynamic_settings}
        self.validate(dynamic_settings)

    @classmethod
    def get_name(cls):
        return cls.Meta.name

    @classmethod
    def get_setting_fields(cls):
        # move to local var for optimize performance
        _getattr = getattr
        properties = {
            attr: _getattr(cls, attr) for attr in dir(cls) if
            not callable(_getattr(cls, attr)) and not attr.startswith("__")
        }
        return properties

    def validate(self, dynamic_settings):
        # move to local var for optimize performance
        _setattr = setattr
        for field_name, field in self.get_setting_fields().items():
            value = field.validate(dynamic_settings[field_name])
            setattr(self, field_name, value)

    class Meta:
        name = None
