# -*- coding: utf-8 -*-
# Faça um Programa que converta metros para centímetros.


# função onde converte metros em centimetros
def convert_metros(metros):
    # multiplica o valor recebido em metros por 100
    centimentros = metros * 100
    # retorna o valor em forma de inteiro
    return int(centimentros)

# entrada de dados
recebe_metros = float(input("digite a metragem: "))

# chama a função para realizar a conversão
resultado = convert_metros(recebe_metros)
print("-"*20)
print(recebe_metros, "metro(s) em centimetros é: ", resultado, "cm")