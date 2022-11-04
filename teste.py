itens = [{'item': 'faca', 'preco': '3.5', 'volume': '5', 'qtd': 1},
         {'item': 'madeira', 'preco': '2', 'volume': '7','qtd': 1},
         {'item': 'taco', 'preco': '7.45', 'volume': '5', 'qtd': 4},
         {'item': 'bola', 'preco': '5', 'volume': '3', 'qtd': 9}]



#for i in itens:
    #if i["item"] == "faca":
       # print(f'Item: {i["item"]}\nQuantidade disponível: {i["qtd"]}')
acc = 0
x = "taco"
for i in itens:
    if i["item"] == x:
        i["qtd"] -= 1

        if i["qtd"] < 1:
            itens.pop(acc)
        else:
            print("Ainda tem item")
    acc += 1

print(itens)