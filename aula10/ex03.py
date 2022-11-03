x = 0
y = 1

while x<y or x>y:

    print("Insira valor de X e Y, separados somente por espaço, ex:(45 12)")
    valores = input("-> ")
    valSplit = valores.split()

    x = int(valSplit[0])
    y = int(valSplit[1])

    if x>y:
        print("Decrescente")
    elif x<y:
        print("Crescente")
    else:
        break      
