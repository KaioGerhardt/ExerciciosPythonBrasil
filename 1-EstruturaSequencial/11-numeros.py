"""Descrição: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a - o produto do dobro do primeiro com metade do segundo .
b - a soma do triplo do primeiro com o terceiro.
c - o terceiro elevado ao cubo."""

n1 = int(input("Dgite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = float(input("Digite agora um numero real: "))

a = (n1 *2)* (n2 / 2)
b = (n1 *3) + n3
c = n3 ** 3

print(f"Com os numeros digitados, respectivamente {n1}, {n2} e {n3:.0f}, obtemos:\na) {a:.2f}\nb) {b:.2f}\nc) {c:.2f}")