"""Descrição: Faça um Programa que leia três números e mostre o maior e o menor deles."""

#------------------- Código -------------------

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"O maior numero é o {num1}")
    if num2 > num3:
        print(f"O menor numero é o numero {num3}")
    else:
        print(f"O menor numero é o numero {num2}")
elif num2 > num1 and num2 > num3:
    print(f"O maior numero é o {num2}")
    if num1 > num3:
        print(f"O menor numero é o {num3}")
    else:
        print(f"O menor numero é o numero {num1}")
elif num3 > num1 and num3 > num2:
    print(f"O maior numero é o numero {num3}")
    if num1 > num2:
        print(f"O menor numero é o numero {num2}")
    else:
        print(f"O menor numero é o numero {num1}")