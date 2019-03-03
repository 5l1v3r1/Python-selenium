from Model.address import address

def test_del_address(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    old_address = app.Contacts.get_address_list()
    app.Contacts.del_first_address()
    assert len(old_address) - 1 == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address[0:1] = []
    assert old_address == new_address