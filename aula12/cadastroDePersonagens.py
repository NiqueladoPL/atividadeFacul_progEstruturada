import os

print("Cadastro de Personagens. \n\nDigite o número da opção desejada:\n1 - Cadastrar Personagens \n2 - Sair")
op = int(input("->"))

while (op != 1) and (op != 2):
    op = int(input(
        "VALOR INCORRETO!\nDigite o número da opção desejada:\n1 - Cadastrar Personagens\n2 - Sair\n->"))


personagens = []

while op == 1:
    os.system('cls')
    print("Dados do Personagem:\n")

    nome = input("Nome:")

    nome = {'nome': (nome),
            'idade': input("Idade: "),
            'raca': input("Raça: "),
            'etnia': input("Etnia: "),
            'naturalidade': input("Naturalidade: "),
            'cultura': input("Cultura: "),
            'origem': input("Origem: "),
            'profissao': input("Profissão: ")}

    personagens.append(nome)

    op = int(
        input("\n\nPara cadastrar outro usuário digite 1\nPara Sair digite 2\n->"))


if (op == 2):
    if (len(personagens) == 0):
        print("Nenhum personagem cadastrado.")
        print("Saindo...")
    else:
        print("Personagens cadastrados:")
        print(personagens)
        print("\nSaindo...")