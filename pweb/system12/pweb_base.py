import os
from flask import Flask


class PWebBase(Flask):

    def is_app_loaded(self):
        print("IS_WSGI_SRV : " + str(self.config["IS_WSGI_SRV"]))
        if not self.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            return True
        return False
