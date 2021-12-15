"""Descrição: Faça um Programa que peça dois números e imprima o maior deles."""

#------------------- Código -------------------
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O maior numero é {num1}")
elif num2 > num1:
    print(f"O maior numero é o {num2}")
elif num1 == num2:
    print("Por favor, digite dois numeros diferentes!")
else:
    print("Favor, digitar um valor válido!")