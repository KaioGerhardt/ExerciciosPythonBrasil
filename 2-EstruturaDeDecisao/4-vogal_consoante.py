"""Descrição: Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

#------------------- Código -------------------
letra = str(input("Digite uma letra qualquer: ").upper())

vogais = "AEIOU"
if letra in vogais:
    print("A letra digitada é uma vogal!")
else:
    print("A letra digitada é uma consoante!")