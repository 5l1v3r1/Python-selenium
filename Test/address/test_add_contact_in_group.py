import random
from Model.contact import Contact
from Model.group import Group
import pytest

def test_add_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.Contacts.add_contact(Contact(firstname="test2"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testName"))
    with pytest.allure.step('Given a group list'):
        selected_group = random.choice(orm.get_group_list())
    with pytest.allure.step('Given a contact_not_in_group'):
        contact_not_in_group = orm.get_contacts_not_in_group(selected_group)
    with pytest.allure.step('Given a contact_in_group'):
        contact_in_group = orm.get_contacts_in_group(selected_group)
    with pytest.allure.step('check contact list before add'):
        countact_before_adding = len(contact_in_group)
    if len(contact_not_in_group) == 0:
        app.Contacts.add_contact(
            Contact(firstname="Firstname", lastname="Lastname", address="Address"))
    contact_not_in_group = orm.get_contacts_not_in_group(selected_group)
    selected_contact = random.choice(contact_not_in_group)
    with pytest.allure.step('when select group list from group page'):
        app.group.select_group_from_home_page(selected_group.id)
    with pytest.allure.step('when added contact in group'):
        app.Contacts.add_contact_in_group(selected_contact.id)
    with pytest.allure.step('given a new contact list in group'):
        new_contact_in_group = orm.get_contacts_in_group(selected_group)
    with pytest.allure.step('then equal contacts before add with after add'):
        count_contact_in_group_after_adding_member = len(new_contact_in_group)
        assert countact_before_adding + 1 == count_contact_in_group_after_adding_member

    #new_contact_list = orm.get_contacts_in_group(old_group_list)
    #count_contacts_after_add = len(new_contact_list)
    #assert count_contacts_before_add + 1 == count_contacts_after_add









