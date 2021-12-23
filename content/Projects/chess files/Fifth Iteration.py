board=[['.','.','.','.','.','.','.','.'],
        ['bp','wp','.','.','.','.','.','.'],
        ['.','.','wp','.','.','.','.','.'],
        ['.','.','bp','.','.','.','.','.'],
        ['wp','wp','bK','wp','bp','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['bc','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]    


position='01'


def start_pos_finder_for_yx(position):#a tool for board_stripper_yx
    diagonal=[]
    start_pos=position
    while True:
        if start_pos[0]=='0' or start_pos[1]=='7':
            return start_pos
        start_pos='{}{}'.format((int(start_pos[0])-1),int(start_pos[1])+1)
        
        
def start_pos_finder_for_y_x(position):#a tool for board_stripper_y_x
    diagonal=[]
    start_pos=position
    while True:
        if start_pos[0]=='7' or start_pos[1]=='7':
            return start_pos
        start_pos='{}{}'.format((int(start_pos[0])+1),int(start_pos[1])+1)


def board_stripper_yx(start_pos,position):
    diagonal=[]
    possible_moves=[]
    start_pos=str(start_pos)
    start_pos='{}{}'.format(int(start_pos[0]),int(start_pos[1]))
    diagonal.append(start_pos)
    
    for i in range(int(start_pos[1])-int(start_pos[0])):
        start_pos='{}{}'.format(int(start_pos[0])+1,int(start_pos[1])-1)
        diagonal.append(start_pos)

    for i in range(diagonal.index(position)):
        if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0] != '.':
            if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0]=='w':
                possible_moves.append(diagonal[diagonal.index(position)-i-1])
                break
            else:break
        possible_moves.append(diagonal[diagonal.index(position)-i-1])
        
    for i in range(len(diagonal)-1-diagonal.index(position)):
            if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0] != '.':
                if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0]=='w':
                    possible_moves.append(diagonal[diagonal.index(position)+i+1])
                    break
                else:break
            possible_moves.append(diagonal[diagonal.index(position)+i+1])
    return possible_moves

def board_stripper_y_x(start_pos,position):
    diagonal=[]
    possible_moves=[]
    start_pos=str(start_pos)
    start_pos='{}{}'.format(int(start_pos[0]),int(start_pos[1]))
    diagonal.append(start_pos)
    
    for i in range(int(start_pos[1])-(7-int(start_pos[0]))):
        start_pos='{}{}'.format(int(start_pos[0])-1,int(start_pos[1])-1)
        diagonal.append(start_pos)

    for i in range(diagonal.index(position)):
        if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0] != '.':
            if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0]=='w':
                possible_moves.append(diagonal[diagonal.index(position)-i-1])
                break
            else:break
        possible_moves.append(diagonal[diagonal.index(position)-i-1])
        
    for i in range(len(diagonal)-1-diagonal.index(position)):
        if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0] != '.':
            if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0]=='w':
                possible_moves.append(diagonal[diagonal.index(position)+i+1])
                break
            else:break
        possible_moves.append(diagonal[diagonal.index(position)+i+1])
    return possible_moves

def board_stripper_x(position):
    return board[int(position[1])]

def board_stripper_y(position):
    column=[]
    for i in range(8):
        column.append(board[i][int(position[0])])
    return column

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

def castle_possible_moves(position):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position))
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position))
    return possible_moves


def bishop_possible_moves(position):
    possible_moves=[]
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position)
    return possible_moves

def queen_possible_moves(position):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position))
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position))
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position)
    return possible_moves

def king_possible_moves(position):
    possible_moves=[]
    king_move_relative=[[-1,0],[1,0],[-1,1],[0,1],[1,1],[-1,-1],[0,-1],[1,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+king_move_relative[i][0]),int(position[1])+king_move_relative[i][1])
        if (possible_move[0] not in ['-','8']) and (possible_move[1] not in ['-','8']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.','w']:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves

def horse_possible_moves(position):
    possible_moves=[]
    knight_move_relative=[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+knight_move_relative[i][0]),int(position[1])+knight_move_relative[i][1])
        if (possible_move[0] not in ['-','8','9']) and (possible_move[1] not in ['-','8','9']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.','w']:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves
    
    
def pawn_possible_moves(position,color='b'):
    possible_moves=[]
    if color=='b':
        direction=1
    elif color=='w':
        direction=-1
    
    possible_move='{}{}'.format(int(position[0]),int(position[1])+direction)
    if board[int(possible_move[1])][int(possible_move[0])][0]=='.':
        if (direction==-1 and position[1]=='6')or(direction==1 and position[1]=='1'):
                possible_moves.append(possible_move)
                possible_move='{}{}'.format(int(position[0]),int(position[1])+direction*2)
        possible_moves.append(possible_move)
    if board[int(position[1])+1][int(position[0])+1][0]=='w' and position[0]!='7':
        possible_move='{}{}'.format(int(position[0])+1,int(position[1])+1)
        possible_moves.append(possible_move)
    if board[int(position[1])+1][int(position[0])-1][0]=='w' and position[0]!='0':
        possible_move='{}{}'.format(int(position[0])-1,int(position[1])+1)
        possible_moves.append(possible_move)
    return possible_moves



def output_possible_moves(possible_moves):
    output_board=board
##    print(len(possible_moves))
    for i in range(len(possible_moves)):
##        print(possible_moves[i])
        output_board[int((possible_moves[i])[1])][int((possible_moves[i])[0])]='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(output_board[0],output_board[1],output_board[2],output_board[3]
                                                    ,output_board[4],output_board[5],output_board[6],output_board[7]))
    
    
output_possible_moves(pawn_possible_moves(position))#board_stripper_yx(position)))
