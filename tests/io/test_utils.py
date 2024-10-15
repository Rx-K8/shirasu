import shutil
import tempfile
from pathlib import Path

import pytest

from shirasu.io.utils import make_directory


@pytest.fixture
def temp_dir():
    # Create a temporary directory
    dir_path = tempfile.mkdtemp()
    print(dir_path)
    yield dir_path
    # Remove the directory after the test
    shutil.rmtree(dir_path)


def test_make_directory_creates_directory(temp_dir):
    # Define a new directory path inside the temporary directory
    new_dir = Path(temp_dir) / "new_dir"

    # Ensure the directory does not exist before the test
    assert not new_dir.exists()

    # Call the function to create the directory
    make_directory(new_dir)

    # Check if the directory was created
    assert new_dir.exists()


def test_make_directory_existing_directory(temp_dir):
    # Define a new directory path inside the temporary directory
    new_dir = Path(temp_dir) / "new_dir"

    # Create the directory before the test
    new_dir.mkdir()

    # Ensure the directory exists before the test
    assert new_dir.exists()

    # Call the function to create the directory again
    make_directory(new_dir)

    # Check if the directory still exists
    assert new_dir.exists()
