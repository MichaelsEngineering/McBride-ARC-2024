# tests/test_utils.py
import pytest
from src.utils.utils import load_and_log_first_task, format_submission

def test_load_and_log_first_task_with_invalid_path():
    result = load_and_log_first_task("invalid_path.json")
    assert result is None

def test_format_submission_with_valid_input():
    test_input = {
        "task1": [[[0, 1], [1, 0]]]
    }
    expected = {
        "task1": [{"attempt_1": [[0, 1], [1, 0]], "attempt_2": [[0, 1], [1, 0]]}]
    }
    assert format_submission(test_input) == expected