print('Bem-vindo a lanchonete')
print('+', '-' * 35, '+')
print('codigo |       Descrição       | Valor')
print('100    |     Cachorro-Quente   | R$ 9')
print('101    | Cachorro-Quente Duplo | R$ 11')
print('102    |        X-Egg          | R$ 12')
print('103    |      X-Salada         | R$ 13')
print('104    |       X-Bacon         | R$ 14')
print('105    |       X-Tudo          | R$ 17')
print('200    |    Frigerante Lata    | R$ 5')
print('201    |      Chá Gelado       | R$ 4')


total = 0

while True:
    produto = int(input('Entre com o produto desejado'))
    if(produto == 100):
        total += 9
        print('Você escolheu Cachorro-Quente no valor de R$ 9,00 ')
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break

    elif(produto == 101):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break

    elif(produto == 102):
        print('Você escolheu X-Egg no valor de R$ 12,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break

    elif(produto == 103):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break
    elif(produto == 102):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break

    elif(produto == 102):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break

    elif(produto == 102):
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00 ')
        total+= 11
        recomprar = input('Você deseja pedir mais alguma coisa? [S/N]')
        if(recomprar == 'S'):
            continue   
        else:    
            print('O total da sua compra foi: R$ {}'.format(total))    
            break
    else:
        print('Opção invalida... voltando para o menu principal')
        continue