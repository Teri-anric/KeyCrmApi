from KeyCrm.UserApi.types.buyer import ClientsCompany
from KeyCrm.UserApi.types.company import Company, CompanyList


class CompanyMinix:
    def get_company_clients(self, id_) -> ClientsCompany:
        url = f"clients/company-list/{id_}"
        return ClientsCompany.parse_obj(self._get_request(url, params={'id': id_}))

    def get_companies(self, query: str = None,  page: int = 1, limit: int = 15, order_by: str = 'created_at|desc'):
        url = "clients/company"
        params = {}
        if query:
            params['query'] = query
        params['per_page'] = limit
        params['page'] = page
        params['orderBy'] = order_by
        return CompanyList.parse_obj(self._get_request(url, params=params))

    def get_company(self, id_):
        url = f"clients/company/{id_}"
        return Company.parse_obj(self._get_request(url))
