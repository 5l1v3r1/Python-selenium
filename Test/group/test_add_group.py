# -*- coding: utf-8 -*-
from Model.group import Group
import pytest

def test_add_group(app, db, json_groups, check_ui):
        group = json_groups
        with pytest.allure.step('Given a group list'):
                old_groups = db.get_group_list()
        with pytest.allure.step('When i add the group to the list'):
                app.group.create(group)
        #assert len(old_groups) + 1 == app.group.countgroup()
        with pytest.allure.step('Then the new group list equal to the old group list with the added group'):
                new_groups = db.get_group_list()
                old_groups.append(group)
                assert old_groups == new_groups
        if check_ui:
                groups_name_from_db = db.get_list_of_groups_names_and_ids()
                assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                           key=Group.id_or_max)