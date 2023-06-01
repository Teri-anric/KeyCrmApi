from .login import LoginMinix
from .types import FileData
from KeyCrm.utils import parse_filters
from typing import List, Union, Dict
from pathlib import Path
from urllib.parse import quote

class UserApi(LoginMinix):
    def __init__(self, domain, token=None, **kwargs):
        super().__init__(domain, token, **kwargs)

    def delete_products(self, ids: List[Union[int, str]]):
        if not ids:
            return
        url = "batch/products/execute/remove?filters[id]=" + quote(",".join(map(str, ids)))
        return self._post_request(url).get("result")

    def temp_upload_import(self, file_path: Union[str, Path]) -> FileData:
        url = "file-storage/temp-upload/import"
        headers = {"Content-type": "multipart/form-data",
                   "Accept": "application/json",
                   "Cache-Control": "no-cache",
                   "Pragma": "no-cache",
                   "Authorization": f"Bearer {self.token}"}
        with open(file_path, 'rb') as fp:
            data = self._post_request(url, headers=headers, files={'file': [fp]})
        return FileData.parse_obj(data)

    def _import(self, file_id: int, selected: Dict[int, str], type_: str = "products", start_import: int = 2,
                separator: str = ',', params=None):
        url = "import"
        _params = {"file_id": file_id, "selected": selected, "type": type_, "start_import": start_import,
                   "separator": separator}
        if params is None:
            params = {"update": True}
        return self._post_request(url, params=_params)

    def easy_product_import(self, file_path, selected: Dict[int, str]):
        file = self.temp_upload_import(file_path)
        return self._import(file.id, selected)

