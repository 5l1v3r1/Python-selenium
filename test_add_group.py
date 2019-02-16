# -*- coding: utf-8 -*-
from group import group
from Application import Application
import pytest

@pytest.fixture
def app(request):
   fixture = Application()
   request.addfinalizer(fixture.destroy)
   return fixture

    
def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(group(name="name", footer="footer", header="header"))
    app.Logout()

def test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(group(name=" ", footer=" ", header=" "))
    app.Logout()

