import random
from Model.contact import Contact
from Model.group import Group

def test_add_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testName"))
    selected_group = random.choice(orm.get_group_list())
    contact_not_in_group = orm.get_contacts_not_in_group(selected_group)
    contact_in_group = orm.get_contacts_in_group(selected_group)
    countact_before_adding = len(contact_in_group)
    if len(contact_not_in_group) == 0:
        app.Contacts.add_contact(
            Contact(firstname="Firstname", lastname="Lastname", address="Address"))
    contact_not_in_group = orm.get_contacts_not_in_group(selected_group)
    selected_contact = random.choice(contact_not_in_group)
    app.group.select_group_from_home_page(selected_group.id)
    app.Contacts.add_contact_in_group(selected_contact.id)
    new_contact_in_group = orm.get_contacts_in_group(selected_group)
    count_members_in_group_after_adding_member = len(new_contact_in_group)
    assert countact_before_adding + 1 == count_members_in_group_after_adding_member

    #new_contact_list = orm.get_contacts_in_group(old_group_list)
    #count_contacts_after_add = len(new_contact_list)
    #assert count_contacts_before_add + 1 == count_contacts_after_add









