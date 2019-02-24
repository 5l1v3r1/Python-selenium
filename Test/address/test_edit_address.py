from Model.address import address


def test_edit_address_name(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.edit_address(address(firstname='firstnamedasdsa'))

def test_edit_address_lastname(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.edit_address(address(lastname='lastnametesto2'))
