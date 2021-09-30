
a = int(input('Um número: '))
b = int(input('Outro número: '))
#resto a = a % 2 primeiro IF
resto_a = a % 2
restO_b = b % 2
#Primeiro IF
#if resto == 0:
#    print('O número {} é par!')
#else:
#    print('Esse número é impar!')

if resto_a == 0 or restO_b == 0:
    print('Foi digitado um número par.')
else:
    print('Não foi digitado nenhum número par.')
