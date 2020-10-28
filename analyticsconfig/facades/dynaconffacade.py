from collections import defaultdict

class DynaconfFacade:
    def __init__(self):
        pass

    def _get(self, key: str, environment: str = None, default: str = None):
        if environment:
            if key in self.cache[environment]:
                return self.cache[environment][key]
            return self.settings.from_env(environment).get(key, default)
        return self.settings.get(key, default)

    def _set(self, key: str, value, environment: str = None):
        if environment:
            self.cache[environment][key] = value
            return
        self.settings.set(key, value)

    # list

class DynaconfSettingsFacade(DynaconfFacade):
    def __init__(self):
        from dynaconf import Dynaconf
        self.settings = Dynaconf(settings_file=['settings.yaml'], environments=True)
        self.cache = defaultdict(dict)

    def get_setting(self, key: str, environment: str = None, default: str = None):
        return self._get(key=key, environment=environment, default=default)

    def set_setting(self, key: str, value, environment: str = None):
        return self._set(key=key, value=value, environment=environment)

class DynaconfSecretsFacade(DynaconfFacade):
    def __init__(self):
        from dynaconf import Dynaconf
        self.settings = Dynaconf(settings_file=['.secrets.yaml'], environments=True)
        self.cache = defaultdict(dict)

    def get_secret(self, key: str, environment: str = None, default: str = None):
        return self._get(key=key, environment=environment, default=default)

    def set_secret(self, key: str, value, environment: str = None):
        return self._set(key=key, value=value, environment=environment)