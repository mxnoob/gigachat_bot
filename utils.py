import re
from typing import Any


def get_file_id(data: str) -> tuple[Any, bool]:
    match = re.search(r'src="([^"]+)"', data)
    if match:
        return match.group(1), True
    return data, False
