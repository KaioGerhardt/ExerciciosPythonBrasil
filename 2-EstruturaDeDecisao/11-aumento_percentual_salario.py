"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram 
para desenvolver o programa que calculará os reajustes.Faça um programa que recebe o salário de um
colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento."""

#------------------- Código -------------------

from traceback import print_tb


salario = float(input("Digite o seu salário: R$ "))

if salario <= 280.00:
    print(f"O seu salário antes do reajuste era de R$ {salario}!")
    print(f"O percentual aplicado ao seu salário foi de 20%!")
    print(f"O valor do aumento do seu salário foi de R$ {salario * 0.2}!")
    print(f"O seu salário com reajuste passou a ser de R$ {(salario * 0.2) + salario}!")

elif 280.00 <= salario and salario < 700.00:
    print(f"O seu salário antes do reajuste era de R$ {salario}!")
    print(f"O percentual aplicado ao seu salário foi de 15%!")
    print(f"O valor do aumento do seu salário foi de R$ {salario * 0.15}!")
    print(f"O seu salário com reajuste passou a ser de R$ {(salario * 0.15) + salario}!")

elif 700.00 <= salario and salario < 1500.00:
    print(f"O seu salário antes do reajuste era de R$ {salario}!")
    print(f"O percentual aplicado ao seu salário foi de 10%!")
    print(f"O valor do aumento do seu salário foi de R$ {salario * 0.1}!")
    print(f"O seu salário com reajuste passou a ser de R$ {(salario * 0.1) + salario}!")

elif 1500.00 < salario:
    print(f"O seu salário antes do reajuste era de R$ {salario}!")
    print(f"O percentual aplicado ao seu salário foi de 5%!")
    print(f"O valor do aumento do seu salário foi de R$ {salario * 0.05}!")
    print(f"O seu salário com reajuste passou a ser de R$ {(salario * 0.05) + salario}!")

else:
    print(f"Valor inválido, insira novamente!")