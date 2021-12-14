"""Descrição: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
no mês. Calcule e mostre o total do seu salário no referido mês."""

#------------------- Código -------------------
money = float(input("Digite o quanto você ganha por hora: R$"))
horas = int(input("Digite a quantidade de horas trabalhados no mês: "))
salario = money * horas

print(f"Você trabalhando {horas} horas no mes e ganhando R${money} por hora, então o seu salário mensal é de R${salario:.2f}!")
