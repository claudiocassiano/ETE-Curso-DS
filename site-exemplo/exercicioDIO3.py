#     PRIMEIRA FORMA
""" n1 = int(input('Primeiro bimestre: '))
n2 = int(input('Segundo bimestre: '))
n3 = int(input('Terceiro bimestre: '))
n4 = int(input('Quarto bimestre: '))

media = int(n1 + n2 + n3 + n4) / 4

if n1 <= 10 and n2 <= 10 and n3 <= 10 and n4 <= 10:
    print('A média foi: {}'.format(media))
else:
    print('Foi digitada alguma nota errada!!!') """
#    Segunda forma

n1 = int(input('Primeiro bimestre: '))
if n1 > 10:
    n1 = int(input('Você digitou errado. Primeiro bimestre: '))
    # FALTA COLOCAR NAS OUTRAS NOTAS ABAIXO
n2 = int(input('Segundo bimestre: '))
if n2 > 10:
    N2 = int(input('Você digitou errado. Segundo bimestre: '))
    
n3 = int(input('Terceiro bimestre: '))
if n3 > 10:
    n3 = int(input('Você digitou errado. Terceiro bimestre: '))

n4 = int(input('Quarto bimestre: '))
if n4 > 10:
    n4 = int(input('Você digitou errado. Quarto bimestre: '))
    

media = int(n1 + n2 + n3 + n4) / 4
print('A média é: {}'.format(media))


