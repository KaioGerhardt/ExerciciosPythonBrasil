"""Descrição: Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

#------------------- Código -------------------

preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

if preco1 < preco2 and preco1 < preco3:
    print(f"O produto a ser comprado é o primeiro produto, com preço de R$ {preco1}")
elif preco2 < preco3 and preco2 < preco1:
    print(f"O produto a ser comprado é o segundo produto, com preço de R$ {preco2}")
elif preco3 < preco1 and preco3 < preco2:
    print(f"O produto a ser comprado é o terceiro produto, com preço de R$ {preco3}")