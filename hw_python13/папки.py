import os
import re

a = os.listdir('.')
k = 0
print('Что в папке:')
for item in a:
    print(str(item))
    path = ''
    path = os.path.join((os.path.abspath('.')), str(item))
    if os.path.isdir(path):
        if re.match('[А-Яа-я]', str(item)):
            k = k+1
print()
print('Папок, в названии которых только кириллические символы: ', k)
