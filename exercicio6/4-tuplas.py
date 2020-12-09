'''
ester vai começar a fazer academia e suas aulas serão 3 vezes na semana
domingo, terca e quinta. use tuplas pra mostrar os dias da
semana que terao aulas imprimindo uma mensagem de lembrete.
 ('domingo','segunda','terça','quarta','quinta','sexta','sabado')
'''
cont = 0
dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
print('Programação semanal')
print('-'*19)
for d in dias:
    if d == dias[0] or d == dias[2] or d == dias[4]:
        cont += 1
        print(f'{cont}-Hoje é dia treino:')
    print(d)
    print('-'*19)
