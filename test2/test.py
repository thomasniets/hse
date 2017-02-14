import re

def open_corpora(f):
    with open(f, 'r', encoding='utf-8') as f:
        return f.readlines()

def write(n, p):
    with open(n, 'w', encoding='utf-8') as f:
        f.write(p)
        
def count(corpora):
    k = 0
    for line in corpora:
        k = k + 1
    return(k)

def dic(corpora):
    dic = {}
    s = re.compile('type="([1-3a-zþ-]*)"')
    for line in corpora:
        if '<w lemma=' in line:
            w = s.findall(line)[0]
            if w in dic:
                dic[w] = dic[w] + 1
            else:
                dic[w] = 1
    return dic

def words(corpora):
    dic = []
    k = 0
    forms = re.compile('type="(?:l[1-3a-zþ-]f[1-3a-zþ-][1-3a-zþ-])">([AaGgOoVvÁáHhÓóWwBbIiPpXxCcÍíQqYyDdJjRrÝýÐðKkSsZzEeLlTtÞþÉéMmUuÆæFfNnÚúÖö]*)<')
    for line in corpora:
        word = forms.findall(line)
        if word:
            dic.append(word[0])
            
    return list(set(dic))



def main():
    corpora = open_corpora('F.xml')
    write('number.txt', str(count(corpora)))
    dictionary = dic(corpora)
    keys = ['{}'.format(key) for key in dictionary]
    write('keys.txt', ', '.join(keys))
    wordforms = words(corpora)
    write('adj.txt', ','.join(wordforms))

if __name__ == '__main__':
    main()
