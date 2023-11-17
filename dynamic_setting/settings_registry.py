class Registry:

    def __init__(self):
        self._registry = {}

    def register(self, item_class):
        if item_class.get_name() in self._registry:
            raise Exception(f'Item class {item_class.get_name()} already registered')
        self._registry[item_class.get_name()] = item_class

    def get_class(self, name):
        item_class = self._registry.get(name)
        if not item_class:
            raise Exception(f'Not found item {name} in registry')
        return item_class

    def get(self, name, *args, **kwargs):
        item_class = self._registry.get(name)
        if item_class:
            return item_class(*args, **kwargs)
        return None

    def list_name(self):
        return sorted(self._registry.keys())

    def list_item(self):
        return self._registry.values()


settings_registry = Registry()
