from Model.address import address


def test_edit_address_name(app):
    old_address = app.Contacts.get_address_list()
    contact = address(firstname='firstnamedasdsa', lastname='fdsfsddfsds', phone='89887052920')
    contact.id = old_address[0].id
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    app.Contacts.edit_address(contact)
    assert len(old_address) == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address[0] = contact
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)

#def test_edit_address_lastname(app):
   #if app.Contacts.count_address() == 0:
        #app.Contacts.edit_address(address(lastname='lastnametesto2'))
