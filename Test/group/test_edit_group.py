from Model.group import group

def test_edit_first_group_name(app):
    app.session.Login(username="admin", password="secret")
    app.Group.edit_group(group(name="New Group"))
    app.session.Logout()