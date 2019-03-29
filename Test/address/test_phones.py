import re
#обратная проверка (склейка)
def test_phones_on_homepage(app, db):
    contact_from_home_page = app.Contacts.get_contact_list()[0]
    contact_from_edit_page = app.Contacts.get_contact_info_from_editpage(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phone_on_home_page(contact_from_edit_page)

#прямая проверка (вырезка)
#def test_phones_on_view_page(app):
    #contact_from_view_page = app.Contacts.get_contact_from_view_page(0)
    #contact_from_edit_page = app.Contacts.get_contact_info_from_editpage(0)
    #assert contact_from_view_page.home == contact_from_edit_page.home
    #assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    #assert contact_from_view_page.work == contact_from_edit_page.work
    #assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[, ], -, +, ()", "", s)


def merge_phone_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map (lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.phone2]))))