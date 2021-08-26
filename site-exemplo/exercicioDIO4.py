"""
a = int(input('Digite um número: '))

div = 0
for x in range(1, a+1):
    resto = a % x 
    print('{} / {} = {}.'.format(a, x, resto))
    if resto == 0:
        div = div + 1

if div == 2:
    print('O número {} é primo, pois é divisivel por 1 \ne por ele mesmo.'.format(a))
else:
    print('O número {} não é primo.'.format(a))
"""
#    Outra forma FOR dentro de FOR

a = int(input('Digite até que número você quer ver se é primo: '))
for num in range(a + 1):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
             div += 1
    if div == 2:
        print('{} é primo.'.format(num))

print('Fim do programa!!!')
    



