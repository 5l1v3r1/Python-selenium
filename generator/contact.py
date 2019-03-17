from Model.address import address
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "../data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

Testdata = [address(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), \
                    Address=random_string("Address", 20), mobilephone=random_string("mobilephone", 20), \
                    email1=random_string("email", 20) ) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(Testdata))