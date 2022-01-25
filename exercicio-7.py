# -*- coding: utf-8 -*-
# Faça um Programa que calcule a área de um quadrado 
# e em seguida mostre o dobro desta área para o usuário.

# função na qual calcula a área do quadrado
def calcula_area(base, altura):
    area = base*altura
    return area


# entrada de dados
recebe_base = float(input("Digite o tamano da base do quadrado: "))
recebe_altura = float(input("Digite o tamano da altura do quadrado: "))

# função na qual realiza o calculo conforme os valores recebidos
resultado = calcula_area(recebe_base, recebe_altura)
print("-"*38)

# imprimi o valor correspondente a área
print("O valor correspondente a área é: ", resultado)

# imprime o valor correspondente ao dobro da área
print("E o dobro da área seria: ", resultado*2)
