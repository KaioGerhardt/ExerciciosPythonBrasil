"""Descrição: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a 
média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez."""

#------------------- Código -------------------
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aluno aprovado!")
elif media < 7:
    print("Aluno reprovado!")
elif media == 10:
    print("Aluno aprovado com Distinção!")
else:
    print("Favor, inserir um dado válido!")