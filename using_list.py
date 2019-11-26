shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('я должен сделать', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь список покупок таков: ', shoplist)

print('Отсортирую-ка свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так: ', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)