# -*- coding: utf-8 -*-
from Model.address import address


def test_add_address(app):
    app.Contacts.add_address(
        address(firstname='firstname', lastname='lastname', nickname='nickname', location='location', email='email',
                phone='phone'))

def test_add_empty_address(app):
    app.Contacts.add_address(address(' ', ' ', ' ', ' ', ' ', ' '))


