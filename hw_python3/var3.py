words = []
while True:
    nextword = input('Введите слово ')
    if nextword == '':
        break
    else:
        words.append(nextword)
for i in range(len(words)):
    string = words[i]
    print(string[i+1:])
