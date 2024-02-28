import os
os.system("cls")

altura = float(input("Digite sua altura em cm: "))
sexo = int(input('Digite seu sexo (1 para feminino e 2 para masculino): '))

if sexo == 1:
        peso = 62.1 * (altura / 100) - 44.7
else:
        peso = 72.2 * (altura / 100) - 58

print('Seu peso ideal é ' + str(peso))