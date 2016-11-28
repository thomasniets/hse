fword = input('Введите слово ')
sword = ''
for i in range(len(fword)):
    for s in range(len(fword)):
        if s + i < len(fword):
            sword += fword[s + i]
        else:
            sword += fword[s + i - len(fword)]
    print (sword)
    sword = ''
