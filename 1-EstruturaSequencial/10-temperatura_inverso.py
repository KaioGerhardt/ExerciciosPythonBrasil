"""Descrição: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

temp_c = float(input("Digite uma temperatura em °C: "))
temp_f = (temp_c * 9/5) + 32 

print(f"A temperatura de {temp_c}°C equivale a {temp_f}°F!")