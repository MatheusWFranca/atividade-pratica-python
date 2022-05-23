print('Bem-vindo a companhia de Logistica Matheus Willian França')


def dimensoesObjeto():
    while True:
        try:
            comprimento = float(input('Digite o comprimento do objeto (Em CM)'))
            largura = float(input('Digite o largura do objeto (Em CM)'))
            altura = float(input('Digite a altura do objeto (Em CM)'))
            volume = comprimento * largura * altura
            print('Volume do seu objeto é {} cm3'.format(volume))
            if (volume < 1000):
                return 10

            elif (volume >= 1000 and volume <= 10000):
                return 20

            elif (volume >= 10000 and volume <= 30000):
                return 30

            elif (volume >= 30000 and volume <= 100000):
                return 50

            else:
                print('Não aceitamos objetos com dimensões tão grandes...')
                print('Entre com as dimensões novamente')
                continue
        except ValueError:
            print('Você digitou as dimensões com valor não numérico')
            print('Entre com as dimensões corretas novamente')
            continue


def peso():
    while True:
        try:
            objetoPeso = float(input('Digite o peso'))
            if (objetoPeso < 0.1):
                return 1
            elif (objetoPeso > 0.1 and objetoPeso < 1):
                return 1.5
            elif (objetoPeso >= 1 and objetoPeso < 10):
                return 2
            elif (objetoPeso >= 10 and objetoPeso < 30):
                return 3
            else:
                print('Não aceitamos objetos tão pesados...')
                print('Entre com o peso novamente')
                continue
        except ValueError:
            print('Você digitou o peso com valor não numérico')
            print('Entre com o peso novamente')
            continue


def tarifas():
    while True:
        try:
            print('BR - De Brasília para Rio de Janeiro')
            print('BS - De Brasília para São paulo')
            print('RB - De Rio de Janeiro para Brasília')
            print('RS - De Rio de Janeiro para São Paulo')
            print('SR - De São Paulo para Rio de Janeiro')
            print('SB - De São Paula para Brasília')
            rota = input('Digite a rota desejada')
            if rota == 'BR':
                return 1.5
            elif rota == 'BS':
                return 1.2
            elif rota == 'RB':
                return 1.5
            elif rota == 'RS':
                return 1
            elif rota == 'SR':
                return 1
            elif rota == 'SB':
                return 1.2
            else:
                print('Você digitou uma rota que não existe\n Digite novamente...')
        except ValueError:
            print('Digitou uma rota que não existe\n ')


dimensoesFinal = dimensoesObjeto()
pesoFinal = peso()
tarifasFinal = tarifas()

print('Total a pagar: R${} (dimensões {} * peso: {} * rota: {:.2f})'.format((dimensoesFinal * pesoFinal * tarifasFinal), dimensoesFinal, pesoFinal, tarifasFinal))

