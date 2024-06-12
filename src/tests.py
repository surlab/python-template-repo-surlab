"""a generic description of this script, tests.py.
generated automatically on project creation from the surlab python-template-repo. 
please update this docstring as you develop.

src/tests.py should contain unit tests for functions in src modules, particularly in src.computation
"""

import src.computation as comp
import pytest


def test_typical_some_function():
	assert comp.some_function() == 1

def test_raises_some_function():
    with pytest.raises(AssertionError):
        comp.some_function()



