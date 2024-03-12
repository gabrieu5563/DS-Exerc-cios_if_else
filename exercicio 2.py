import os
os.system("cls")

nascimento = int(input("Digite sua data de nascimento: "))
idade = 2024 - nascimento


if idade >= 16:
        print('pode votar')
else:
        print("nao pode votar")