"""Descrição: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário 
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça 
um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa 
com as mensagens adequadas."""

#------------------- Código -------------------
peso = float(input("Digite o peso dos peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"O preço da multa a ser paga é de R$ {multa:.2f}, pois ultrapassou em {excesso:.2f}kg o limite!")
else:
    print("Não será necessário pagar multa, pois o peso não excedeu o limite!")