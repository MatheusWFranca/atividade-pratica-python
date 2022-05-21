from calendar import c
from operator import iand
from tokenize import Number


print('Bem-vindo a companhia de Logistica Matheus Willian França')


tarifa = 0
peso_final = 0

while True:
    try:
        comprimento = int(input('Digite o comprimento do objeto (Em CM)'))
        largura = int(input('Digite o largura do objeto (Em CM)'))
        altura = int(input('Digite a altura do objeto (Em CM)'))
        volume = comprimento * largura * altura
        print('Volume do seu objeto é de objeto {} cm3'.format(volume))

        if(volume > 0):
            if(volume <= 1000):
                tarifa += 10
        
            elif(volume  >= 1000 and volume <= 10000):
                tarifa += 20

            elif(volume >= 10000 and volume <= 30000):
                tarifa += 30

            elif(volume >= 30000 and volume <= 100000):
                tarifa += 50
        
            else:
                print('Não aceitamos objetos com valores tão grandes...')
                print('Entre com as dimensões novamente')
              
        else:
            print('Objeto com metragem cubica menor que 1\n Digite novamente...')
            continue
    except ValueError:
        print('Digite um valor válido...')
        print('Entre com as dimensões corretas novamente')
    
    try:
        peso = int(input('Digite o peso do objeto'))    
        if(peso > 10000):
            print('Não trabalhos com objeto pesados.. \n tenta novamente')
        else:
            peso = peso_final
        print('o peso do seu objeto é de {}'.format(peso))
        
    except ValueError:
        print('Você digitou o peso  com caracter invalido')

