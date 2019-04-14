from Model.group import Group
import random
import pytest

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    with pytest.allure.step('Given a old group list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    #app.group.delete_group_by_index(index)
    with pytest.allure.step('delete group by id'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Given a new group list'):
        new_groups = db.get_group_list()
    with pytest.allure.step('Then the new group list equal to the old group list with the edit group'):
        assert len(old_groups) - 1 == app.group.countgroup()
        #old_groups[index:index+1] = []
        old_groups.remove(group)
        assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)