import re

def test_first_last_address_on_homepage(app):
    contact_from_home_page = app.Contacts.get_contact_list[0]
    contact_from_edit_page = app.Contacts.get_contact_info_from_editpage(0)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def clear(s):
    return re.sub("[, ], -, +, ()", "", s)