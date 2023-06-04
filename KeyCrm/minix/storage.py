from typing import Optional, Dict, Any

from KeyCrm.types.file import ListFile, File


class StorageMinix:
    def get_storage(self, include: Optional[str] = None, sort: Optional[str] = None,
                    filters: Dict[str, Any] = None) -> ListFile:
        url = "/storage"
        params = {}
        if sort is not None:
            params['sort'] = sort
        if include is not None:
            params['include'] = include
        if filters is not None:
            params['filter'] = filters

        # Perform the get_request and parse the response into CustomFieldProduct objects
        response = self._get_request(url, params)
        data = response.json()

        return ListFile.parse_obj(data)

    def upload_file(self, file_path: str) -> File:
        headers = self.default_header()
        headers.update({"Content-Type": "multipart/form-data"})
        url = "/storage/upload"
        files = {"file": open(file_path, "rb"), }

        # Perform the upload request
        response = self._post_request(url, headers=headers, files=files)
        data = response.json()

        return File.parse_obj(data)
