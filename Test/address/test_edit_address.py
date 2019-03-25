from Model.contact import Contact
from random import randrange

def test_edit_some_address(app, db, check_ui):
    if app.Contacts.count_contacts() == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))

    old_address = db.get_contact_list()
    index = randrange(len(old_address))
    contact = Contact(firstname='firstname', lastname='lastname')
    contact.id = old_address[index].id
    app.Contacts.edit_contact_by_id(contact.id, contact)
    new_address = db.get_contact_list()
    assert len(old_address) == len(new_address)
    new_address = db.get_contact_list()
    old_address[index] = contact
    assert old_address == new_address
    if check_ui:
        contact_list = db.get_contact_full_list()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.Contacts.get_contact_list(), key=Contact.id_or_max)

#def test_edit_address_lastname(app):
   #if app.Contacts.count_address() == 0:
        #app.Contacts.edit_address(address(lastname='lastnametesto2'))
