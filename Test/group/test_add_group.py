# -*- coding: utf-8 -*-
from Model.group import Group
from sys import maxsize

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="name", footer="footer", header="header")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.countgroup()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", footer="", header="")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.countgroup()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) 


