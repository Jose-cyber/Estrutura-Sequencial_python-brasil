# -*- coding: utf-8 -*-

'''

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

'''
peso_de_peixes = float(input("Digite quantos quilos de peixe você pegou: "))

def calcula_multa(peso):
    if peso > 50.0:
        excedente = peso - 50.0
        calc = 4.00 / 1.00 * excedente
        return calc
    else:
        multa = "não há multas a pagar"
        return multa

resultado = calcula_multa(peso_de_peixes)

print("-"*30)

print("O valor a ser pago é de: ",resultado)