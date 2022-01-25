# -*- coding: utf-8 -*-
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# formula para conversão de Fahrenheit para celsius
# C = 5 * ((F-32) / 9)
def converte_temperatura(Fahrenheit):
    Celsius = 5*((Fahrenheit-32)/9)
    return Celsius


# entrada de dados
entrada_Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# chama a função e armazena o resultado na variavel resultado
resultado = converte_temperatura(entrada_Fahrenheit)

print("-"*38)
print("A temperatura em celsius é: ", resultado)