from Model.group import Group
from random import randrange
import pytest

def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testName"))
    with pytest.allure.step('Given a old group list'):
        old_groups = db.get_group_list()
        index = randrange(len(old_groups))
        group = Group(name="New Nameasasa")
        group.id = old_groups[index].id
    with pytest.allure.step('When edit group'):
        app.group.edit_group_by_id(group.id,group)
    #assert len(old_groups) == app.group.countgroup()
    with pytest.allure.step('Given a new group list'):
        new_groups = db.get_group_list()
    with pytest.allure.step('Then the new group list equal to the old group list with the edit group'):
        old_groups[index] = group
        assert old_groups == new_groups
    if check_ui:
        groups_name_from_db = db.get_list_of_groups_names_and_ids()
        assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                 key=Group.id_or_max)

#def test_edit_first_group_header(app):
    #if app.group.countgroup() == 0:
     #   app.group.create(Group(header="testHeader"))
   # old_groups = app.group.get_group_list()
   # app.group.edit_group(Group(header="New Header"))
    #new_groups = app.group.get_group_list()
   # assert len(old_groups) == len(new_groups)
