from Model.address import address


def test_del_address(app):
    app.session.Login(username="admin", password="secret")
    app.Contacts.edit_address(
        address(firstname='firstnamedasdsa', lastname='laasdasdtname', nickname='nicknaasdsame', location='location', email='email',
                phone='phodne'))
    app.session.Logout()