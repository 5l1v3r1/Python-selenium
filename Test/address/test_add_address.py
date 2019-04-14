# -*- coding: utf-8 -*-
from Model.contact import Contact
import pytest


def test_add_address(app, orm, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a old contact list'):
        old_address = orm.get_contact_list()
    with pytest.allure.step('When add contact'):
        app.Contacts.add_contact(contact)
    #assert len(old_address) + 1 == app.Contacts.count_address()
    with pytest.allure.step('Given a new contact list'):
        new_address = orm.get_contact_list()
    with pytest.allure.step('Then the new contact list equal to the old contact list with the added contact'):
        old_address.append(contact)
        assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_full_list()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.Contacts.get_contact_list(), key=Contact.id_or_max)




