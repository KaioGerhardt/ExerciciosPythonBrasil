"""Descrição:Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
temperatura em graus Celsius. """

#------------------- Código -------------------
temp_f = float(input("Digite a temperatura em Fahrenheit: "))

temp_c = 5 * ((temp_f-32) / 9)
print(f"A temperatura de {temp_f}°F equivale a {temp_c}°C!")