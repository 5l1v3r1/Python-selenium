def test_del_address(app):
    app.session.Login(username="admin", password="secret")
    app.Contacts.del_first_address()
    app.session.Logout()