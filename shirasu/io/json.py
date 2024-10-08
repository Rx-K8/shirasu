import json
from pathlib import Path
from typing import Any

from shirasu.io import make_directory


def load_json(file_path: Path) -> Any:
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def write_json(file_path: Path, data: Any):
    make_directory(file_path.parent)
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
