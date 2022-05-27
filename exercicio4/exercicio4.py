print('Bem-vindo ao Controle de Estoque da Bicicletária do Matheus Willian França')

# cadastro das peças
peca = {}
pecas = []


def cadastraPeca(): # função para cadastrar a peça
    while True: # loop
        print('Você Selecionou a opção cadastrar')
        try:
            for i in range(4): # loop para o cadastro de peças
                codigo = len(pecas) + 1 # captura o length do numero de peças cadastradas e adiciona + 1
                peca['Codigo'] = codigo
                print('Código da Peça é: {}'.format(codigo))
                peca['Nome:'] = input('Por favor entre com o nome da peça')
                peca['Fabricante'] = input('Por favor entre com o FABRICANTE da peça')
                peca['Valor'] = float(input('Por favor entre com o VALOR(R$) da Peça'))
                pecas.append(peca.copy()) #adiciona a lista cadastrada ao dicionário peças
                return
        except ValueError: #captura o erro de digitação do usuário
            print('Caracter inválido')
            continue


def consultarPeca(): # função para consultar a peças
    while True:
        try:
            print('Você selecionou a opção de consultar peças')
            consultar = int(input('Entre com a opção desejada:\n' #input para o menu desejado
                                '1-Consultar Todas as Peças\n'
                                '2-Consultar Peças por código\n'
                                '3-Consultar peças por Fabricante\n'
                                '4-Retornar\n'))
            if consultar == 1:
                for peca in pecas: # o loop percore todas as peças cadastradas
                    print('---------')
                    for key, value in peca.items():  #printa para o usuário todas as peças
                        print('{} : {}'.format(key, value))

            elif consultar == 2:
                codigoPeca = int(input('Digite o CÓDIGO da Peça:'))
                for peca in pecas: # o loop percore todas as peças cadastradas
                    print('---------')
                    if(peca['Codigo'] == codigoPeca):# o loop percore todas as pecas que estiveram com o código digitado pelo usuário
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
               
            elif consultar == 3:
                fabricante = input('Digite o FABRICANTE da Peça:')
                for peca in pecas:
                    print('---------')
                    if(peca['Fabricante'] == fabricante): # o loop percore todas as pecas que estiveram com o nome do fabricante cadastrado
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
               
            elif consultar == 4: # se o usuário digitar 4, ele retorna para o começo do menu
                return
            else:
                print('opção desconhecida, tente novamente.')

        except ValueError:
            print('Opção inválida... tente novamente')
            continue

def removerPeca():
    print('Você selecionou a opção de remover a peça')
    entrada = int(input('Digite o código da peça que deseja remover:')) # captura a entrada do código da peça
    for peca in pecas: # Percorre todas as peças cadastradas
        if(peca['Codigo'] == entrada): # verifica código digitado pelo usuário
            pecas.remove(peca) # remove a peça pelo numero do código
            print('Peça removida com sucesso!')


def editarCadastroPeca():
    print('Você selecinou a opção de editar o cadastro')
    entrada = int(input('Digite o código da peça'))
    for peca in pecas:
        if(peca['Codigo'] == entrada):
                pecas.remove(peca)
                peca['Nome:'] = input('Por favor entre com o novo nome da peça')
                peca['Fabricante'] = input('Por favor entre com o  novo FABRICANTE da peça')
                peca['Valor'] = float(input('Por favor entre com o  novo VALOR(R$) da Peça'))
                pecas.append(peca.copy())
                print('Cadastro editado com sucesso')
    return
while True: #Entrada principal dos menus
    try:
        opcao = int(input('Digite a opção desejada: \n'
                          '1-Cadastrar peça\n'
                          '2-Consultar peça\n'
                          '3-Remover peça\n'
                          '4-Editar dados já cadastrados\n'
                          '5-Sair''\n'))


        # verificação abaixo das entradas do usuário
        if opcao == 1:
            cadastraPeca()

        elif opcao == 2:
            consultarPeca()

        elif opcao == 3:
            removerPeca()

        elif opcao == 4:
            editarCadastroPeca()

        elif opcao == 5:
            print('Programa finalizado')
            break

        else:
            print('Você não digitou uma opcão inválida')
            print('Tente novamente')
            continue

    except ValueError:
        print('digite um caracter válido, tente novamente!') # captura o erro de digitação
        continue


