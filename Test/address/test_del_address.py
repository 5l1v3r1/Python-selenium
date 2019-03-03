from Model.address import address

def test_del_address(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    old_address = app.Contacts.get_address_list()
    app.Contacts.del_first_address()
    new_address = app.Contacts.get_address_list()
    assert len(old_address) - 1 == len(new_address)