# tests/conftest.py
import pytest


@pytest.fixture
def mock_requests_get(mocker):
    """Provides a mock API response.

    Returns:
        Json document
    """
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


def pytest_configure(config):
    """Adds pytest markers that can be used for configuration"""

    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
