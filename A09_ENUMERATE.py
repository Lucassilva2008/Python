for indice in "Ciencia de Dados":
    print(f"{indice}")


for indice in enumerate("Ciencia de Dados"):
    print(f"{indice}")

for indice, caractere in enumerate("Ciencia de Dados"):
    print(f"{indice}: {caractere}")

lista = ["Brasil", "EUA", "Inglaterra", "Italia", "França", "Alemanha"]

for indice, country in enumerate(lista):
    print(f"{indice} {country}")
print()

for indice, country in enumerate(lista, start=3):
    print(f"{indice} {country}")
