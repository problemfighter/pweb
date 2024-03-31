import os
from flask import Flask


class PWebBase(Flask):
    _is_run_on_wsgi = False

    def is_app_loaded(self):
        print("?????????????????????")
        print(os.environ)
        IS_WSGI = os.environ.get("IS_WSGI")
        print(f"IS_WSGI {IS_WSGI}")
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true" or self._is_run_on_wsgi:
            return True
        return False
