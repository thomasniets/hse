n = input()
i = len(n)-1
while i>=0:
    if (n[i]!='з')and(n[i]!='я'):
        print(n[i])
        i -= 1
    else:
        i -= 1
