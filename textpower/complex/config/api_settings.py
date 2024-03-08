import threading


class ApiSettings:
    def __init__(self, data=None):
        self.data = {} if data is None else data

    def __getitem__(self, key):
        return self.get(key)

    def get_config(self, key):
        keys = key.split(".")
        result = self.data
        for k in keys:
            result = result.get(k, {})
        return result

    def __setitem__(self, key, value):
        self.set(key, value)

    def set_config(self, key, value):
        keys = key.split(".")
        current = self.data
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value

    def to_dict(self):
        return self.data


api_settings = threading.local()
api_settings.config = ApiSettings()


def set_config(key, value):
    api_settings.config.set_config(key, value)


def get_config(key):
    return api_settings.config.get_config(key)


def get_config_dict():
    return api_settings.config.data


def init_config(data):
    api_settings.config = ApiSettings(data)
