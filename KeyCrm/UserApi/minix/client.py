from KeyCrm.UserApi.types.client import Client


class ClientMinix:
    def get_client(self, id_: int) -> Client:
        url = f"clients/{id_}"
        return Client.parse_obj(self._get_request(url))
