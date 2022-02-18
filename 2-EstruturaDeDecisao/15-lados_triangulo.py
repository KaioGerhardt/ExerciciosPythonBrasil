lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

soma_lado = lado1 + lado2
soma_lado2 = lado1 + lado3
soma_lado3 = lado2 + lado3

if soma_lado > lado3 or soma_lado2 > lado2 or soma_lado3 > lado1:
    print("É um tringulo!")
    if lado1 == lado2 and lado2 == lado1:
        print("Este triangulo se categoriza como Equilátero!")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Este triangulo se categoriza como Isósceles!")
    else:
        print("Este triangulo se categoriza como Escaleno!")
else:
    print("Não é um triangulo!")