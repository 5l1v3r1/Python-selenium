from Model.contact import Contact

def test_contact_list(app, db):
    if app.Contacts.count_contacts() == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))

    ui_list = app.Contacts.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

    db_list = map(clean, db.get_contact_full_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
