
from ctypes.wintypes import PINT


L = [5, 7, 2, 9, 4, 1, 3]

print("Tamanho da lista: {}".format(len(L)))

print("Maior valor da lista: {}".format(max(L)))

print("Menor valor da lista: {}".format(min(L)))

print("Soma de todos os elementos da lista: {}".format(sum(L)))

L.sort()
print("Lista em ordem crescente: {}".format(L))

L.reverse()
print("Lista em ordem decrescente: {}".format(L))
