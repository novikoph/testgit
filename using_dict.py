ab = { 'Swaroop'   : 'swaroop@swaroop.com',
       'Larry'     : 'larry@wall.com',
       'Matsumoto' : 'matz@ruby.com',
       'Spammer'   : 'spam@mail.com'
}

print('Adress Swaroop', ab['Swaroop'])

del ab['Spammer']

print('\nIn adress book {0} contacts\n'.format(len(ab)))

for name, adress in ab.items():
    print('Contact {0} with adress {1}'.format(name, adress))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s adress:', ab['Guido'])