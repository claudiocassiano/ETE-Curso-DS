from time import sleep

def soma_dois_num():
    soma = n1 + n2
    print(f'A soma do número {n1} e do número {n2} é: {soma}')

def mult_dois_num():
    mult = n1 * n2
    print('A multiplicação do número {} e o número {} são: {}'.format(n1, n2, mult))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(soma_dois_num())
print(mult_dois_num())

nome = input("Diga seu nome: ")
print('Processando...............')
sleep(2)
print("Seu nome é: {}".format(nome))

# Continuando os exercícios
# continuar 