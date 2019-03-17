# -*- coding: utf-8 -*-
from Model.address import address


def test_add_address(app, json_contacts):
    contact = json_contacts
    old_address = app.Contacts.get_address_list()
    app.Contacts.add_address(contact)
    assert len(old_address) + 1 == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)




