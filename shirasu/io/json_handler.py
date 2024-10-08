import json
import logging
from pathlib import Path
from typing import Dict, Optional

from shirasu.io.utils import make_directory

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            err_msg = f"File not found: {args}, error: {e}"
            logger.error(err_msg)
            raise FileNotFoundError(err_msg)
        except json.JSONDecodeError as e:
            err_msg = f"Failed to decode JSON from {args}, error: {e}"
            logger.error(err_msg)
            raise json.JSONDecodeError(err_msg, e.doc, e.pos)

    return wrapper


@error_handler
def load_json(file_path: Path) -> Optional[Dict]:
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    logger.info(f"Loaded JSON from {file_path}: {data}")
    return data


@error_handler
def write_json(file_path: Path, data: Dict):
    make_directory(file_path.parent)
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
