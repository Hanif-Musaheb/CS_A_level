board=[['bc','.','bc','bp','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['bp','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]

position='20'
possible_moves=[]
def possible_moves(position):
    possible_moves_in=[]
    for i in range(7):
        possible_position='{}{}'.format((i+1),position[1])

        y_pos_pos=int(possible_position[1])
        x_pos_pos=int(possible_position[0])+int(position[0])
        
        if board[y_pos_pos][x_pos_pos] != '.':
            if (str(board[y_pos_pos][x_pos_pos]))[0]=='w':
                print(board[y_pos_pos][x_pos_pos]) 
                possible_moves_in.append(possible_position)#entering possible move
                break
            else: break
        print(board[y_pos_pos][x_pos_pos]) 
        possible_moves_in.append(possible_position)#entering possible move
        
    for i in range(7):
        possible_position='{}{}'.format(position[0],(i+1))
        #print(possible_position)
        if board[int(possible_position[1])][int(possible_position[0])] != '.':
            if (str(board[int(possible_position[1])][int(possible_position[0])]))[0]=='w':
                print(board[int(possible_position[1])][int(possible_position[0])]) #y,x
                possible_moves_in.append(possible_position)#entering possible move
                break
            else: break
        print(board[int(possible_position[1])][int(possible_position[0])]) #y,x
        possible_moves_in.append(possible_position)#entering possible move
    return possible_moves_in
    
    
print(possible_moves(position))
