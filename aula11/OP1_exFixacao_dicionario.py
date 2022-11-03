print("Insira as informações do filme para poder adicioná-lo.")

# OPÇÃO 1 - INPUT DIRETO   ---------------------------------------

# filme = {
#    "titulo": input("Título: "),
#    "duracao": input("Duração: "),
#   "sinopse": input("Sinopse: ")
# }


# OPÇÃO 2 - SALVANDO EM VARIÁVEIS E INSERINDO DIRETO -------------

#titulo = input("Título: ")
#duracao = input("Duração: ")
#sinopse = input("Sinopse: ")

#filme = {
#    "titulo": titulo,
#    "duracao": duracao,
#    "sinopse": sinopse
#}


# OPÇÃO 3 - INSERINDO NOVA KEY -----------------------------------

filme = {}

filme["titulo"] = input("Título: ")
filme["duracao"] = input("Duração: ")
filme["sinopse"] = input("Sinopse: ")

print(" Título: {} \n Duração: {} \n Sinopse: {}".format(filme["titulo"], filme["duracao"], filme["sinopse"]))
