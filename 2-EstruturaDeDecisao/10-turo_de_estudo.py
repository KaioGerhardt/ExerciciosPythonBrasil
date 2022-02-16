"""Descrição: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
ou "Valor Inválido!", conforme o caso."""

#------------------- Código -------------------

print("TURNOS E SIGLAS:\nM - Matutino\nV - Vespertino\nN - Noturno")
turno = str(input("Digite o turno em que você estuda: ").upper())

if turno == "M":
    print(f"Bom dia!")
elif turno == "V":
    print(f"Boa tarde!")
elif turno == "N":
    print(f"Boa noite!")
else:
    print(f"Valor inválido!")