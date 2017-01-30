import re

def main():
    dic = []
    p = re.compile('программир(у(ют?|й|йте|е(шь|те?|м(ы([ейхм]|ми)|ая|о([ейм]|го|му)))|я|ющ(ая|и(й|е(й|го|му|м)))|ое|ие|ую|и(м|х|ми))|овал([аи])|овать)(с[ья])?')
    with open('прогю.txt', 'r', encoding = 'utf-8') as f:
        for line in f.readlines():
            words = [word.strip(',.:;!?-"').lower() for word in line.split() if word]
            dic += [p.fullmatch(word) for word in words]
        dic = [i.group() for i in dic if i]
    print('\n'.join(set(dic)))

if __name__ == '__main__':
    main()
