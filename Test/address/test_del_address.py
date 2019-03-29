from Model.contact import Contact
import random

def test_del_some_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))
    old_address = db.get_contact_list()
    contact = random.choice(old_address)
    app.Contacts.del_contact_by_id_with_allert(contact.id)
    new_address = db.get_contact_list()
    assert len(old_address) - 1 == app.Contacts.count_contacts()
    old_address.remove(contact)
    assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_phone_and_mail_list()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.Contacts.get_contact_list(), key=Contact.id_or_max)