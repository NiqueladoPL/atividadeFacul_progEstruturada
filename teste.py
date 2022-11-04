itens = [{'item': 'faca', 'preco': '3.5', 'volume': '5', 'qtd': '4'},
         {'item': 'madeira', 'preco': '2', 'volume': '7','qtd': '5'},
         {'item': 'taco', 'preco': '7.45', 'volume': '5', 'qtd': '4'},
         {'item': 'bola', 'preco': '5', 'volume': '3', 'qtd': '9'}]

for i in itens:
    print(f'Item: {i["Item"]}\nPreço: {i["Preço"]}\nVolume: {i["Volume"]}\nQuantidade disponível: {i["Quantidade disponível"]}\n---------------')