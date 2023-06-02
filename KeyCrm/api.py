import requests
from KeyCrm.minix import ProductMinix, CustomFieldsMinix, OfferMinix
from KeyCrm.exceptions import UnAuthorizedError, TooManyRequests
from typing import Optional
from logging import getLogger, Logger
from time import sleep

BASE_API_URL = 'https://openapi.keycrm.app/v1'
DEFAULT_LOGGER = getLogger("KeyCrm")


class ApiCrm(ProductMinix, CustomFieldsMinix, OfferMinix):
    def __init__(self, token: str, logger: Optional[Logger] = None, max_count_repair_request: int = 10):
        self.token = token
        self.log = logger if logger is not None else DEFAULT_LOGGER
        self.max_count_repair_request = max_count_repair_request
        self._session = requests.session()
        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Cache-Control": "no-cache",
                   "Pragma": "no-cache",
                   "Authorization": f"Bearer {self.token}"}
        self._session.headers.update(headers)

    def _send_request(self, method: str, url, **kwargs):
        for i in range(self.max_count_repair_request):
            response = self._session.request(method, url, **kwargs)
            if response.status_code in [200, 201, 202]:
                return response.json()
            elif response.status_code == 401:
                raise UnAuthorizedError(response.json().get('message', "Unauthenticated"))
            elif response.status_code == 422:
                raise ValueError()
            elif response.status_code == 429:
                t = int(response.headers.get("Retry-After", 30))
                self.log.info("wait %s sec. and repeat the request" % t)
                sleep(t if t > 0 else 5)
                continue
            else:
                raise response.raise_for_status()
        raise TooManyRequests()

    def _get_request(self, url: str, params):
        return self._send_request("GET", BASE_API_URL + url, params=params)

    def _post_request(self, url: str, params):
        return self._send_request("POST", BASE_API_URL + url, params=params)

    def _put_request(self, url: str, data):
        return self._send_request("PUT", BASE_API_URL + url, data=data)