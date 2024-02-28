import os
os.system("cls")

ang1 = float(input('Digite o valor do primeiro ângulo: '))
ang2 = float(input('Digite o valor do segundo ângulo: '))
ang3 = float(input('Digite o valor do terceiro ângulo: '))

if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print('Triângulo retângulo')
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('Triângulo obtusângulo')
else:
    print('Triângulo acutângulo')