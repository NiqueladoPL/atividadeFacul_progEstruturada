galera = list()
pessoa = dict()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]:")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    galera.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]: ")).upper()[0]
        if reposta in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resposta == 'S':
        break

print(galera)