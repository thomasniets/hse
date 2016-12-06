with open ('freq.txt','r',encoding='utf-8')as n:
    k = 0
    s = []
    for line in n:
        words = line.split(' | ')
        for i in range(len(words)):
            if words[i] == 'союз':
                print(line)
