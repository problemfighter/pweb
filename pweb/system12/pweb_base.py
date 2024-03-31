import os
from flask import Flask


class PWebBase(Flask):
    IS_WSGI_SERVER = False

    def is_app_loaded(self):
        print(f"IS_WSGI_SERVER : {PWebBase.IS_WSGI_SERVER}")
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            return True
        return False
