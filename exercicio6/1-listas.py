'''
joaquim coleciona filmes no computador, mas quer gravar alguns em cd,
precisar organizar sua lista por ordem alfabetica e gravar os cinco 
primeiros. (mae, vida, nos, eli, vidro, resgate, close, o poço, fragmentado, parasita).
'''
import time

filmes = ['mae', 'vida', 'nos', 'eli', 'vidro', 'resgate',
          'close', 'o poco', 'fragmentado', 'parasita']
gravados = []
cont = 0
print('-'*5, 'Lista de Filmes', '-'*5)
for f in sorted(filmes):
    cont += 1
    print(cont, '-', f)
    if cont <= 5:
        gravados.append(f)
print('-'*5, '5 primeiros filmes', '-'*5)
print('Iniciando gravação dos seguintes filmes')
cont = 0
for g in sorted(gravados):
    cont += 1
    print(cont, '-', g)
print('Gravando...')
for l in range(1, 101):
    print(l, '%')
    time.sleep(1)
print('Gravação concluída.')
