import re

def test_emails_on_homepage(app):
    contact_from_home_page = app.Contacts.get_address_list()[0]
    contact_from_edit_page = app.Contacts.get_address_info_from_editpage(0)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_on_home_page(contact_from_edit_page)


def test_emails_on_view_page(app):
    contact_from_view_page = app.Contacts.get_emails_from_view_page(0)
    contact_from_edit_page = app.Contacts.get_address_info_from_editpage(0)
    assert contact_from_view_page.email1 == contact_from_edit_page.email1
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3




def clear(s):
    return re.sub("[, ], -, +, ()", "", s)

def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map (lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.email1, contact.email2, contact.email3]))))