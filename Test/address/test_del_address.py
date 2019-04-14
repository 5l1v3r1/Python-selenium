from Model.contact import Contact
import random
import pytest

def test_del_some_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))
    with pytest.allure.step('Given a old contact list'):
        old_address = db.get_contact_list()
    contact = random.choice(old_address)
    with pytest.allure.step('When i delete contact to the list'):
        app.Contacts.del_contact_by_id_with_allert(contact.id)
    with pytest.allure.step('Given a new contact list'):
        new_address = db.get_contact_list()
    with pytest.allure.step('Then the new contact list equal to the old contact list with the delete contact'):
        assert len(old_address) - 1 == app.Contacts.count_contacts()
        old_address.remove(contact)
        assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_phone_and_mail_list()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.Contacts.get_contact_list(), key=Contact.id_or_max)