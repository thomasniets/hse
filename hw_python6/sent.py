##У МЕНЯ НИЧЕГО НЕ ПОЛУЧИЛОСЬ, НО Я ПОСМЕЯЛАСЬ

import random

def nouns1():
    nouns1 = ['травы','таблеток','мескалина','кислоты','кокаина','транквилизаторов','сортов','расцветок','текилы','рома','пива','эфира','амилнитрита','поездки','дури','опасения','зомби','дряни','крошек']
    return random.choice(nouns1)

def nouns2():
    nouns2 = ['пакетики','упаковки','множества','ящики','пинты','запасы','вокзалы']
    return random.choice(nouns2) 

def adverbs():
    adverbs = ['трудно','рано','поздно','скоро','довольно','интересно','скоро']
    return random.choice(adverbs)

def adjectives():
    adjectives = ['целые','необходимые','единственные','беспомощные','испорченные','эфирные','милые','летучие','бешеные','готовые']
    return random.choice(adjectives)

def imperatives():
    imperatives = ['будь как','переходи на','начинай','собирай','вызывай','знай','переходи на','коллекционируй','окунись в','втыкай в','залезай в']
    return random.choice(imperatives)

def verbs_past():
    verbs_past = ['были как','перешли на','собрали','стали как','вызвали','знали','коллекционировали','окунулись в','втыкали в','залезли в']
    return random.choice(verbs_past)
def verbs_past_2():
    verbs_past_2 = ['принимали','поощрали','одобряли','понимали']
    return random.choice(verbs_past_2)

def inf():
    inf = ['быть','переходить','начать','собрать','стать','остановиться','вызвать','знать','перейти','коллекционировать','окунуться в','втыкать','залезть в','умереть','жить']
    return random.choice(inf)
def nach():
    nach = ['Мигом ','Бегом ','Скорее ','Иди, ']
    return random.choice(nach)


def utv_sentence():
    sentence = 'Мы ' + adverbs() + ' ' + verbs_past() + ' ' + adjectives() + ' ' + nouns2() + ' ' + nouns1() + '.'
    return sentence

def otr_sentence():
    sentence = 'Они не ' + verbs_past() + ' ' + adjectives() + ' ' + nouns2() + ' ' + nouns1() + ', а мы такое не ' + verbs_past_2() + '.'
    return sentence

def usl_sentence():
    sentence = 'Если вы ещё не ' + verbs_past() + ' ' + adjectives() + ' ' + nouns2() + ' ' + nouns1() + ', можете ' + adverbs() + ' ' + inf() + '.'
    return sentence

def pob_sentence():
    sentence = nach() + imperatives() + ' ' + nouns2() + ' ' + nouns1() + '!'
    return sentence
def vop_sentence():
    sentence = 'Знаете ли вы, как ' + adverbs() + ' ' + inf() + ' ' + nouns2() + '?'
    return sentence


spisok = []
spisok.append(utv_sentence())
spisok.append(otr_sentence())
spisok.append(pob_sentence())
spisok.append(usl_sentence())
spisok.append(vop_sentence())
new_spisok = list(spisok)
random.shuffle(new_spisok)
for word in new_spisok:
    print(word)
