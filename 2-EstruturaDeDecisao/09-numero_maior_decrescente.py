"""Descrição: Faça um Programa que leia três números e mostre-os em ordem decrescente."""

#------------------- Código -------------------

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num2< num1 > num3:
    if num2 > num3:
        print(f"A sequencia dos numeros é: {num3}, {num2} e {num1}!")
    elif num3 > num2:
        print(f"A sequencia dos numeros é: {num2}, {num3} e {num1}!")
        
elif num1 < num2 > num3:
    if num1 > num3:
        print(f"A seuquencia dos numeros é: {num3}, {num1} e {num2}!")
    else:
        print(f"A sequencia dos numeros é: {num1}, {num3} e {num2}!")

elif num1 < num3 > num2:
    if num1 > num2:
        print(f"A sequencia dos numeros é: {num2}, {num1} e {num3}!")
    else:
        print(f"A sequencia dos numeros é: {num1}, {num2} e {num3}!")