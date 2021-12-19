def position_axis_to_cord(axis_position,axis,other_axis_position):
    if axis=='x':return '{}{}'.format(axis_position,other_axis_position)
    elif axis=='y':return '{}{}'.format(other_axis_position,axis_position)
    

def possible_moves_for_axis(position,axis,axis_of_board):
    possible_moves_for_axis=[]
    if axis=='x':
        position_on_axis=int(position[0])
        other_axis_position=int(position[1])
    elif axis=='y':
        position_on_axis=int(position[1])
        other_axis_position=int(position[0])

        
    for i in range(position_on_axis):
        if axis_of_board[position_on_axis-i-1][0] != '.':
            if axis_of_board[position_on_axis-i-1][0]=='w':
                possible_moves_for_axis.append(position_axis_to_cord(position_on_axis-i-1,axis,other_axis_position))
                break
            else:break
        possible_moves_for_axis.append(position_axis_to_cord(position_on_axis-i-1,axis,other_axis_position))
        
    for i in range(7-position_on_axis):
        if axis_of_board[position_on_axis+i+1][0] != '.':
            if axis_of_board[position_on_axis+i+1][0]=='w':
                possible_moves_for_axis.append(position_axis_to_cord(position_on_axis+i+1,axis,other_axis_position))
                break
            else:break
        possible_moves_for_axis.append(position_axis_to_cord(position_on_axis+i+1,axis,other_axis_position))

    return possible_moves_for_axis

def board_stripper_x(position):
    return board[int(position[1])]

def board_stripper_y(position):
    column=[]
    for i in range(8):
        column.append(board[i][int(position[0])])
    return column

def output_possible_moves(possible_moves):
    output_board=board
    for i in range(len(possible_moves)):
        output_board[int((possible_moves[i])[1])][int((possible_moves[i])[0])]='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(output_board[0],output_board[1],output_board[2],output_board[3]
                                                    ,output_board[4],output_board[5],output_board[6],output_board[7]))
    
    
#print(possible_moves_for_axis('30','x'))
board=[['bc','bp','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','bp','.','wp','bp','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]

position='14'
possible_moves=[]
##print(board_stripper_x(position))
##print(board_stripper_y(position))
possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position))
possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position))

output_possible_moves(possible_moves)
