# -*- coding: utf-8 -*-
from Model.contact import Contact



def test_add_address(app, orm, db, json_contacts, check_ui):
    contact = json_contacts
    old_address = orm.get_contact_list()
    app.Contacts.add_contact(contact)
    #assert len(old_address) + 1 == app.Contacts.count_address()
    new_address = orm.get_contact_list()
    old_address.append(contact)
    assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_full_list()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.Contacts.get_contact_list(), key=Contact.id_or_max)




