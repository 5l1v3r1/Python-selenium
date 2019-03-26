import random
from Model.contact import Contact
from Model.group import Group

def test_add_contact_in_group(app, orm, db, json_contacts, json_groups):
    contacts = json_contacts
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(contacts)
    groups = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(groups)
    old_contact_list = orm.get_contact_list()
    contact = random.choice(old_contact_list)
    old_group_list = orm.get_group_list()
    group = random.choice(old_group_list)
    old_contact = orm.get_contacts_in_group(group)
    count_contact_before_add = len(old_contact)

    app.group.select_group_from_home_page(group.id)
    app.Contacts.add_contact_in_group(contact.id)

    contact_in_group = orm.get_contacts_in_group(group)
    count_contact_after_add = len(contact_in_group)
    assert count_contact_before_add + 1 == count_contact_after_add

    #new_contact_list = orm.get_contacts_in_group(old_group_list)
    #count_contacts_after_add = len(new_contact_list)
    #assert count_contacts_before_add + 1 == count_contacts_after_add









