# Usando a biblioteca math

from math import hypot

catetoOposto = float(input("Cateto Oposto: "))
catetoAdjacente = float(input("Cateto Adjacente: "))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** 0.5

print(f" A Hipotenusa mede {hipotenusa: .2f}")

hipo = hypot(catetoOposto, catetoAdjacente)
print((f"Usando hypot: {hipo: .0f}"))