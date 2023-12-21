from typing import Optional, Dict, Union


def parse_filters(filters: Optional[Dict[str, Union[str, int, list]]] = None, base: str = "filter"):
    params = {}
    for key, value in filters.items():
        if isinstance(value, list):
            value = ",".join(map(str, value))
        params[f"{base}[{key}]"] = value
    return params
