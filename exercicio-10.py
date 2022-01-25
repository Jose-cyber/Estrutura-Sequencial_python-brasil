# -*- coding: utf-8 -*-
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# Para converter de graus celsius para Fahrenheit usamos a formula:
# °F = °C × 1, 8 + 32

# função na qual realiza a conversão da unidade
def converte_Fahrenheit(celsius):
    Fahrenheit = celsius*1.8+32
    return Fahrenheit



# entrada de dados
entrada_celsius =  float(input("Insira o valor em celsius: "))

# chama a função para realizar o calculo e armazena na variavel resultado
resultado = converte_Fahrenheit(entrada_celsius)

print("-"*40)
print("O valor da temperatura de celsius em Fahrenheit é: ", resultado)

