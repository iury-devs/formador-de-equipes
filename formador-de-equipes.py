from random import choice
from time import sleep

lista1 = ['iury', 'roberto', 'joao', 'jean'] #preencher com nomes (quantos você quiser) ->
lista2 = ['carlos', 'pedro', 'lucas', 'jhonatan']  #preencher com nomes (quantos você quiser) ->  TEM QUE SER A MESMA QUANTIDADE DE NOME EM TODAS AS LISTAS
lista3 = ['vincius', 'mateus', 'joao vitor', 'nathan']  #preencher com nomes (quantos você quiser) ->
lista4 = ['gabriel', 'raul', 'henrique', 'michael']  #preencher com nomes (quantos você quiser) ->

for c in range(1, 5):
    print('FORMANDO EQUIPES.....')
    sleep(1)
    print('-' * 20)
    print(f'      \033[34mEQUIPE {c}\033[m')
    print('-' * 20)
    #
    j1_player = choice(lista1)
    lista1.remove(j1_player)
    j2_player = choice(lista2)
    lista2.remove(j2_player)
    j3_player = choice(lista3)
    lista3.remove(j3_player)
    j4_player = choice(lista4)
    lista4.remove(j4_player)
    #
    sorteio = (f'{j1_player}\n'
               f'{j2_player}\n'
               f'{j3_player}\n'
               f'{j4_player}')
    print(sorteio)
    print('-' * 20) 