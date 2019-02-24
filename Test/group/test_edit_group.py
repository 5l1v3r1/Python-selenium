from Model.group import group

def test_edit_first_group_name(app):
    if app.Group.countgroup() == 0:
        app.Group.create(group(name="testName"))
    app.Group.edit_group(group(name="New Name"))


def test_edit_first_group_header(app):
    if app.Group.countgroup() == 0:
        app.Group.create(group(header="testHeader"))
    app.Group.edit_group(group(header="New Header"))
