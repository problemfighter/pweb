import os
from flask import Flask


class PWebBase(Flask):

    def is_app_loaded(self):
        env = os.environ.get('env', 'Local')
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true" or env.lower() == "prod":
            return True
        return False
