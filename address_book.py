import pickle

bookfile = 'book.data'

class AddressBook:
    '''Представляет любого человека в книге.'''
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Contact(AddressBook):
    def __init__(self, name, address):
        AddressBook.__init__(self, name, address)
        ab = {name: address}
        f = open(bookfile, 'w')
        pickle.dump(ab, f)
        f.close()

adr = Contact('Tom', 'tb@.com')

f = open(bookfile, 'rb')
contacts = pickle.load(f)
print(contacts)