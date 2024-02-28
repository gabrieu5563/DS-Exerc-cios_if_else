import os
os.system("cls")

quantidade = int(input("Quantas maçãs deseja comprar: "))

if quantidade < 12:
        valor = quantidade * 0.30
else:
        valor = quantidade * 0.25

print(str(quantidade)+" maçãs custarão R$"+str(valor))