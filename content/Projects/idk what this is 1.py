        board=[['bc','bh','bb','bq','bk','bb','bh','bc'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','wp','wp','wp','wp','wp','wp','wp'],
        ['wc','wh','wb','wq','wk','wb','wh','wc']]

def peice_value(peice,color):
    if peice[1]=='p':value=100
    elif peice[1]=='h':value=400
    elif peice[1]=='b':value=400
    elif peice[1]=='c':value=600
    elif peice[1]=='q':value=1000
    elif peice[1]=='k':value=1000000
    if peice[0] != color:value*=-1
    return value

def value_board(board,color):
    move_value=0
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.':
                move_value+=peice_value(board[i][j],color)
    return move_value

def move_value_finder(peice_position,move_position,color,board):

    possible_move_board=[]
    for i in range(8):possible_move_board.append(list(board[i]))
        
    possible_move_board[int(move_position[1])][int(move_position[0])]=possible_move_board[int(peice_position[1])][int(peice_position[0])]
    possible_move_board[int(peice_position[1])][int(peice_position[0])]='.'
    
    move_value =value_board(possible_move_board,color)
    
                
    return move_value

print(move_value_finder('01','03','b',board))

        ```
