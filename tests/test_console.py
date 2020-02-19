# tests/test_console.py
import click.testing
import pytest

from hypermodern import console

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch("requests.get")

@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner, mock_requests_get):
    runner  = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
