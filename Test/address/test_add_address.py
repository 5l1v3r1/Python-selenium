# -*- coding: utf-8 -*-
from Model.address import address


def test_add_address(app):
    old_address = app.Contacts.get_address_list()
    app.Contacts.add_address(
        address(firstname='firstname', lastname='lastname', nickname='nickname', location='location', email='email',
                phone='phone'))
    new_address = app.Contacts.get_address_list()
    assert len(old_address) + 1 == len(new_address)


def test_add_empty_address(app):
    app.Contacts.add_address(address(' ', ' ', ' ', ' ', ' ', ' '))


