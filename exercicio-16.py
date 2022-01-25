# -*- coding: utf-8 -*-
'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

# importando a biblioteca math

import math as mt

qtd_metros=int(input('tamanho em metros quadrados da area a ser pintada: '))

litros = float(qtd_metros/3)

if litros<=18:
    print("-"*30)
    print('1 lata de tinta e o preço é de 80 reais')
else:
    # a função mt.ceil aredonda o valor para a quantidade de latas de tinta
    qtd_latas_tintas=mt.ceil(litros/18) 
    valor_latas = qtd_latas_tintas*80
    print("-"*30)  
    print('ira precisar de {} latas de tinta\ne o valor é de {} reais'.format(qtd_latas_tintas,valor_latas))

        
