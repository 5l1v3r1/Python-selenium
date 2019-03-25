from Fixture.orm import ORMFixture
from Model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contacts_not_in_group(Group(id="18"))
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    pass #db.destroy()

















#from Fixture.db import DbFixture

#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
    #contacts = db.get_contact_list()
    #for contact in contacts:
        #print(contact)
    #print(len(contacts))
#finally:
    #db.destroy()