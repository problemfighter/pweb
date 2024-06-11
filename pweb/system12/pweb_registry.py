from typing import Dict
from pweb.system12.pweb_base import PWebBase
from pweb.system12.pweb_interfaces import PWebModuleDetails
from pweb.system12.pweb_app_config import PWebAppConfig


class PWebRegistry:
    config: PWebAppConfig = PWebAppConfig()
    registerModules: Dict[str, PWebModuleDetails] = {}
    pweb_app: PWebBase = None
