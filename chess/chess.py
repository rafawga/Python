from func import *

board = defaultBoard()    #chama a função que cria o tabulerio e atribui a variável board
mostrarBoard(board)       #chama a função que mostra o tabuleiro

turn  = int(0)             #variável que define a vez de cada jogador
lance = 1                 #variavel que conta o numero de lances

tranf = {'A':1, 'B':2, 'C': 3, 'D' : 4, 'E':5, 'F':6, 'G':7, 'H':8, 
              'a':1, 'b':2, 'c': 3, 'd' : 4, 'e':5, 'f':6, 'g':7, 'h':8,
               '1':8, '2':7, '3':6, '4':5, '5':4, '6':3, '7':2, '8':1}

turndic = {0:'brancas', 1:'negras'}

while 1:

    inputMove = input(f"vez das {turndic[turn]} jogarem: ") #recebe a posiçao inicial e final
    inputMove = list(inputMove.split(" ")) #coloca em listas 
    
    for i in range(len(inputMove)):
        inputMove[i] = tranf[inputMove[i]] #troca os valores de letra para numero
    
    positionY = int(inputMove[1] - 1) #transforma cada index da lista em variaveis
    positionX = int(inputMove[0] - 1)
    toY = int(inputMove[3] - 1)
    toX = int(inputMove[2] - 1)


    if moveValid(board, positionY, positionX, toY, toX,turn,lance) == True: #se a validação do movimento estiver OK
        peca = board[positionY][positionX] #identifica qual a peça da posição escolhida
        move(board, positionY, positionX, toY, toX, turn,peca) #chama função que realiza o movimetno
        if turn == 1:
            lance += 1 #conta mais um lance ao fim do ciclo das negras
        turn = (1 + turn) % 2  #muda a vez do jogador

    
    else:
        print(moveValid(board, positionY, positionX, toY, toX,turn, lance)) #verificação não OK
    print(mostrarBoard(board)) #apenas printa o tabuleiro novamente



    


