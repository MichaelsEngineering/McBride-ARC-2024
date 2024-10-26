# tests/conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--ollama-url",
        default="http://localhost:11434",
        help="URL for the Ollama server"
    )
    parser.addoption(
        "--model",
        default="llama3.2",
        help="Model to use for testing"
    )
    parser.addoption(
        "--timeout",
        default=30,
        type=int,
        help="Timeout in seconds for generation requests"
    )

@pytest.fixture
def ollama_config(request):
    return {
        "base_url": request.config.getoption("--ollama-url"),
        "model": request.config.getoption("--model"),
        "timeout": request.config.getoption("--timeout")
    }