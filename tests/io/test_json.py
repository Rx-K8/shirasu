import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from shirasu.io.json import load_json, write_json


def test_load_json():
    with NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8", suffix=".json"
    ) as temp_file:
        json_data = {"key": "value"}
        json.dump(json_data, temp_file)
        temp_file_path = Path(temp_file.name)

    result = load_json(temp_file_path)

    assert result == json_data

    # Clean up the temporary file
    temp_file_path.unlink()


def test_write_json():
    # Create a temporary file path
    with NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file_path = Path(temp_file.name)

    # Data to be written
    data = {"key": "value"}

    # Write the JSON data using the function
    write_json(temp_file_path, data)

    # Read the data back from the file
    with open(temp_file_path, "r", encoding="utf-8") as json_file:
        result = json.load(json_file)

    # Check if the written data matches the expected data
    assert result == data

    # Clean up the temporary file
    temp_file_path.unlink()
