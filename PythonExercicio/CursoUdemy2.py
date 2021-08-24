def func_nome(nome, idade):
    print('Meu nome é '+ nome +'.')
    print('Eu tenho ' + idade +' anos.')


func_nome('João','32')
func_nome('Carlos','64')
func_nome('Amanda', '32')
func_nome('Cláudio', '43')

numero = 10
print(type(numero))

def sumario():
    global numero #Global torna acesivel a todos
    numero = 20  #Número local 
    print('Inicial: ' + str(numero))


sumario()
print('Final: ' + str(numero))
