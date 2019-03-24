from Model.address import Address
import random

def test_del_some_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_address(Address(firstname="test2"))
    old_address = db.get_contact_list()
    contact = random.choice(old_address)
    app.Contacts.del_address_by_id(contact.id)
    new_address = db.get_contact_list()
    old_address.remove(contact)
    assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Address.id_or_max) == sorted(app.Contacts.get_address_list(), key=Address.id_or_max)