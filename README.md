# Exercicios do Site Python Brasil

Caso queira ter acesso aos desafios e fazer você mesmo, pode entrar no site clicando [aqui] (https://wiki.python.org.br/ListaDeExercicios

> ## Sumário - Lista de Resolução


+ [Estrutura Sequencial](#EstruturaSequencial)
+ [Estrutura de Decisão](#EstruturadeDescião)

## <a name = "section"></a>Estrutura Sequencial
1. Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
3. Faça um Programa que peça dois números e imprima a soma.
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
5. Faça um Programa que converta metros para centímetros.
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.<br>
    **C = 5 * ((F-32) / 9).**
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:<br>
    a. o produto do dobro do primeiro com metade do segundo .<br>
    b. a soma do triplo do primeiro com o terceiro.<br>
    c. o terceiro elevado ao cubo.
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: **(72.7*altura) - 58**
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:<br>
    **Para homens: (72.7*h) - 58<br>**
    **Para mulheres: (62.1*h) - 44.7**
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:<br>
    + salário bruto.
    + quanto pagou ao INSS.
    + quanto pagou ao sindicato.
    + o salário líquido.
    + calcule os descontos e o salário líquido, conforme a tabela abaixo:
    <img src = "./readme/16.png"></img>

16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

## <a name = "section"></a>Estrutura de Decisão
1. Faça um Programa que peça dois números e imprima o maior deles.
2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: *F - Feminino, M - Masculino, Sexo Inválido.*
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    - A mensagem "Reprovado", se a média for menor do que sete;
    - A mensagem "Aprovado com Distinção", se a média for igual a dez.
6. Faça um Programa que leia três números e mostre o maior deles.
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.<br>
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        - o salário antes do reajuste;
        - o percentual de aumento aplicado;
        - o valor do aumento;
        - o novo salário, após o aumento.
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.<br>
    - **Desconto do IR:**
        - Salário Bruto até 900 (inclusive) - isento
        - Salário Bruto até 1500 (inclusive) - desconto de 5%
        - Salário Bruto até 2500 (inclusive) - desconto de 10%
        - Salário Bruto acima de 2500 - desconto de 20% <br>

    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
    <img src = "./readme/12.png"></img>
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
<img src = "./readme/14.png"></img>