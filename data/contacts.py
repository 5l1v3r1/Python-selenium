from Model.address import address
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

Testdata = [address(firstname='', lastname='', Address='', mobilephone='', email1='')] + \
           [address(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), \
                    Address=random_string("Address", 20), mobilephone=random_string("mobilephone", 20), \
                    email1=random_string("email", 20) ) for i in range(2)]