def somar_elementos(lista):
    total = sum(lista)
    return total

numeros = [1, 2, 3, 4, 5]
resultado = somar_elementos(numeros)
print(resultado)

def somar_elementos(Lista):
    return sum(Lista)

#dados ficticios
lista1=[1,2,3,4,5] # a soma deve ser 15
lista2=[10,-2,3.5,7.5] # a soma deve ser 19.0
lista3=[]            # a soma deve ser 0
lista4=[-1,-2,-3,-4] # a soma deve ser -10

print("soma da lista1: ", somar_elementos(lista1))
print("soma da lista2: ", somar_elementos(lista2))
print("soma da lista3: ", somar_elementos(lista3))
print("soma da lista4: ", somar_elementos(lista4))