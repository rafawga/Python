# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:37:50 2022

@author: SRA2CT
"""

import random

ingles = ['agree', 'awswer', 'apologize', 'ask', 'awaken', 'breath', 'brush', 'call', 'care', 'change', 'clean', 'close', 'cook', 'cross', 'cry', 'dance', 'deliver', 'describe', 'die', 'disagree', 'end', 'enjoy', 'fail', 'fear', 'guess', 'hate', 'help', 'invite', 'join', 'kill', 'learn', 'lie', 'like', 'listen', 'live', 'look', 'love', 'miss', 'move', 'study', 'walk', 'want', 'work', 'worry']
portugues = ['concordar', 'responder', 'desculpar', 'perguntar', 'acordar', 'respirar', 'escovar', 'ligar', 'cuidar', 'mudar', 'limpar', 'fechar', 'cozinhar', 'cruzar', 'chorar', 'dançar', 'entregar', 'descrever', 'morrer', 'descordar', 'terminar', 'aproveitar', 'falhar', 'temer', 'adivinhar', 'odiar', 'ajudar', 'convidar', 'entrar', 'matar', 'aprender', 'mentir', 'gostar', 'ouvir', 'viver', 'olhar', 'amar', 'perder', 'mover', 'estudar', 'andar', 'querer', 'trabalhar', 'preocupar']

def Traduzir(listaing, listapt):
    
    certo = 0
    errado = 0
    erro = []
    
    for j in range(10):
            pal = random.randint(0, len(ingles) - 1)
            palavra = ingles[pal]
            print('___________\ningles:', palavra, end = ' ')
            traducao = input('Tradução: ')
            if traducao == portugues[pal]:
                print('Correto')
                certo += 1
            else:
                print('Errado')
                errado += 1
                erro.append(palavra)
            ingles.remove(ingles[pal])
            portugues.remove(portugues[pal])        
            
    print(f'\n=-=-=-=-=-=-=-=-=-=-=-=-=\nQuantidade de Acertos: {certo}\nQuantidade de erros: {errado}')
            
    if len(erro) > 0:
        print('Palavras erradas: ')
        for j in range(len(erro)):
            print( erro[j], ' ', end=' ')


Traduzir(ingles, portugues)