from KeyCrm.UserApi.minix.client import ClientMinix
from KeyCrm.UserApi.minix.company import CompanyMinix
from KeyCrm.UserApi.minix.import_ import ImportMinix
from KeyCrm.UserApi.minix.login import LoginMinix
from KeyCrm.UserApi.minix.product import ProductMinix


class UserApi(LoginMinix, ImportMinix, ProductMinix, CompanyMinix, ClientMinix):
    def __init__(self, domain, token=None, **kwargs):
        super().__init__(domain, token, **kwargs)
