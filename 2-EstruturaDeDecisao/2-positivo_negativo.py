"""Descrição: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

#------------------- Código -------------------
num = float(input("Digite um valor qualquer: "))

if num > 0:
    print("Este numero é positivo!")
elif num < 0:
    print("Este numero é negativo!")
else:
    print("Este numero é zero.")