print("Insira valor de A e N, separados somente por espaço, ex:(45 12)")
valores = input("-> ")
valSplit = valores.split()

a = int(valSplit[0])
n = int(valSplit[1])

while n < 1:
    n = int(input("Insira um valor para N que seja válido: "))
i =0
i = (0 <= i <= n-1)
