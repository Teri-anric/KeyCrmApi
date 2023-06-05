from KeyCrm.UserApi.types.client import Client
from KeyCrm.UserApi.types.client_query import ClientQueryList


class ClientMinix:
    def get_client(self, id_: int) -> Client:
        url = f"clients/{id_}"
        return Client.parse_obj(self._get_request(url))

    def sreach_client(self, query):
        url = "clients"
        params = {"query": query}
        return ClientQueryList.parse_obj(self._get_request(url, params=params))