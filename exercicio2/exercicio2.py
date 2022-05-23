print('Bem-vindo a lanchonete de Matheus Willian França')
print('+', '-' * 35, '+')
print('Código |       Descrição       | Valor')
print('100    |     Cachorro-Quente   | R$ 9')
print('101    | Cachorro-Quente Duplo | R$ 11')
print('102    |        X-Egg          | R$ 12')
print('103    |      X-Salada         | R$ 13')
print('104    |       X-Bacon         | R$ 14')
print('105    |       X-Tudo          | R$ 17')
print('200    |   Refrigerante Lata   | R$ 5')
print('201    |      Chá Gelado       | R$ 4')

total = 0  # acomulador do carrinho

while True:  # laço de repetição para repetir os passos das perguntas ao usuário
    produto = int(input('Entre com o produto desejado'))  # pergunta ao usuário qual lanche ele deseja comprar
    if (produto == 100):  # se produto foi igual ao código
        print('Você escolheu Cachorro-Quente no valor de R$ 9,00 ')
        total += 9  # adiciona o total do produto ao acomulador "carrinho"

    elif (produto == 101):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total += 11

    elif (produto == 102):
        print('Você escolheu X-Egg no valor de R$ 12,00 ')
        total += 12

    elif (produto == 103):
        print('Você escolheu X-Salada no valor de R$ 12,00 ')
        total += 12

    elif (produto == 104):
        print('Você escolheu X-Bacon no valor de R$ 14,00 ')
        total += 14

    elif (produto == 105):
        print('Você escolheu X-Tudo no valor de R$ 17,00 ')
        total += 17

    elif (produto == 200):
        print('Você escolheu Refrigerante Lata no valor de R$ 5,00 ')
        total += 5

    elif (produto == 201):
        print('Você escolheu Chá Gelado no valor de R$ 4,00 ')
        total += 4

    else:  # tratar o erro se o usuário digitar algum caracter invalido ou código que não existe
        print('Você digitou um caracter inválido e/ou esse código não existe')
        continue

    recomprar = int(input('Você deseja pedir mais alguma coisa?\n'
                      '1 - Sim\n'
                      '0 - Não\n'))  # Perguntamos o usuário se ele deseja adicionar mais coisas

    if recomprar == 1:  # Se comprar, ele volta ao começo do laço
        continue
    elif recomprar == 0:  # Se ele digitar N, ele encerra o programa e mostra ao usuário total gasto
        print('O total da sua compra foi: R$ {:.2f}'.format(total))
        break
    else:  # tratar o erro se o usuário digitar algum caracter invalido ou código que não existe
        print('Você digitou um caracter inválido e/ou esse código não existe')
        continue

