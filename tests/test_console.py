# tests/test_console.py
import click.testing
import pytest

from hypermodern import console

def test_main_succeeds():
    runner  = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
