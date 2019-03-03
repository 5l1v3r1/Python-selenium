from Model.address import address
from random import randrange

def test_edit_some_address(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))

    old_address = app.Contacts.get_address_list()
    index = randrange(len(old_address))
    contact = address(firstname='firstname', lastname='lastname')
    contact.id = old_address[index].id
    app.Contacts.edit_some_address(index, contact)
    assert len(old_address) == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address[index] = contact
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)

#def test_edit_address_lastname(app):
   #if app.Contacts.count_address() == 0:
        #app.Contacts.edit_address(address(lastname='lastnametesto2'))
