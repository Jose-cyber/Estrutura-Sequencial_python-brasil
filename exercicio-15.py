# -*- coding: utf-8 -*-
'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
'''

hora_custo = float(input("quanto você ganha por hora: "))

horas_trabalhadas = float(input("quantas horas você trabalhou: "))

def calcula_salario(hora_custo, horas_trabalhadas):
    salario_bruto = hora_custo*horas_trabalhadas
    IR = 11%salario_bruto
    INSS = 8%salario_bruto
    sindicato = 5%salario_bruto
    liquido = salario_bruto - IR - INSS - sindicato
    remuneracao= {'Bruto': salario_bruto, 'IR': IR, 'INSS':INSS, 'Sindicato':sindicato, 'Liquido':liquido}
    return remuneracao



resultado = calcula_salario(hora_custo, horas_trabalhadas)

print("O Salario bruto é: {}\nDesconto IR: {}\nDesconto INSS: {}\nDesconto sindicato: {}\nSalario liquido: {}".format(resultado['Bruto'], resultado['IR'], resultado['INSS'], resultado['Sindicato'], resultado['Liquido']))