vazio   = 'ㅤ '
torre   = ' ♜'
bispo   = ' ♝'
cavalo  = ' ♞'
rainha  = ' ♛'
rei     = ' ♚'
peao    = ' ♙'
torreB  = '\33[1;33;93m ♜\33[0m'
bispoB  = '\33[1;33;93m ♝\33[0m'
cavaloB = '\33[1;33;93m ♞\33[0m'
rainhaB = '\33[1;33;93m ♛\33[0m'
reiB    = '\33[1;33;93m ♚\33[0m'
peaoB   = '\33[1;33;93m ♙\33[0m'
peca    = [torre, bispo, cavalo, rainha, rei, peao]
pecaB   = [torreB, bispoB, cavaloB, rainhaB, reiB, peaoB]


def defaultBoard(): #cria o tabuleiro inicial
    board = [
        [torreB, cavaloB, bispoB, rainhaB, reiB, bispoB, cavaloB, torreB],
        [peaoB, peaoB, peaoB, peaoB, peaoB, peaoB, peaoB, peaoB],
        [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio],
        [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio],
        [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio],
        [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio],
        [peao, peao, peao, peao, peao, peao, peao, peao ],
        [torre, cavalo, bispo, rainha, rei ,bispo , cavalo, torre],
            ] 
    return board

def mostrarBoard(board): #retorna o tabuleiro já 'padronizado'
    x = 9    
    print('\n       A     B     C     D     E     F     G     H')
    for i in range(8):
        print('    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        x -= 1
        print(x, ' ', end = ' | ')
        for j in range(8):
            print(board[i][j],end=' | ')
            
        print(' ', x)
            
    print('    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('       A     B     C     D     E     F     G     H')
    return ''


def moveValid(board,positionY, positionX, toY, toX,turn,lance):  # verificação de movimento
    actMove  = board[positionY][positionX]                 # posição inicial
    nextMove = board[toY][toX]                             # posição final
    nextMoveCase2 = board[toX][toY]

    try:
        
#========================== VERIFICAÇÃO PEÕES =============================== #
        
        if turn == 0:  #peões brancos
             if actMove == peao:
                 
                 if lance == 1:
                        if toY + 1 == positionY  and toX == positionX or toY + 2 == positionY  and toX == positionX:
                            return True
                        else:
                            return 'Movimento irregular do peão'
                        
                 elif toY == positionY - 1 and toX == positionX + 1 and board[toY][toX] != vazio or toY == positionY - 1 and toX == positionX -1 and nextMove != vazio:
                     return True
                 
                 elif toY + 1 == positionY  and toX == positionX:
                     return True
                 else: 
                     return 'Movimento Irregular do Peão'
        
            
                
                
        elif turn == 1: #peões negros
            if actMove == peaoB:
                
                if lance == 1:
                    if toY - 1 == positionY  and toX == positionX or toY - 2 == positionY  and toX == positionX:
                        return True
                    else:
                        return 'Movimento irregular do peão'
                if toY == positionY + 1 and toX == positionX + 1 and board[toY][toX] != vazio or toY == positionY + 1 and toX == positionX -1 and board[toY][toX] != vazio:
                    return True
                elif toY - 1 == positionY  and toX == positionX:
                    return True
                else: 
                   return 'Movimento Irregular do peão'
               
           
      
                
  #========================== VERIFICAÇÃO BISPOS =============================== #
        
  
        if actMove == bispo or actMove == bispoB:   #movimento bispo
                if abs(positionY - toY) == abs(positionX - toX):
                    return True
                else: 
                    return 'Movimento Irregular do bispo'
                
                
                
#========================== VERIFICAÇÃO TORRE =============================== #


        if actMove == torre or actMove == torreB:    #moveimento Torre
            if positionX == toX and positionY != toY or positionY == toY and positionX != toX:
                return True
            else:
                return 'Movimento irregular da Torre'
            
        
#========================== VERIFICAÇÃO RAINHAS =============================== #    

    
        if actMove == rainha or actMove == rainhaB:   #movimento rainha
            if abs(positionY - toY) == abs(positionX - toX) or positionX == toX and positionY != toY or positionY == toY and positionX != toX:
                return True
            else:
                return 'Movimento Irregular da Rainha'
            

#========================== VERIFICAÇÃO CAVALOS =============================== #


        if actMove == cavalo or actMove == cavaloB:   #movimento cavalo
            if abs(toY - positionY) == 2 and abs(toX - positionX) == 1:
                return True
            elif abs(toY - positionY) == 1 and abs(toX -positionX) == 2:
                return True
            else:
                return 'Movimento irregular do cavalo'
        
        
#========================== VERIFICAÇÃO REIS =============================== #


        if actMove == rei or actMove == reiB:
            if abs(toX - positionX) <= 1 and abs(toY - positionY) <= 1:
                return True
            else:
                return 'Movimento irregular do rei'


#========================== VERIFICAÇÕES EXTRAS =============================== #


        if turn == 0:  
            for pecas in range(len(pecaB)): #verificação se selecionou a cor certa
                if actMove == pecaB[pecas]:
                    return 'Vez das brancas jogarem!'
                    exit()
            
            for pecas in range(len(peca)): #Verificação se já existe uma peça na casa selecioanada
                if nextMove == peca[pecas]: #cavalo e peão
                    return 'Já existe uma peça sua nesta posição'
        elif turn == 1:
            for pecas in range(len(peca)): #verificação se selecionou a cor certa
                if actMove == peca[pecas]:
                    return 'Vez das Negras jogarem!'
                    exit()
            
            for pecas in range(len(pecaB)): #Verificação se já existe uma peça na casa selecioanada
                if nextMove == pecaB[pecas]:  #cavalo e peão
                    return 'Já existe uma peça sua nesta posição'
      
        if actMove == vazio: #verificação se está vazia a casa
          return 'Escolha casas que contenham peças!'
        
                
    except IndexError:
        return 'Escolha casas que estejam no tabuleiro!'
    
    else:
        pass
    
 #======================================================== #
   

def move(board,positionY, positionX, toY, toX,turn, peca):
    board[positionY][positionX] = vazio
    board[toY][toX]  = peca
    return board


 #======================================================== #


