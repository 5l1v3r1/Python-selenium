from Model.group import group

def test_delete_first_group(app):
    app.session.Login(username="admin", password="secret")
    app.Group.edit_group(group(name="name2", footer="footer2", header="headercxcxczxcxcxzcc"))
    app.session.Logout()