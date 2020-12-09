'''
ana tem uma lanchonete e quer fazer um menu eletronico onde as pessoas
possam ver o que querem escolher por nome ou pelo preço.
menu real{'hamburguer':5,'hotdog':5,'empada':3,'coxinha':3,'açai':8,'esfirra':7,'pastel':6,'bolo':5,'torta':8}
'''
cardapio = {'hamburguer': 5, 'hotdog': 5, 'empada': 3, 'coxinha': 3,
            'açai': 8, 'esfirra': 7, 'pastel': 6, 'bolo': 5, 'torta': 8}

while True:
    print('§'*13, 'Cardápio', '§'*13)
    print('§'*2, 'Seja bem vindo a Ana Lanches!', '§'*2)
    print('Escolha a forma de consultar o menu:')
    print('Por: 1- Nome 2- Preço  3- Ambos:')
    opcao = int(input('Informe sua escolha(1 ou 2 ou 3):'))
    if opcao == 1:
        print('§'*14, 'Lanches', '§'*14)
        for k in cardapio.keys():
            print('-'*13, k, '-'*13)
    elif opcao == 2:
        print('§'*12, 'Preços', '§'*12)
        for v in cardapio.values():
            print('-'*13, 'R$', v, '-'*13)
    elif opcao == 3:
        print('§'*13, 'Cardápio - Ana Lanches', '§'*13)
        for k, v in cardapio.items():
            print('-'*13, f'{k} = R$ {v}', '-'*13)
    continua = str(input('Deseja continuar?(s/n) '))
    if continua == 'n':
        print('Obrigado pela preferência, volte sempre!')
        break
