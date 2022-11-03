# Leia a data de nascimento do usuário e informe se ele é obrigado a votar nas próximas eleições, no dia 02/10/2022 ("Pessoas alfabetizadas maiores de 18 (dezoito) e menores de 70 (setenta) anos são obrigados a votar").

dia = int(input("Informe o seu dia de nascimento: "))
mes = int(input("Informe o seu mês de nascimento: "))
ano = int(input("Informe o seu ano de nascimento: "))

idade = 2022 - ano - ((10, 2) < (mes, dia))


if (idade >= 18) and (idade < 70):
    print("Você tem {} anos.".format(idade))
    print("Você é obrigado(a) a votar.")
else:
    print("Você tem {} anos.".format(idade))
    print("Você não é obrigado(a) a votar.")
