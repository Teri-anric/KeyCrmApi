from typing import List, Optional, Union, Dict, Any

from KeyCrm.types.costom_fields import CustomField

class CustomFieldsMinix:
    def get_custom_fields(self, include: Optional[str] = None, sort: Optional[str] = None, filters: Dict[str, Any] = None) -> List[CustomField]:
        url = "/products"
        if sort is not None:
            params['sort'] = sort
        if include is not None:
            params['include'] = include
        if filters is not None:
            params['filter'] = filters

        return [CustomField.parse_obj(obj) for obj in self.get_request(url, params)]
