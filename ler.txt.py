# Microatividade 04

# ler = open('loremipsum.txt', 'r')

with open('loremipsum.txt', 'r') as ler:
    conteudo = ler.read()

print(conteudo)

print()
print()

conteudo = ler.readlines()

print('primeira linha')

print(0)
print()
print()
