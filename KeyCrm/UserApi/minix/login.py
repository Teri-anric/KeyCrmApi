import requests

from KeyCrm.UserApi.types.account import User
from KeyCrm.exceptions import UnAuthorizedError, TooManyRequests


class LoginMinix:
    def __init__(self, domain, token=None, max_count_repair_request=2):
        self.domain = domain
        self._session = requests.session()
        self.token = token
        self.max_count_repair_request = max_count_repair_request
        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Cache-Control": "no-cache",
                   "Pragma": "no-cache"}
        self._session.headers.update(headers)

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value if value else 'null'
        self._session.headers.update({"Authorization": f"Bearer {self._token}"})

    def is_active(self):
        url = "billing/check"
        try:
            return self._get_request(url, params=None).get('active', False)
        except UnAuthorizedError:
            return False

    @property
    def base_url(self):
        return f"https://{self.domain}.api.keycrm.app/"

    def _send_request(self, method: str, url, **kwargs):
        for i in range(self.max_count_repair_request):
            response = self._session.request(method, self.base_url + url, **kwargs)
            if response.status_code in [200, 201, 202]:
                return response.json()
            elif response.status_code == 204:
                return {}
            elif response.status_code == 401:
                raise UnAuthorizedError(response.json().get('message', "Unauthenticated"))
            elif response.status_code == 422:
                raise ValueError(response.json())
            elif response.status_code == 429:
                t = int(e.response.headers.get("Retry-After", 30))
                sleep(t if t > 0 else 5)
                continue
            else:
                raise response.raise_for_status()
        raise TooManyRequests()

    def _get_request(self, url: str, params=None, **kwargs):
        response = self._send_request("GET", url, params=params, **kwargs)
        return response

    def _post_request(self, url: str, params=None, **kwargs):
        response = self._send_request("POST", url, params=params, **kwargs)
        return response

    def _put_request(self, url: str, data=None, **kwargs):
        response = self._send_request("PUT", url, data=data, **kwargs)
        return response

    def _delete_request(self, url: str):
        response = self._send_request("DELETE", url)
        return response

    def login(self, email, password):
        url = 'auth/login'
        params = {"username": email, "password": password}
        result = self._post_request(url, params=params)
        token = result.get('token', None)
        if not token:
            return False
        self.token = token
        return True

    def get_me(self):
        url = "auth/profile"
        try:
            return User.parse_obj(self._get_request(url))
        except UnAuthorizedError:
            return None
