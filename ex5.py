import os
os.system("cls")

valor1 = int(input("valor 1:"))
valor2 = int(input("valor 2:"))
valor3 = int(input("valor 3:"))

if valor1 > valor2 and valor1 > valor3:
        if valor2 > valor3:
                print(str(valor1) + ' ' + str(valor2) + ' ' + str(valor3))
        else:
                print(str(valor1) + ' ' + str(valor3) + ' ' + str(valor2))
elif valor2 > valor3:
        if valor3 > valor1:
                print(str(valor2) + ' ' + str(valor3) + ' ' + str(valor1))
        else:
                print(str(valor2) + ' ' + str(valor1) + ' ' + str(valor3))
elif valor1 > valor2:
        print(str(valor3) + ' ' + str(valor1) + ' ' + str(valor2))
else:
        print(str(valor3) + ' ' + str(valor2) + ' ' + str(valor1))