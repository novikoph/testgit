try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну и зачем вы мне сделали EOF?')
except KeyboardInterrupt:
    print('Вы отменили опреацию.')
else:
    print('Вы ввели: {0}'.format(text))
