notas = input()
n1 = float(notas.split()[0])  # peso 2
n2 = float(notas.split()[1])  # peso 3
n3 = float(notas.split()[2])  # peso 4
n4 = float(notas.split()[3])  # peso 1
exame = 0

mediaA = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: {:.1f}".format(mediaA))

if (mediaA >= 7):
    print("Aluno aprovado")
elif (mediaA < 5):
    print("Aluno reprovado")
elif (mediaA >= 5) and (mediaA < 7):
    print("Aluno em exame")
    exame = 1

if (exame == 1):
    notaExame = float(input("Insira a nota obtida no exame: "))
    print("Nota do exame: {:.1f}".format(notaExame))
    mediaB = (mediaA + notaExame) / 2
    if (mediaB >= 5):
        print("Aluno aprovado")
    elif (mediaB < 5):
        print("Aluno reprovado")
    print("Media final: {:.1f}".format(mediaB))
