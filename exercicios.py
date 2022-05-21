print('Bem-vindo a loja do Matheus Willian França')

valorUnitario = int(input('Digite o valor unitário do produto'))
quantidade = int(input('Digite a quantidade que deseja'))
total = valorUnitario * quantidade

print('O valor sem desconto é: {}'.format(total))

if quantidade >= 10 and quantidade <= 99 :
    desconto = total - (total * 0.05)
    print('O valor com 5% de desconto é: {} '.format(desconto))
elif quantidade >= 100 and quantidade < 999:
    desconto = total - (total * 0.10)
    print('O valor com 10% de desconto é: {}'.format(desconto))
elif(quantidade >= 1000):
    desconto = total - (total * 0.15)
    print('O valor com 15% de desconto é {} '.format(desconto))
else:
    print('O valor total sem desconto foi de: R$ {}, adicione mais quantidades para ganhar descontos.'.format(valorUnitario * quantidade))

