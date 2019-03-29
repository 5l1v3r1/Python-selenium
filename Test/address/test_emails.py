import re

def test_emails_on_homepage(app):
    contact_from_home_page = app.Contacts.get_contact_list()[0]
    contact_from_edit_page = app.Contacts.get_contact_info_from_editpage(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_on_home_page(contact_from_edit_page)


#def test_emails_on_view_page(app): - прямая проверка
    #contact_from_view_page = app.Contacts.get_emails_from_view_page(0)
    #contact_from_edit_page = app.Contacts.get_contact_info_from_editpage(0)
    #assert contact_from_view_page.email == clear(contact_from_edit_page.email)
    #assert contact_from_view_page.email2 == clear(contact_from_edit_page.email2)
    #assert contact_from_view_page.email3 == clear(contact_from_edit_page.email3)




def clear(s):
    return re.sub("[, ], -, +, ()", "", s)

def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map (lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))