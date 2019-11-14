"""
Unit and regression test for the masscalc package.
"""

# Import package, test suite, and other packages as needed
import masscalc
import pytest
import sys

def test_masscalc_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "masscalc" in sys.modules
