'''
Autora: Nathália Maria Urenha Machado
Data: 11/11/2020
Descrição: Esse script responde qualquer pergunta que for feita a ele.

'''

from random import randrange

respostas = [
    'Sim.',
    'Não.',
    'Você não deveria fazer isso.',
    'Mas é claro!',
    'Hummm.. Não acho uma boa ideia.',
    'Sim, vai lá',
    'Siga seu coração!',
    'Você merece mais que isso!',
    'Talvez você só precise de um sorvete',
    'Deixa isso pra lá',
    'Que tal ir assistir um filme?'
]
while True:
    pergunta = input()
    if pergunta == 'Não quero perguntar mais':
        print('Até logo!!')
        break
    numero = randrange(0, 11)
    print(respostas[numero])

