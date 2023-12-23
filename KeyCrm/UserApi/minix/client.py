from KeyCrm.UserApi.types.client import Client
from KeyCrm.UserApi.types.client_query import ClientQueryList


class ClientMinix:
    def get_client(self, id_: int) -> Client:
        url = f"clients/{id_}"
        return Client.parse_obj(self._get_request(url))

    def sreach_client(self, query):
        url = "clients"
        params = {"query": query}
        obj = self._get_request(url, params=params)
        if obj:
            return ClientQueryList.parse_obj(obj)
        return None

    def contact_set_client(self, contact_id: int, client_id: int):
        url = f"clients/contacts/{contact_id}/assign/{client_id}"
        return self._put_request(url)

    def contact_switch_client(self, contact_id: int, client_id: int):
        url = f"clients/contacts/{contact_id}/switch/{client_id}"
        return self._put_request(url)