from Model.group import Group

def test_edit_first_group_name(app):
    if app.group.countgroup() == 0:
        app.group.create(Group(name="testName"))
    old_groups = app.group.get_group_list()
    group = Group(name="New Name")
    group.id = old_groups[0].id
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
    #if app.group.countgroup() == 0:
     #   app.group.create(Group(header="testHeader"))
   # old_groups = app.group.get_group_list()
   # app.group.edit_group(Group(header="New Header"))
    #new_groups = app.group.get_group_list()
   # assert len(old_groups) == len(new_groups)
