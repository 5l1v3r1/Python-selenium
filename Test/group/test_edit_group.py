from Model.group import group

def test_edit_first_group_name(app):
    app.Group.edit_group(group(name="New Group"))
