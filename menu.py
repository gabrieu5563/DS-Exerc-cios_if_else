import os
os.system("cls")

ex = '1'
while ex != 0:
    print("Exercício 1")
    print("Exercício 2")
    print("Exercício 3")
    print("Exercício 4")
    print("Exercício 5")
    print("Exercício 6")
    print("Exercício 7")
    print("Exercício 8")
    print("Exercício 9")
    print("Exercício 10")
    print("Exercício 11")
    print("Digite 0 para encerrar o código")
    ex = int(input("Digite o execício que quer executar: "))

    match ex:

        case 1:
            valor1 = int(input("valor 1: "))

            valor2 = int(input("valor 2: "))

            if valor1 > valor2:
                print(valor1)
            elif valor2 > valor1:
                print(valor2)
            else:
                print("Os dois valores são iguais.")

            os.system("pause")
            os.system("cls")

        case 2:
            nascimento = int(input("Digite sua data de nascimento: "))
            idade = 2024 - nascimento

            if idade >= 16:
                print('Pode votar')
            else:
                print("Não pode votar")

            os.system("pause")
            os.system("cls")

        case 3:
            senha = int(input("Digite a senha: "))

            if senha == 1234:
                print("ACESSO PERMITIDO")
            else:
                print("ACESSO NEGADO")

            os.system("pause")
            os.system("cls")

        case 4:
            quantidade = int(input("Quantas maçãs deseja comprar: "))

            if quantidade < 12:
                valor = quantidade * 0.30
            else:
                valor = quantidade * 0.25

            print(str(quantidade) + " Maçãs custarão R$" + str(valor))

            os.system("pause")
            os.system("cls")

        case 5:
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

            os.system("pause")
            os.system("cls")

        case 6:
            altura = float(input("Digite sua altura em cm: "))
            sexo = int(input('Digite seu sexo (1 para feminino e 2 para masculino): '))

            if sexo == 1:
                peso = 62.1 * (altura / 100) - 44.7
            else:
                peso = 72.2 * (altura / 100) - 58

            print('Seu peso ideal é ' + str(peso))

            os.system("pause")
            os.system("cls")

        case 7:
            lados = int(input("Digite quantos lados possui o polígono: "))
            tamanho = float(input("Digite o tamanho dos lados em cm: "))
            if lados == 3:
                print("triangulo")

            os.system("pause")
            os.system("cls")

        case 8:
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

            os.system("pause")
            os.system("cls")

        case 9:
            val1 = int(input("Digite o primeiro valor: "))
            val2 = int(input("Digite o segundo valor: "))
            val3 = int(input("Digite o terceiro valor: "))

            list = [val1, val2, val3]
            print(max(list))

            os.system("pause")
            os.system("cls")

        case 10:
            lado1 = float(input("Digite o tamanho do primeiro lado: "))
            lado2 = float(input("Digite o tamanho do segundo lado: "))
            lado3 = float(input("Digite o tamanho do terceiro lado: "))

            if lado1 == lado2 and lado1 == lado3:
                print('O triângulo é equilátero')
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("O triângulo é escaleno")
            else:
                print("O triângulo é isosceles")

            os.system("pause")
            os.system("cls")

        case 11:
            ang1 = float(input('Digite o valor do primeiro ângulo: '))
            ang2 = float(input('Digite o valor do segundo ângulo: '))
            ang3 = float(input('Digite o valor do terceiro ângulo: '))

            if ang1 == 90 or ang2 == 90 or ang3 == 90:
                print('Triângulo retângulo')
            elif ang1 > 90 or ang2 > 90 or ang3 > 90:
                print('Triângulo obtusângulo')
            else:
                print('Triângulo acutângulo')

            os.system("pause")
            os.system("cls")