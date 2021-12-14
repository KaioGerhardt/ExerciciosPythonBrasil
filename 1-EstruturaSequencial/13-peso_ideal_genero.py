"""Descrição: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

altura = float(input("Digite a sua altura: "))
sexo = int(input("------------- SEXO -------------\n1- Homem\n2- Mulher\nDigite o seu sexo: "))

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

if sexo == 1:
    print(f"Um homem com uma alture de {altura} metros, tem como peso ideal o de {homens}kg!")
elif sexo == 2:
    print(f"Uma mulher com uma alture de {altura} metros, tem como peso ideal o de {mulheres}kg!"),