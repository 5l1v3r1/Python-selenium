import re
from Model.contact import Contact


def test_assert_all_contacts_with_db (app, db):
    if app.Contacts.count_contacts() == 0:
        app.Contacts.add_contact(Contact(firstname="adadsad", lastname="adsdasd", address="sdadasd",email="asds add",home="sdasdsdad",
                                   mobile="8989989899"))
    else:
        pass
    contacts_from_home_page = app.Contacts.get_contact_list()
    contacts_from_db = db.get_contact_full_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)

    contacts_from_home_page_sorted = sorted(contacts_from_home_page, key = Contact.id_or_max)
    contacts_from_db_sorted = sorted(contacts_from_db, key=Contact.id_or_max)


    for x in range(len(contacts_from_home_page_sorted)):
        assert contacts_from_home_page_sorted[x].lastname == contacts_from_db_sorted[x].lastname.strip()
        assert contacts_from_home_page_sorted[x].firstname == contacts_from_db_sorted[x].firstname.strip()
        assert contacts_from_home_page_sorted[x].address == contacts_from_db_sorted[x].address.strip()
        assert contacts_from_home_page_sorted[x].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db_sorted[x])
        assert contacts_from_home_page_sorted[x].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db_sorted[x])




def clear(s):
    return re.sub('[() -]', " ", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))



def merge_fio_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.firstname, contact.lastname, contact.address, ]))))