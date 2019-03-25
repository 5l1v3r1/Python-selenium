import pymysql.cursors
from Model.group import Group
from Model.contact import Contact
class DbFixture:
    def __init__(self, host, name, user, password):
        self.user = user
        self.name = name
        self.host = host
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list.append(Group(id=str(id), header=header, footer=footer, name=name))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, mobile from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, mobile) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, mobile=mobile, email=email))
        finally:
            cursor.close()
        return list

    def get_contact_full_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, all_phones_from_home_page=home + mobile + work + phone2, all_emails_from_home_page=email + email2 + email3))
        finally:
            cursor.close()
        return list


    def get_list_of_groups_names_and_ids(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()