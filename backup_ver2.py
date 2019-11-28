import os
import time

source = '/Users/kophmachine/PycharmProjects/CopyFromHere'
target_dir = '/Users/kophmachine/PycharmProjects/CopyThere'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
print('Успешно создан каталог', today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось!')