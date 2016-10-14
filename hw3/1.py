print('Введите числа')
a = input()
b = input()
c = input()

if float(b) == 0:
    if float(b) < 0:
        d = '(' + b + ')'
    else:
        d = b
    if float(c) < 0:
        s = a + '*' + '(' + c + ')'
    else:
        s = a + '*' + c
    if float(a) * float(c) + float(b) == 0:
        print(c + ' является решением линейного уравнения ' + s + ' + ' + d + ' = 0')
    else:
        print(c + ' не является решением линейного уравнения ' + s + ' + ' + d + ' = 0')
else:
    if float(a) % float(b) == float(c):
        print(a + ' даёт остаток ' + c + ' при делении на ' + b)
    else:
        print(a + ' не даёт остаток ' + c + ' при делении на ' + b)
    if float(b) < 0:
        d = '(' + b + ')'
    else:
        d = b
    if float(c) < 0:
        s = a + '*' + '(' + c + ')'
    else:
        s = a + '*' + c
    if float(a) * float(c) + float(b) == 0:
        print(c + ' является решением линейного уравнения ' + s + ' + ' + d + ' = 0')
    else:
        print(c + ' не является решением линейного уравнения ' + s + ' + ' + d + ' = 0')
