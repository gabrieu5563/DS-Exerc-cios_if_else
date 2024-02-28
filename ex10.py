import os
os.system("cls")

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print('O triângulo é equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é escaleno")
else:
    print("O triângulo é isosceles")