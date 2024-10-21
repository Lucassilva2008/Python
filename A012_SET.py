# Set (conjunto)
# conjunto1 (1,2,3,4,5,4,5,4)
# set não considera as repetições

conjunto = {1,2,3,4,5,4,5,4}
print(conjunto)

nomes = {"abigail","karl","gustavo","karl","abigail"}
print(nomes)

conjunto.add(9)
conjunto.remove(3)
print(conjunto)

outroConjunto = {7,5,3,9,1}
uniao = conjunto.union(outroConjunto)
print()
print(uniao)

diferença = conjunto.difference(outroConjunto)
print(diferença)

intersecção = conjunto.intersection(outroConjunto)
print(intersecção)