import random
from Model.contact import Contact
from Model.group import Group

def test_delete_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testName"))
    group_list = orm.get_group_list()
    contact_list = orm.get_contact_list()
    selected_group = random.choice(group_list)
    contact_list_from_group = orm.get_contacts_in_group(selected_group)
    if len(contact_list_from_group) == 0:
        selected_contact = random.choice(contact_list)
        app.group.select_group_from_home_page(selected_group.id)
        app.Contacts.add_contact_in_group(selected_contact.id)
        contact_list_from_group = orm.get_contacts_in_group(selected_group)
    count_contact_before_add = len(contact_list_from_group)
    selected_contact = random.choice(contact_list_from_group)
    app.Contacts.open_group_page_with_contact(selected_group.name)
    contact_index = contact_list_from_group.index(selected_contact)
    app.Contacts.delete_contact_from_group(selected_group.name, contact_index)
    contact_list = orm.get_contacts_in_group(selected_group)
    count_contact_after_add = len(contact_list)
    assert count_contact_before_add - 1 == count_contact_after_add

