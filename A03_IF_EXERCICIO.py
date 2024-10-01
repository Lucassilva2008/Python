# faça uma rotina com o uso do if, elif, else quer receba um valor numerico inteiro entre 1 e 100 e print se a pessoa com idade obrigatoriamente vota, se vota compulsoriamente ou não pode votar

acordei = True 
if acordei:
    print("Acordei cedo")
else:
    print("Faltei na Escola")

if acordei:
    print("Me arrumei e fui ao colegio")
else:
    print("Não fui ao colegio e tomei bronca")

idade = int(input("Digite a idade: "))
if idade >= 60:
    print("O voto é opcional")
elif idade >= 18:
    print("O voto é obrigatorio")
elif idade >= 16:
    print("Voto opcional")
else:
    print("Não é obrigado a votar")
    
if idade >= 60 or idade <= 16 and idade >= 16:
    print("O Voto é Opcional")
elif idade >= 18:
    print("O voto é Obrigatorio")
else:
    print("Não pode votar")

