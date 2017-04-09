def open_f():
    f = open('text.txt', 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    a = s.split()
    a = [word.strip('!?();:<>,."“”»«— ') for i,word in enumerate(a)]
    return a

def printing(t):
    for word in t:
        template = '{}'
        print (template.format(str(word) + '_' + str(len(str(word)))))

def main():
    text = open_f()
    printing(text)
main()

if __name__ == '__main__':
    main()
