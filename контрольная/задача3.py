words = []
while True:
    nextword = input('Введите слово ')
    if nextword == '':
        break
    else:
        words.append(nextword)
for i in range(len(words)):
    with open ('freq.txt','r',encoding='utf-8')as n:
        for line in n:
            wordss = line.split(' | ')
            for d in range(len(wordss)):
                slova = line.split()
                for s in range(len(slova)):
                    if slova[s] == words[i]:
                        print(wordss[i+1],wordss[i+2])
                    else:
                        print('Такого слова нет')

# я очень поздно поняла свои ошибки. открытие файла надо делать сначала,
# чтобы программа не бегала по тексту столько раз, сколько слов я ввела
