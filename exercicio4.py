print('Bem-vindo ao Controle de Estoque da Bicicletária do Matheus Willian França')
print('Escolha a opção desejada:')
'''
remover = int(input('3 - Remover Peças'))
sair = int(input('4 - Sair'))
'''

#cadastro das peças

loja = {'codigo': [], 'nomePeca': [], 'fabricante':[], 'valor': []}



def cadastraPeca():
    while True:
        cadastrar = int(input('1 - Cadastrar Peças'))
        try:
            for i in range(4):
                codigo = len(loja['codigo']) + 1
                print('Seu codigo é {}'.format(codigo))
                print('Você Selecionou a opção cadastrar')
                nomePeca = input('Por favor entre com o nome da peça')    
                fabricante = input('Por favor entre com o FABRICANTE da peça')
                valor = input('Por favor entre com o VALOR(R$) da Peça')
                loja['nomePeca'].append(nomePeca)
                loja['fabricante'].append(fabricante)
                loja['valor'].append(valor)
                loja['codigo'].append(codigo)
                print(loja)
                break
        except ValueError:
            print('Caracter inválido')
            
        finally:
            continue
    
            
cadastraPeca()


'''
def consultarPeca():
    while True:
        consultar = int(input('2 - Consultar Peças'))
        try:
'''