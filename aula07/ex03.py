# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

inicio = int(input("Hora de Início: "))
fim = int(input("Hora de Término: "))

if fim <= inicio:
    tempo = ((24 - inicio) + fim)
else:
    tempo = (fim - inicio)

print("O JOGO DUROU {} HORA(S)".format(tempo))
