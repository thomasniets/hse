with open ('freq.txt','r',encoding='utf-8')as n:
    k = 0
    for line in n:
        words = line.split(' | ')
        for i in range(len(words)):
            if (words[i] == 'сущ одуш ед жен им') or (words[i] == 'сущ неод ед жен им') or (words[i] == 'сущ ед жен им'):
                print(words[i-1])
                k = k + float(words[i+1])
    print(k)
