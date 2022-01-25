# -*- coding: utf-8 -*-
# Faça um Programa que peça dois números e imprima a soma.

# iniciando a função para o calculo das medias
def calcula_media(valor1, valor2, valor3, valor4):
# o valor da media corresponde a soma dos valores divido pela quantidade
    soma_medias = valor1 + valor2 + valor3 + valor4
    media = soma_medias/4
    return media 

# onde vou solicitar a entrada da nota
while True:
    nota_1_bimestre = int(input("Digite a nota do primeiro bimestre: "))
    if nota_1_bimestre > 10:
        print("Valor invalido!")
    else: 
        break
# onde vou solicitar a entrada da nota
while True:
    nota_2_bimestre = int(input("Digite a nota do segundo bimestre: "))
    if nota_2_bimestre > 10:
        print("Valor invalido!")
    else: 
        break
# onde vou solicitar a entrada da nota
while True:
    nota_3_bimestre = int(input("Digite a nota do terceiro bimestre: "))
    if nota_3_bimestre > 10:
        print("Valor invalido!")
    else: 
        break
# onde vou solicitar a entrada da nota
while True:
    nota_4_bimestre = int(input("Digite a nota do quarto bimestre: "))
    if nota_4_bimestre > 10:
        print("Valor invalido!")
    else: 
        break


print("-"*30)
# chama a função para calcular a media e armazena na variavel resultado
resultado = calcula_media(nota_1_bimestre, nota_2_bimestre, nota_3_bimestre, nota_4_bimestre)
# printa o resultado calculado na função
print("o valor da media é ", resultado)