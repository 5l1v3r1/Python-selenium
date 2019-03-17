# -*- coding: utf-8 -*-
from Model.address import address
import pytest
from data.contacts import Testdata

@pytest.mark.parametrize("contact", Testdata, ids=[repr(x) for x in Testdata])

def test_add_address(app, contact):
    old_address = app.Contacts.get_address_list()
    app.Contacts.add_address(contact)
    assert len(old_address) + 1 == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)




