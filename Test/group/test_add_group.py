# -*- coding: utf-8 -*-
from Model.group import group

    
def test_add_group(app):
    app.Group.create(group(name="name", footer="footer", header="header"))

def test_add_empty_group(app):
    app.Group.create(group(name=" ", footer=" ", header=" "))


