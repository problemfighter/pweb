import os
from flask import Flask


class PWebBase(Flask):
    context_data_holder: dict = None

    def is_app_loaded(self):
        env = os.environ.get('runas', 'dev')
        print(f"Running as {env}")
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true" or env.lower() == "prod":
            return True
        return False

    def add_to_context_data(self, key, value):
        if not self.context_data_holder:
            self.context_data_holder = {}
        self.context_data_holder[key] = value
        return self

    def get_context_data(self, key: str, default=None):
        if self.context_data_holder and key in self.context_data_holder:
            return self.context_data_holder[key]
        return default
