# -*- coding: utf-8 -*-
from Model.address import address


def test_add_address(app):
    app.Contacts.open_edit_address()
    app.Contacts.add_address(
        address(firstname='firstname', lastname='lastname', nickname='nickname', location='location', email='email',
                phone='phone'))
    app.Contacts.add_work()
    app.Contacts.add_birthday()
    app.Contacts.submit_add_address()
    app.Contacts.return_home_page()
    app.session.Logout()

def test_add_empty_address(app):
    app.Contacts.open_edit_address()
    app.Contacts.add_address(address(' ', ' ', ' ', ' ', ' ', ' '))
    app.Contacts.submit_add_address()
    app.Contacts.return_home_page()

