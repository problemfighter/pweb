from pweb_orm import PWebSaaS


class PWebSaaSRegistry:
    saasConfig: dict = {}

    @staticmethod
    def add_to_saas_config(tenant_key, config_key, value):
        if tenant_key not in PWebSaaSRegistry.saasConfig:
            PWebSaaSRegistry.saasConfig[tenant_key] = {}
        PWebSaaSRegistry.saasConfig[tenant_key][config_key] = value

    @staticmethod
    def get_saas_config(config_key, default=None, tenant_key=None):
        if not tenant_key:
            tenant_key = PWebSaaS.get_tenant_key()
        if tenant_key and tenant_key in PWebSaaSRegistry.saasConfig and config_key in PWebSaaSRegistry.saasConfig[tenant_key]:
            return PWebSaaSRegistry.saasConfig[tenant_key][config_key]
        return default
