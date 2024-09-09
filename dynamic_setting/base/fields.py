from .exceptions import SettingValueInvalid


class SettingField:
    def __init__(self, default=None, description=None, is_public=False):
        self.default = default
        self.description = description
        self.is_public = is_public
        self.value = None

    def validate(self, value):
        pass

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class CharSettingField(SettingField):
    def __init__(self, min_length=None, max_length=None, **kwargs):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(**kwargs)

    def validate(self, value):
        validated_value = str(value)
        len_value = len(validated_value)
        if self.min_length and len_value < self.min_length:
            raise SettingValueInvalid(f'This setting must have minimum {self.min_length} characters')
        if self.max_length and len_value > self.max_length:
            raise SettingValueInvalid(f'This setting must have maximum {self.max_length} characters')
        return validated_value


class IntegerSettingField(SettingField):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(**kwargs)

    def validate(self, value):
        try:
            validated_value = int(value)
        except ValueError:
            raise SettingValueInvalid(f'This setting must be a integer')

        if self.min_value and validated_value < self.min_value:
            raise SettingValueInvalid(f'This setting must have minimum value is {self.min_value}')
        if self.max_value and validated_value > self.max_value:
            raise SettingValueInvalid(f'This setting must have maximum value is {self.max_value}')
        return validated_value


class IntegerRangeSettingField(SettingField):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(**kwargs)

    def validate(self, value):
        try:
            parts = value.split(",")
            minv = int(parts[0])
            maxv = int(parts[1])
        except ValueError:
            raise SettingValueInvalid(f'This setting must be a integer')
        
        if minv > maxv:
            raise SettingValueInvalid(f'This setting must have min value <= max value')
        
        if self.min_value and minv < self.min_value:
            raise SettingValueInvalid(f'This setting must have minimum value is {self.min_value}')
        if self.max_value and maxv > self.max_value:
            raise SettingValueInvalid(f'This setting must have maximum value is {self.max_value}')
        return minv, maxv


class BooleanSettingField(SettingField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        if value not in ['0', '1']:
            raise SettingValueInvalid(f'This setting must have value is 0 or 1')
        validated_value = bool(int(value))
        return validated_value
