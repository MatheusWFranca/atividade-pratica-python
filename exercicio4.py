from random import randint

print('Bem-vindo ao Controle de Estoque da Bicicletária do Matheus Willian França')

# cadastro das peças

peca = {}
pecas = []


def cadastraPeca():
    while True:
        print('Você Selecionou a opção cadastrar')
        try:
            for i in range(4):
                codigo = len(pecas) + 1
                peca['Codigo'] = codigo
                print('Seu codigo é {}'.format(codigo))
                peca['Nome:'] = input('Por favor entre com o nome da peça')
                peca['Fabricante'] = input('Por favor entre com o FABRICANTE da peça')
                peca['Valor'] = input('Por favor entre com o VALOR(R$) da Peça')
                pecas.append(peca.copy())
                return
        except ValueError:
            print('Caracter inválido')
            continue


def consultarPeca():
    while True:
        try:
            print('Você selecionou a opção de consultar peças')
            consultar = int(input('Entre com a opção desejada:\n'
                                '1-Consultar Todas as Peças\n'
                                '2-Consultar Peças por código\n'
                                '3-Consultar peças por Fabricate\n'
                                '4-Retornar\n'))
            if consultar == 1:
                print('-------')
                for peca in pecas:
                    for key, value in peca.items():
                        print('{} : {}'.format(key, value))

            elif consultar == 2:
                codigoPeca = int(input('Digite o CÓDIGO da Peça:'))
            elif consultar == 3:
                fabricante = int(input('Digite o FABRICANTE da Peça:'))
            elif consultar == 4:
                return
            else:
                print('opção desconhecida, tente novamente.')

        except ValueError:
            print('')


while True:
    try:
        opcao = int(input('Digite a opção desejada: \n'
                          '1-Cadastrar peça\n'
                          '2-Consultar peça\n'
                          '3-Remover peça\n'
                          '4-Sair''\n'))

        if opcao == 1:
            cadastraPeca()

        elif opcao == 2:
            consultarPeca()

        elif opcao == 3:
            removerPeca()

        elif opcao == 4:
            print('Programa finalizado')

        else:
            print('Você não digitou uma opcão inválida')
            print('Tente novamente')
            continue

    except ValueError:
        print('digite um caracter inválido, tente novamente!')
        continue


