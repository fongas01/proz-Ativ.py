'''
Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
Porém, o dono do hotel é supersticioso e optou por não ter um 13º andar.

a) Escreva um código que imprima todos os números exceto o número 13.
b) Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
c) Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
'''

# RESOLUÇÃO:

# Imprimindo (print) o número de cada andar (De 1 a 21 atendendo os 20 andares)

# contador = i, porém i !13 para atender a supertição citada

# Usando FOR, atendemos a alínea a) do exercício
for i in range(1, 21):
    if i != 13:
        print(i)

# Usando WHILE, atendemos a alínea b) do exercício
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1

# imprimindo decrescentemente
for i in range(20, 0, -1):
    if i != 13:
        print(i)
