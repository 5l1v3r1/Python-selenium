from Model.address import address
from random import randrange

def test_del_some_address(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    old_address = app.Contacts.get_address_list()
    index = randrange(len(old_address))
    app.Contacts.del_address_by_index(index)
    assert len(old_address) - 1 == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address[index:index+1] = []
    assert old_address == new_address