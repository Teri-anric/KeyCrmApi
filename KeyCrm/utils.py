from typing import Optional, Dict, Union

def parse_filters(filters: Optional[Dict[str, Union[str, int, list]]] = None):
    params = {}
    for key, value in filters.items():
        if isinstance(value, list):
            value = ",".join(f"{value}")
        params[f"filter[{key}]"] = value
    return params


