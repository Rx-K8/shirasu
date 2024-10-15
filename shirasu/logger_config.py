import logging
from pathlib import Path

LOG_DIR = Path(__file__).parents[1].resolve() / "logs"


def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(level=level, format=format)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(LOG_DIR / log_file, mode="w")

    stream_handler = logging.StreamHandler()

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
