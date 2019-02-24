from Model.address import address


def test_edit_address(app):
    app.Contacts.edit_address(
        address(firstname='firstnamedasdsa', lastname='laasdasdtname', nickname='nicknaasdsame', location='location', email='email',
                phone='phodne'))