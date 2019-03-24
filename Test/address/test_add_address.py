# -*- coding: utf-8 -*-
from Model.address import Address


def test_add_address(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_address = db.get_contact_list()
    app.Contacts.add_address(contact)
    #assert len(old_address) + 1 == app.Contacts.count_address()
    new_address = db.get_contact_list()
    old_address.append(contact)
    assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Address.id_or_max) == sorted(app.Contacts.get_address_list(), key=Address.id_or_max)




