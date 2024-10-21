# TUPLA
# tupla = (elemento 1, elemento 2, ....)

variavel1 = 9 # variavel númerica
variavel2 = "Texto" # variavel tipo string
variavel3 = True # variavel do tipo boleano
variavel4 = ["Item1", "Item2", "Item3"] # lista
variavel5 = ("Item1", "item2", "...") # tupla

tupla = (1, "Olá", 5.14, True, 'o') # # imutavel
tuplaDireta = 'o', "Lucas", 1.618, 'o', "Lucas"
tuplavazia = ()
tuplaSimples = (27,)

print(tupla[1])
print(tupla[3])

print()
for indice, elemento in enumerate(tupla):
    print(f"{indice}", "{elemento}" )

tuplaAninhada = ((1,2,3), 1, True, [1,4, "sim"])
print()
print(tuplaAninhada[0])
print(tuplaAninhada[1])
print(tuplaAninhada[3][2])
print(len(tuplaDireta))

