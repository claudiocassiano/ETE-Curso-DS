
a = int(input('Digite um número: '))
b = int(input('Digite ouro número: '))
c = int(input('Digite mais um número: '))

if a > b and a > c:
    print('O número {} é maior que o número {} e {}.'.format(a, b, c))
elif b > a and b > c:
    print('O número {} é maior que o número {} e {}.'.format(b, a, c))
else:
    print('O número {} é maio que o número {} e {}'.format(c, b, a))
print('Fim do programa.')





