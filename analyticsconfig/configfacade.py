from analyticsconfig.facades import DynaconfSecretsFacade, DynaconfSettingsFacade

class ConfigFacade:
    # environment_prefix = "ANALYTICSCONFIG"
    # env_switcher = "ENV_ANALYTICSCONFIG"
    environment = "default"

    def __init__(self, secrets_backend=None, settings_backend=None):
        self.secrets_backend = secrets_backend or DynaconfSecretsFacade()
        self.settings_backend = settings_backend or DynaconfSettingsFacade()

    def get_secret(self, key: str, environment: str = None, default: str = None):
        return self.secrets_backend.get_secret(key=key, environment=environment, default=default)

    def get_setting(self, key: str, environment: str = None, default: str = None):
        return self.settings_backend.get_setting(key=key, environment=environment, default=default)

    def set_secret(self, key: str, value, environment: str = None):
        return self.secrets_backend.set_secret(key=key, value=value, environment=environment)

    def set_setting(self, key: str, value, environment: str = None):
        return self.settings_backend.set_settings(key=key, value=value, environment=environment)




