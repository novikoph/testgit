import sys
import warnings

if sys.version_info[0] < 3:
    warnings.warn('Для выполнения этой команды необходима, как минимум, \
                  версия Python 3.0', RuntimeWarning)
else:
    print('Нормальное продолжение.')