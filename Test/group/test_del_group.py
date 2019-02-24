from Model.group import group

def test_delete_first_group(app):
    if app.Group.countgroup() == 0:
        app.Group.create(group(name="test1"))

    app.Group.delete_first_group()