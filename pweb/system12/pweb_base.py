import os
from flask import Flask


class PWebBase(Flask):

    def is_app_loaded(self):
        IS_WSGI = os.environ.get("IS_WSGI")
        print(f"is_app_loaded IS_WSGI {IS_WSGI}")
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            return True
        return False
