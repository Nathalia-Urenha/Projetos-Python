'''
Autora: Nathália Maria Urenha Machado
Data: 11/11/2020
Descrição: Esse script simula um dado, gerando um valor aleatório entre 1 e 6.

'''

import random

opc = 1
choice = input('Você quer jogar o dado??')
if choice == 'sim' or choice == 'Sim' or choice == 'SIM':
    while opc != 2:
        if opc != 1 and opc != 2:
            opc = int(input('ERRO: Digite 1 para continuar jogando o dado ou 2 para encerrar !!!'))
        else:
            print(random.randrange(1, 7))
            opc = int(input('Você gostaria de jogar o dado novamente?\n [1]Sim\n [2]Não'))





