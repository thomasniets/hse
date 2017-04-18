import os

max1 = 0
otvet = ''
extensions = []
for root, dirs, files in os.walk('.'):
    for f in files:
        f = f.split('.')
        if len(f) == 2:
            extensions.append(f[1])
            for item in extensions:
                if extensions.count(item) > max1:
                    max1 = extensions.count(item)
                    otvet = item
print('Чаще всего встречаются файлы с расширением ' + otvet)

