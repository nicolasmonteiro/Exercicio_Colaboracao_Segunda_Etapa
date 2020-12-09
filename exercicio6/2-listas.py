'''
joao precisa atualizar a lista de empregados da sua firma.
lista antiga ("maria","joao","pedro","ana","jose","miguel","ester","leticia","marcos","matheus")
para isso ele precisa tirar  quatro nomes, alternadamente e depois incluir os novos
nomes (bruce, clark, diana, peter, henri).
'''
# Eu interpretei que não precisava colocar os novos nomes nas posições respectivas que foram removidas.
# Não ficou tão claro pra mim, fiz da maneira como interpretei.

cont = 0
antiga = ["maria", "joao", "pedro", "ana", "jose",
          "miguel", "ester", "leticia", "marcos", "matheus"]
novo = []
novosfunc = ['bruce', 'clark', 'diana', 'peter', 'henri']
print('Antigo quadro de funcionários')
for a in antiga:
    cont += 1
    print(cont, '-', a)
cont = 0
print('Quadro reduzido de funcionários')
for e in range(0, len(antiga), 2):
    cont += 1
    print(cont, '-', antiga[e])
    novo.append(antiga[e])
    final = novo+novosfunc
cont = 0
print('Novo Quadro de funcionários')
for f in final:
    cont += 1
    print(cont, '-', f)
