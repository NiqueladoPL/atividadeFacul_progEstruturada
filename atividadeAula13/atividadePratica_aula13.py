import os
mainLoop = 1
op = 0
itens = []

# Loop principal
while (mainLoop == 1):
    os.system('cls')
    print("Loja de Itens\n")
    op = input("Digite o número da opção desejada:\n1) Cadastrar Novo Item\n2) Itens Cadastrados\n3) Vender um Item\n4) Sair\n->")
    # validando a opção selecionada
    while (op != "1") and (op != "2") and (op != "3") and (op != "4"):
        os.system('cls')
        print("Valor Inválido!\n")
        op = input(
            "Digite o NÚMERO da opção desejada:\n1) Cadastrar Novo Item\n2) Itens Cadastrados\n3) Vender um Item\n4) Sair\n->")

# Cadastro de novo item
    while (op == "1"):
        os.system('cls')

        print("Cadastro de Itens\n")
        opCadastro = input("1) Cadastrar Novo Item\n2) Voltar\n->")
        while (opCadastro != "1") and (opCadastro != "2"):
            opCadastro = input(
                "Opção INVÁLIDA\nDigite 1 para Cadastrar Novo Item ou 2 para Voltar ao Menu\n->")
            os.system('cls')

        if (opCadastro == "1"):
            while (opCadastro == "1"):
                os.system('cls')
                print("Cadastrar Novo Item\n")
                novoItem = {'nome_item': input("Nome do item: "), 'preco': input(
                    "Preço: "), 'volume': input("Volume: "), 'quantidade': input("Quantidade disponível: ")}
                itens.append(novoItem)

                decisao = input("\n1) Cadastrar outro item\n2) Voltar ao Menu Principal\n-> ")
                while (decisao != "1") and (decisao != "2"):
                    decisao = input("ERRO! Digite 1 para Cadastrar outro Item ou 2 para Voltar ao Menu Principal\n->")
                if (decisao == "2"):
                    opCadastro = "0"
                    op = "0"

        elif (opCadastro == "2"):
            os.system('cls')
            print("Voltando...")
            op = 0

# Itens Cadastrados
    while (op == "2"):
        os.system('cls')
        if len(itens) == 0:
            print("Nenhum Item Cadastrado")
            input("\nAperte ENTER para voltar ao Menu Principal")
            op = 1

        else:
            print("A lista não está vazia")
            input()

# SAIR --- OP=4
    if (op == "4"):
        mainLoop = 0


os.system('cls')
print("Saindo...")
