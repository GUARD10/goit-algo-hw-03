import os
import pytest

from task_1.task_1 import copy_and_sort_files


def create_file(path, content="test"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


@pytest.fixture
def test_structure(tmp_path):
    src = tmp_path / "test_src"
    dst = tmp_path / "dist"

    # Файли верхнього рівня
    create_file(src / "file1.txt")
    create_file(src / "file2.jpg")
    create_file(src / "file3")  # без розширення

    # Вкладені
    create_file(src / "sub" / "file4.txt")
    create_file(src / "sub" / "nested" / "file5.png")
    create_file(src / "sub" / "nested" / "file6.mp3")

    return str(src), str(dst)


def test_copy_and_sort_basic(test_structure):
    src, dst = test_structure

    copy_and_sort_files(src, dst)

    assert os.path.exists(os.path.join(dst, "txt", "file1.txt"))
    assert os.path.exists(os.path.join(dst, "jpg", "file2.jpg"))
    assert os.path.exists(os.path.join(dst, "no_extension", "file3"))

    assert os.path.exists(os.path.join(dst, "txt", "file4.txt"))
    assert os.path.exists(os.path.join(dst, "png", "file5.png"))
    assert os.path.exists(os.path.join(dst, "mp3", "file6.mp3"))


def test_no_extra_folders(test_structure):
    src, dst = test_structure

    copy_and_sort_files(src, dst)

    allowed = {"txt", "jpg", "png", "mp3", "no_extension"}
    created = set(os.listdir(dst))

    assert allowed == created, f"Unexpected folders: {created - allowed}"


def test_nested_recursion(test_structure):
    src, dst = test_structure

    copy_and_sort_files(src, dst)

    nested_path = os.path.join(dst, "png", "file5.png")
    assert os.path.exists(nested_path), "Failed to copy nested file"
