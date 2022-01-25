# -*- coding: utf-8 -*-
'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''

Arquivo_tamanho = float(input('Tamanho do arquivo (MB): '))

Velocidade_internet = float(input('Velocidade de Internet (MBps): '))

print('Tempo aproximado de download: %.0f Minutos ' %((Arquivo_tamanho / Velocidade_internet) * 60))

