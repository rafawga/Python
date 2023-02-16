# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:26:02 2023

@author: SRA2CT

"""
'================ IMPORTAÇÕES ================='
import random
'=============================================='


'==================== CORES ==================='
green = '\033[32m'
yellow = '\033[32m'
reset = '\033[0m'
'=============================================='
    

'========= DICIONARIO DE PALAVRAS=============='
palavra = ['rapido', 'pedra', 'louca', 'marca', 'rafael', 'garfo', 'fraco', 'baleia', 'dado', 'sorte']
'=============================================='


def get_word(escolha):   
    escolha = random.choice(palavra).upper() #escolhe um item aleatório dentro da lista de palavras
    return escolha   #retorna a palavra escolhida            

palavraf = get_word(palavra)   # escolha da palavra para o jogo
palavra = list(palavraf)       # cria uma lista com a palavra escolhida, onde cada letra é um index
game    = []                  # lista que contém todas as palavras já digitadas
tries   = 0                   # contador de erros

cript = ['_'] * len(palavra)  # criação da "primeira palvra" para o 
game.append(cript)              # usuário saber quantas letras a palavra contém

for a in range(len(palavra)):   # print desta "primeira palavra"
    print(cript[a], end = ' ')


while True:
    while True:
        letra = list(input('Digite uma palavra: ').upper())  #recebe a palavra de cada rodada
        if len(letra) != len(palavra):
            print(f'{reset}Digite uma palavra de {len(palavra)} letras!')  #verificação para ver se possui o mesmo tanto
        else:                                                                  #de letras da palavra sorteada
            break 
        
        
    game.append(letra) #adiciona a lista da palavra escolhida em outra lista
                         #com as tentaivas
    
    for b in range(len(game)):   #verificação de todas a lista dentro da lista GAME
        print('\n')
        for c in range(len(game[0])):                    #verifiação de cada letra contida na lista
            if game[b][c] == palavra[c]:                    #verificação de possui a letra no lugar exato da palavra
                print(f' \33[1;33;32m {game[b][c]}\33[0m ', end = ' ')
            elif game[b][c] in palavra:                       #verificação se a letra possui na palavra em qualquer posição
                print(f' \33[1;33;93m {game[b][c]}\33[0m ', end = ' ')
            else:                                               #verificação caso a letra não exista na palavra
                print(f' \33[1;33;31m {game[b][c]}\33[0m ', end = ' ')
    
    tries += 1 #acrescenta uma tentativa ao final de cada rodada
    
    if list(letra) == palavra:
        print('\n\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n          Você venceu \n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        break
    
    elif tries > 6:
        print(f'\n\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n    Você perdeu \n  A palavra era {palavraf}\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        break
