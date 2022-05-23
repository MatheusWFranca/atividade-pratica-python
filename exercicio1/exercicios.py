print('Bem-vindo a loja do Matheus Willian França')

valorUnitario = int(input('Digite o valor unitário do produto')) #caputura o valor unitário
quantidade = int(input('Digite a quantidade que deseja')) #captura a quantidade 
total = valorUnitario * quantidade # total 

print('O valor sem desconto é R${:.2f}'.format(total)) # printa para o usuário o valor sem desconto


#verifica a quantidade selecionada se está dentra as opções de desconto
if quantidade >= 10 and quantidade <= 99 :  
    desconto = total - (total * 0.05)
    print('O valor com 5% de desconto é R${:.2f} '.format(desconto))
elif quantidade >= 100 and quantidade < 999:
    desconto = total - (total * 0.10)
    print('O valor com 10% de desconto é R${:.2f}'.format(desconto))
elif(quantidade >= 1000):
    desconto = total - (total * 0.15)
    print('O valor com 15% de desconto é R${:.2f} '.format(desconto))
else: # caso nenhumas das opções atenda, ele entra no else (valor sem desconto)
    print('O valor total sem desconto foi de: R$ {:.2f}, adicione mais quantidades para ganhar descontos.'.format(valorUnitario * quantidade))

