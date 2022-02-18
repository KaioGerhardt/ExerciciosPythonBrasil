nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

aprov = ''
conceito = ''
if 10.0 > media >= 9.0:
    aprov = True
    conceito = "A"
elif 9.0 > media >= 7.5:
    aprov = True
    conceito = "B"
elif 7.5 > media >= 6.0:
    aprov = True
    conceito = "C"
elif 6.0 > media >= 4.0:
    aprov = False
    conceito = "D"
elif 4.0 > media >= 0:
    aprov = False
    conceito = "E"

if conceito in "ABC":
    print(f"""
        ===============================
        NOTAS REFERENTE AO ALUNO {nome}
        ===============================
        A primeira nota foi de {nota1}!
        A segunda nota foi de {nota2}!
        A média geral foi de {media}!
        O conceito fo aluno foi {conceito}!
        Portanto, o aluno está APROVADO!
    """)
#elif aprov == False:
else:
    print(f"""
        ===============================
        NOTAS REFERENTE AO ALUNO {nome}
        ===============================
        A primeira nota foi de {nota1}!
        A segunda nota foi de {nota2}!
        A média geral foi de {media}!
        O conceito fo aluno foi {conceito}!
        Portanto, o aluno está REPROVADO!
    """) 