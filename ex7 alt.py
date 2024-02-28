lados = int(input("Digite a quantidade de lados do polígono: "))
tamanho = float(input("Digite o tamanho dos lados em cm: "))
area = float(0)

if lados < 3:

        print("NÃO É UM POLÍGONO")
elif lados > 5:

        print("POLÍGONO NÃO IDENTIFICADO")
elif lados == 3:
        print("TRIÂNGULO")
        area = (tamanho * tamanho) / 2
        print(area)

elif lados == 4:
        print("QUADRADO")
        area = (tamanho * tamanho)
        print(area)

else:
        print("PENTAGONO")