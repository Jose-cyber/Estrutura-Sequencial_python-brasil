# -*- coding: utf-8 -*-
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# e calcule e mostre o total do seu salário no referido mês.
 
# função na qual calcula o salario
def calcula_salario(valor, hora):
    salario = valor*hora
    return int(salario)


# entrada de dados
valor_hora = float(input("Quando você ganha por hora ?\nvalor: "))
horas_trabalhadas = float(input("Quando horas você trabalhou no mes ?\nvalor:  "))

# chama a função para realização do calculo e armazena na variavel resultado
resultado = calcula_salario(valor_hora, horas_trabalhadas)

print("O valor de seu salario é: ", resultado)
