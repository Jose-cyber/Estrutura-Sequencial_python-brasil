# -*- coding: utf-8 -*-
'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

# entrada de dados
recebe_altura = float(input('Digite sua altura: '))

def calcula_imc(altura):
    imc = (72.7*altura) - 58
    return imc

resultado = calcula_imc(recebe_altura)

print("-"*20)

print("O peso ideal para sua altura é de: ", resultado)
