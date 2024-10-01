# Controle de fluxo "if"

habilitado = True
if habilitado:
    print("Esta habilitado!")

print("Esta linha sempre sera impressa")

if habilitado:
    print("Ok, habilitado")
else:
    print("Nada feito, Não está habilitado")

media = 8
if media >= 6:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
elif media >= 4:
    print("Trabalho de Recuperação")
else:
    print("Reprovado")

print("Terminado")


