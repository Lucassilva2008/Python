# lista = conjunto de valores
# lista = [valor1, valor2, ...]
# lista = list(valor1, valor2, ...)

listaVazia = [] # cria lista vazia

listaComElementos = [1, 2, 3, 4, 5, 6, 7,]
listaComElementosMista = [7, "Python", 3.14159, True, 'c']

listaComElementos[0] # pega o primeiro elemento
listaComElementos[-1] # pega o ultimo elemento
listaComElementos[:4] # pega os 3 primeiros elementos
listaComElementos[3:] # pega do terceiro item em diante
listaComElementos[3:5] # pega do terceiro até o quinto
listaComElementos[3:8:2] # pega do terceiro ao setimo de 2 em 2

print(listaComElementos[3:8:2])

len(listaComElementos)# retorna número de elementos
    #print (len:(listaComElementos:))

max(listaComElementos)# retorna o maior valor
    #print(max:(listaComElementos:))

min(listaComElementos)# retorna o menor valor
sum(listaComElementos)# retorna a soma de todos elementos

print(sum(listaComElementos))
sorted(listaComElementos)# retorna a lista em ordem crescente

listaVazia.append(1) # adiciona um elemento
listaVazia.append("Texto")
listaVazia.append(True)

print(listaVazia)

listaVazia.insert(2, "novo elemento") #  adiciona elementos no indice 2

print(listaVazia)

listaVazia.remove("Texto") # remove o primeiro elemento encontrado
print(listaVazia)

print(listaVazia.pop(0))
print(listaVazia)

print(listaVazia.index("novo elemento"))

ListaNacoes = ["Brasil","Eua", "China", "Canada", "Inglaterra"]

print(ListaNacoes.count("Eua"))

novalista = ListaNacoes.copy()
print(novalista)

temElemento = 'Canada' in novalista
print(temElemento)

while True:
    if "Brasil" in ListaNacoes
    print("Descobri o Brasil")
    ListaNacoes.remove("Brasil")
elif "Inglaterra" in ListaNacoes:



