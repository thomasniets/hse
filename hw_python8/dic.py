def read_file():
    f = open("slova.csv", 'r', encoding = "utf-8")
    a = f.readlines()
    f.close()
    return(a)

def make_dict(a):
    words = {}
    for line in a:
        a2 = line.split(',')
        for i, d in enumerate(a2):
            a2[i] = d.strip()
        words[a2[1]] = a2[0]
    return words

def guess(dic):
    for noun in dic:
        print(dic[noun], '...')
        att = 0
        while att != len(dic[noun]):
            print('Осталось', len(dic[noun]) - att ,'попыток')
            att += 1
            if input() == noun:
                print('Ты умный котик! c:')
                att = len(dic[noun])
            elif len(dic[noun]) - att == 0:
                print('Увы, это не так >:')

def main():
    text = read_file()
    words = make_dict(text)
    guess(words)

main()
         
