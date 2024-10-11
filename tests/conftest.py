"""
Configuration for pytest fixtures.
"""

import sys
import pexpect
import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()  # Ensure 'create' is a valid method or adjust accordingly

@pytest.fixture
def repl():
    """Fixture to start the REPL application."""
    script = 'main.py'
    child = pexpect.spawn(sys.executable + f' {script}', encoding='utf-8', timeout=5)
    child.expect('Welcome to the Calculator REPL.*')
    yield child
    child.terminate()
