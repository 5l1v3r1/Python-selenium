from sys import maxsize

class address:
    def __init__(self, firstname=None, lastname=None, nickname=None, location=None, email=None, phone=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.location = location
        self.email = email
        self.phone = phone
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.phone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.phone == other.phone

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize