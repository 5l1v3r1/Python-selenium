from Model.group import group

def test_edit_first_group(app):
    app.session.Login(username="admin", password="secret")
    app.Group.edit_group(group(name="namsadasdsae2", footer="footssadadasdasasder2", header="headercxcxczxcxcxzcc"))
    app.session.Logout()