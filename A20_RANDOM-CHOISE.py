import random


nomes = []
n = 5
while len(nomes) < n:
    resp = input(f"digite {len(nomes) + 1}º nome: ")
    nomes.append(resp)
    print(nomes)

nomesorteado = random.choice(nomes)
print(f"{nomesorteado} foi o nome sorteado")    

sair = "n"
while sair != "s":
   random.shuffle(nomes)
   print(nomes)
   sair = input("sair digite s: ")