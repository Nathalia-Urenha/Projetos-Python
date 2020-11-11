'''
Autora: Nathália Maria Urenha Machado
Data: 11/11/2020
Descrição: Esse script gera um valor aleatório, guarda este valor, e pergunta
repetidamente para o usuário chutar o valor gerado até que ele acerte.

'''

import random

numero = random.randrange(0, 101)
numero = int(numero)
while 1:
    while True:
        valor = input('Chute um valor!')
        try:
            valor = int(valor)
            break
        except ValueError:
            print('Por favor, digite somente números!!')

    if valor == numero:
        print('Parabéns, você acertou!')
        break
    elif valor < numero:
        print('Chutou baixo!!')
    elif valor > numero:
        print('Chutou alto!!')

