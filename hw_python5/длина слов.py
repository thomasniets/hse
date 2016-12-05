with open ('words.txt','r',encoding='utf-8')as n:
    kol1 = 0
    kol3 = 0
    for line in n:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 1:
                kol1 = kol1 + 1
            if len(words[i]) == 3:
                kol3 = kol3 + 1
    if kol1 == 0:
        print('Нет слов длины 1')
    else:
        print('Слов длины 3 больше, чем слов длины 1, в ' + str(kol3/kol1) + ' р.')
