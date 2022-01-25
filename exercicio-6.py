# cofing: -*- utf-8 -*-
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


# importando a biblioteca math 
import math
# função para retornar a area do circulo
def calc_area_circulo(raio):
    # a area de um circulo corresponde a forumula A = π . r2 respresentada abaixo
    Area = math.pi*raio**2
    # retornando a area
    return Area

# entrada de dados
recebe_raio = float(input("Digite o raio do circulo: "))

# executa o calculo passando o valor do raio para a função calcular a área
resultado = calc_area_circulo(recebe_raio)
# exibe o valor da área 
print("O valor correspondente a area do circulo é: ", resultado)