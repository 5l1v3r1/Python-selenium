# -*- coding: utf-8 -*-
from Model.address import address


def test_add_address(app):
    old_address = app.Contacts.get_address_list()
    contact = address(firstname='firstname', lastname='lastname', nickname='nickname', location='location', email='email',
                phone='phone')
    app.Contacts.add_address(contact)
    new_address = app.Contacts.get_address_list()
    assert len(old_address) + 1 == len(new_address)
    old_address.append(contact)
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)


#def test_add_empty_address(app):
    #app.Contacts.add_address(address(' ', ' ', ' ', ' ', ' ', ' '))


