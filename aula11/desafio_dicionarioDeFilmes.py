print("Cadastro de Filmes")

qtd = int(input("Insira a quantidade de filmes a serem cadastrados: "))

filmes = []

vez = 0
while vez < qtd:
    filme = {'Título' : input("Título: "), 'duracao' : input("Duração: "), 'sinopse' : input("Sinopse: ")}

    filmes.append(filme) 

    vez += 1


print(filmes)