
'''
lurdes tem um brecho e quer um programa que armazene todas as suas peças
com seus respectivos preços, e que ela possa excluir e incluir itens depois.
use um dicionario e um menu com opções de incluir e excluir.
{'calça':50,'saia':40,'vestido':80,'short':30,'top':20,'blusa':45,'camisa':35,'bolsa':60,'sandalia':25}
'''
import os

import time

brecho = {'calca': 50, 'saia': 40, 'vestido': 80, 'short': 30,
          'top': 20, 'blusa': 45, 'camisa': 35, 'bolsa': 60, 'sandalia': 25}
lista = []


def cls():
    return os.system('cls')


def atualizada():
    print('§'*15, 'Brechó - Itens atualizados', '§'*15)
    for k, v in brecho.items():
        print('-'*15, f'{k} = R$ {v}', '-'*15)


while True:
    atualizada()
    print('§'*15, 'Escolha a opção desejada', '§'*15)
    opcao = str(input('1-Adicionar, 2- Remover, 3- Sair : '))
    cls()
    if opcao == '1':
        add = str(input('Deseja adicionar qual peça? '))
        preco = str(input('Qual o valor da peça? '))
        brecho[add] = preco
        print(
            f'O item {add} com preço: R$ {preco} , foi adicionado com sucesso!')
        atualizada()
        time.sleep(5)
        cls()
    if opcao == '2':
        apagar = str(input('Desejar apagar qual peça? '))
        copia = apagar
        del brecho[apagar]
        print(f'O item {copia} foi removido com sucesso!')
        atualizada()
        time.sleep(5)
        cls()
    if opcao == '3':
        atualizada()
        print('Obrigado Dona Lurdes, é um prazer lhe servir!')
        break
    sair = str(input('Deseja sair ?(s/n)'))
    cls()
    if sair == 's':
        cls()
        atualizada()
        print('Obrigado Dona Lurdes, é um prazer lhe servir!')
        break
