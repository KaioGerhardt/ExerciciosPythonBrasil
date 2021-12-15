"""Descrição: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido."""

#------------------- Código -------------------
letra = str(input("Por favor, digite se é maculino ou feminino: ").upper())

if letra == "M": # or "M":
    print("M - Masculino")
elif letra == "F":# or "F":
    print("F - Feminino")
else:
    print("Sexo inválido!")