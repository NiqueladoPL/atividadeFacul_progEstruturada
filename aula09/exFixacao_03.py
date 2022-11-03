temps = [12.5, 15.0, 19.5, 21.0, 17.5, 13.0]

print("A temperatura máxima foi de: {}°C".format(max(temps)))
print("A temperatura mínima foi de: {}°C".format(min(temps)))
print("A variação máxima foi de: {}°C".format((max(temps))-(min(temps))))

i = 0
soma = 0
while i < len(temps):
    soma += temps[i]
    i += 1

print("A temperatura média foi de: {:.2f}°C".format(soma/(len(temps))))
