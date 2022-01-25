# -*- coding: utf-8 -*-
'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7h) - 58
Para mulheres: (62.1h) - 44.7
'''

# entrada de dados
recebe_altura = float(input('Digite sua altura: '))

def calcula_imc_homen(altura):
    imc = (72.7*altura) - 58
    return imc

def calcula_imc_mulher(altura):
    imc = (62.1*altura) - 44.7
    return imc


resultado = calcula_imc_homen(recebe_altura)
resultado1 = calcula_imc_mulher(recebe_altura)


print("-"*20)

print("O peso ideal para sua altura é de(homen): ", resultado)

print("-"*20)

print("O peso ideal para sua altura é de(mulher): ", resultado1)
