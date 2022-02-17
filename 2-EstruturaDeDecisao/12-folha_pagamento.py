from socket import INADDR_ALLHOSTS_GROUP


valor_hora = float(input("Digite o valor da sua hora: R$ "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas no mês:"))

salario_bruto = valor_hora * qtd_horas

#calculo do IR
if salario_bruto <= 900:
    desconto_ir = 0
elif 900 <= salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif 1500 <= salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.1
elif salario_bruto > 2500:
    desconto_ir = salario_bruto * 0.2

desconto_sindicato = salario_bruto * 0.03
desconto_ifgts = salario_bruto * 0.11

desconto_total = desconto_ir + desconto_sindicato

#output dos dados
print(f"""
    Salário Bruto: ({qtd_horas} * {valor_hora})        : R$ {salario_bruto}
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
""")