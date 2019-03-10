# -*- coding: utf-8 -*-
from Model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



Testdata = [Group(name="", footer="", header="")] + [Group(name=random_string("name", 10), footer=random_string("footer", 20), header=random_string("header", 20)) for i in range(3)]


@pytest.mark.parametrize("group", Testdata, ids=[repr(x) for x in Testdata])
def test_add_group(app, group):
        old_groups = app.group.get_group_list()
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.countgroup()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
