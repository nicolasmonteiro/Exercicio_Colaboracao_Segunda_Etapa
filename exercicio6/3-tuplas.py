'''
maria tem uma tupla com consoantes ('b','d','f','l','m')
e uma com vogais ('a','e','i','o','u') e quer formar as silabas com essas letras.
'''
consoantes = ('b', 'd', 'f', 'l', 'm')
vogais = ('a', 'e', 'i', 'o', 'u')
print('-'*2, 'Formando as sílabas', '-'*2)
for c in range(0, 5):
    for v in range(0, 5):
        print('-'*10, consoantes[c], vogais[v], '-'*10)
