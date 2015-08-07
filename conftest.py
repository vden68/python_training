# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

