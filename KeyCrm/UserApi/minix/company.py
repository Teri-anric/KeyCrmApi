from KeyCrm.UserApi.types.buyer import ClientsCompany


class CompanyMinix:
    def get_company_clients(self, id_) -> ClientsCompany:
        url = f"clients/company-list/{id_}"
        return ClientsCompany.parse_obj(self._get_request(url, params={'id': id_}))
