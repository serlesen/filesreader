import pytest

from filesreader import FileReader


def test_read_existing_file():
    # given
    reader = FileReader("tests/resources/existing_file.txt")

    # when
    lines = reader.read_all_lines()

    # then
    assert lines == ["first", "second", "the last line"]


def test_read_not_existing_file():
    # when then
    with pytest.raises(FileNotFoundError):
        reader = FileReader("tests/resources/not_existing_file.txt")

