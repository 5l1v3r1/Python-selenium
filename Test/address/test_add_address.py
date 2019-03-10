# -*- coding: utf-8 -*-
from Model.address import address
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

Testdata = [address(firstname='', lastname='', Address='', mobilephone='', email1='')] + \
           [address(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), \
                    Address=random_string("Address", 20), mobilephone=random_string("mobilephone", 20), \
                    email1=random_string("email", 20) ) for i in range(2)]

@pytest.mark.parametrize("contact", Testdata, ids=[repr(x) for x in Testdata])

def test_add_address(app, contact):
    old_address = app.Contacts.get_address_list()
    app.Contacts.add_address(contact)
    assert len(old_address) + 1 == app.Contacts.count_address()
    new_address = app.Contacts.get_address_list()
    old_address.append(contact)
    assert sorted(old_address, key=address.id_or_max) == sorted(new_address, key=address.id_or_max)




