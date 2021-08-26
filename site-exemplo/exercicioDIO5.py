"""
a = 0
while a <= 10:
    print(a)
    a += 1
"""

nota1 = int(input('Digite uma nota de 0 a 10: '))
while nota1 > 10:
    nota1 = int(input('Nota inválida. Entre com a nota correta: '))
nota2 = int(input('Digite uma nota de 0 a 10: '))
while nota2 > 10:
    nota2 = int(input('Nota inválida. Entre com a nota correta: '))

soma = nota1 + nota2

print("A soma é: {}".format(soma))


