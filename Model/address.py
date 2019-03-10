from sys import maxsize

class address:
    def __init__(self, firstname=None, lastname=None, nickname=None,
                 location=None, email=None, homephone=None, workphone=None,
                 all_phones_from_homepage=None, mobilephone=None, secondphone=None,id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.location = location
        self.email = email
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondphone = secondphone
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage


    def __repr__(self):
        return "%s:%s:%s:" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize