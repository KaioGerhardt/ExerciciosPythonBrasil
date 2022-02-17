from traceback import print_tb


nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

con = " "
def conceito():
    print(f"""
        ===========================
        AVALIAÇÕES DO ALUNO {nome}!\n
        ===========================
        A sua primeira nota foi {nota1}!
        A sua segunda nota foi {nota2}!
        A média geral foi de {media}!
        O seu conceito como aluno foi {con}
    """)
    if cc == 1:
        print(f"Portanto, o aluno {nome} está APROVADO")
    elif cc == 0:
        print(f"Portanto, o aluno {nome} está REPROVADO")

#a = "A"
#b = "B"
#c = "C"

if 10.0 > media >= 9.0:
    con = "A"
elif 9.0 > media >= 7.5:
    con = "B"
elif 7.5 < media >= 6.0:
    con = "C"
elif 6.0 > media >= 4.0:
    con = "D"
elif 0.0 <= media < 4.0:
    con = "E"

cc = 0
if con == "A" or "B" or "C":
    cc = cc += 1
elif con == "C" or "D":
    cc = 0

conceito()