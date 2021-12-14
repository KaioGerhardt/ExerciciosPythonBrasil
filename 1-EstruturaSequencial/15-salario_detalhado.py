"""Descrição: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo"""

#------------------- Código -------------------
preco_hora = float(input("Digite quanto voce ganha por hora: R$ "))
qtd_hora = int(input("Digite quantas horas você trabalha no mês: "))

calc_salario = preco_hora * qtd_hora
ir = calc_salario * 0.11
inss = calc_salario * 0.08
sind = calc_salario * 0.05
salario_liq = calc_salario - (ir + sind + inss)

#print informações
print(f"+ Salário Bruto: R$ {calc_salario}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sind:.2f}")
print(f"= Salário Liquido: R$ {salario_liq:.2f}")