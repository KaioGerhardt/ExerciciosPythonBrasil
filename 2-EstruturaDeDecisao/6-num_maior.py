"""Descrição: Faça um Programa que leia três números e mostre o maior deles."""

#------------------- Código -------------------
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 > num2 and num3:
    print(f"O maior numero é {num1}!")
elif num2 > num1 and num3:
    print(f"O maior numero é {num2}!")
elif num3 > num1 and num2:
    print(f"O maior numero é o {num3}!")
else:
    print("Favor, digite um valor válido!")