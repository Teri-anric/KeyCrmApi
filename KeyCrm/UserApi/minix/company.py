from KeyCrm.UserApi.types.buyer import ClientsCompany
from KeyCrm.UserApi.types.company import Company


class CompanyMinix:
    def get_company_clients(self, id_) -> ClientsCompany:
        url = f"clients/company-list/{id_}"
        return ClientsCompany.parse_obj(self._get_request(url, params={'id': id_}))

    def get_company(self, id_):
        url = f"clients/company/{id_}"
        return Company.parse_obj(self._get_request(url))
