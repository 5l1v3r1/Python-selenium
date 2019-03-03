from Model.address import address


def test_edit_address_name(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    old_address = app.Contacts.get_address_list()
    app.Contacts.edit_address(address(firstname='firstnamedasdsa'))
    new_address = app.Contacts.get_address_list()
    assert len(old_address) == len(new_address)

#def test_edit_address_lastname(app):
   #if app.Contacts.count_address() == 0:
        #app.Contacts.edit_address(address(lastname='lastnametesto2'))
