nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if 10.0 > media >= 9.0:
    print(f"O conceito do Aluno {nome} é A!")
elif 9.0 > media >= 7.5:
    print(f"O conceito do Aluno {nome} é B!")
elif 7.5 < media >= 6.0:
    print(f"O conceito do Aluno {nome} é C!")
elif 6.0 > media >= 4.0:
    print(f"O conceito do Aluno {nome} é D!")
elif 0.0 <= media < 4.0:
    print(f"O conceito do Aluno {nome} é E!")  