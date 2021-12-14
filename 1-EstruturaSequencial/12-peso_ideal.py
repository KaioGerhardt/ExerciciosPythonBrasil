"""Descrição: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu
peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

#------------------- Código -------------------
altura = float(input("Digite a sua altura: "))

peso_ideal = (72.7 * altura) - 58

print(f"Com uma altura de {altura} metros seu peso ideal é de {peso_ideal}kg!")