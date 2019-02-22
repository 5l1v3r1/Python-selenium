# -*- coding: utf-8 -*-
from Model.group import group

    
def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.Group.create(group(name="name", footer="footer", header="header"))
    app.session.Logout()


def test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.Group.create(group(name=" ", footer=" ", header=" "))
    app.session.Logout()

