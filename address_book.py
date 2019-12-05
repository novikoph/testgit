import pickle

bookfile = 'book.data'

class AddressBook:
    '''Представляет любого человека в книге.'''
    def __init__(self, name, address):
        self.name = name
        self.address = address

class AddContact(AddressBook):
    def __init__(self, name, address):
        AddressBook.__init__(self, name, address)
        ab[name] = address

ab = {}

adr = AddContact('Tom', 'dsad@mail.com')
adr = AddContact('Dom', 'sad@mail.com')
adr = AddContact('Rom', 'rrr@mail.com')
adr = AddContact('Kom', 'kkk@mail.com')

del ab['Rom']

f = open(bookfile, 'wb')
pickle.dump(ab, f)
f.close()

f = open(bookfile, 'rb')
contacts = pickle.load(f)

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
