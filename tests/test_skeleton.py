# -*- coding: utf-8 -*-

import pytest
from dash_google.skeleton import fib

__author__ = "Christof Westland"
__copyright__ = "Christof Westland"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
