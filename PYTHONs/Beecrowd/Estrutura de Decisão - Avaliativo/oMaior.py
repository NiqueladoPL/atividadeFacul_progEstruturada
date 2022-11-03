num = input()
a = int(num.split()[0])
b = int(num.split()[1])
c = int(num.split()[2])

maior1 = (a+b+abs(a-b))/2
maior2 = (maior1+c+abs(maior1-c))/2

print("{:.0f} eh o maior".format(maior2))
