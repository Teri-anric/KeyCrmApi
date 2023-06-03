from pathlib import Path
from typing import Dict, Union

from KeyCrm.UserApi.types.file import FileData


class ImportMinix:
    def temp_upload_import(self, file_path: Union[str, Path]) -> FileData:
        url = "file-storage/temp-upload/import"
        return FileData.parse_obj(self._post_request(url))

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
