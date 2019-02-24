from Model.address import address

def test_del_address(app):
    if app.Contacts.count_address() == 0:
        app.Contacts.add_address(address(firstname="test2"))
    app.Contacts.del_first_address()