import os
os.system("cls")

aluno = [None] * 10
for a in range(1, 11, 1):
    print("Aluno " + str(a))
    for i in range(1, 4, 1):
        while True:
            if i == 1:
                verifnota = (int(input("Digite a primeira nota: ")))
            elif i == 2:
                verifnota = (int(input("Digite a segunda nota: ")))
            else:
                verifnota = (int(input("Digite a terceira nota: ")))

            if verifnota >= 0 and verifnota <= 10:
                if i == 1:
                    nota1 = verifnota
                elif i ==2:
                    nota2 = verifnota
                else:
                    nota3 = verifnota

                break
            else:
                print("Nota inválida. Digite novamente")

    lista = [nota1, nota2, nota3]
    menor = min(lista)
    lista.remove(menor)
    media = (lista[0] + lista[1]) / 2
    aluno[int(a - 1)] = media

mediasala = (aluno[0] + aluno[1] + aluno[2] + aluno[3] + aluno[4] + aluno[5] + aluno[6] + aluno[7] + aluno[8] + aluno[9]) / 10
print("Média da sala: " + str(mediasala))

maior = 0

for b in range (1, 11, 1):
    if aluno[int(b - 1)] >= 9:
        maior += 1

print(str(maior) + " alunos tiveram uma média maior que 9.")