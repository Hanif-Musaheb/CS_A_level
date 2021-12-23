import random

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

def board_stripper_yx(start_pos,position,enemy_color):
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
            if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0]==enemy_color:
                possible_moves.append(diagonal[diagonal.index(position)-i-1])
                break
            else:break
        possible_moves.append(diagonal[diagonal.index(position)-i-1])
        
    for i in range(len(diagonal)-1-diagonal.index(position)):
            if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0] != '.':
                if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0]==enemy_color:
                    possible_moves.append(diagonal[diagonal.index(position)+i+1])
                    break
                else:break
            possible_moves.append(diagonal[diagonal.index(position)+i+1])
    return possible_moves

def board_stripper_y_x(start_pos,position,enemy_color):
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
            if (board[int(diagonal[(diagonal.index(position))-i-1][0])][int(diagonal[(diagonal.index(position))-i-1][1])])[0][0]==enemy_color:
                possible_moves.append(diagonal[diagonal.index(position)-i-1])
                break
            else:break
        possible_moves.append(diagonal[diagonal.index(position)-i-1])
        
    for i in range(len(diagonal)-1-diagonal.index(position)):
        if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0] != '.':
            if (board[int(diagonal[(diagonal.index(position))+i+1][0])][int(diagonal[(diagonal.index(position))+i+1][1])])[0][0]==enemy_color:
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
    
def possible_moves_for_axis(position,axis,axis_of_board,enemy_color):
    possible_moves_for_axis=[]
    if axis=='x':
        position_on_axis=int(position[0])
        other_axis_position=int(position[1])
    elif axis=='y':
        position_on_axis=int(position[1])
        other_axis_position=int(position[0])

    for i in range(position_on_axis):
        if axis_of_board[position_on_axis-i-1][0] != '.':
            if axis_of_board[position_on_axis-i-1][0]==enemy_color:
                possible_moves_for_axis.append(position_axis_to_cord(position_on_axis-i-1,axis,other_axis_position))
                break
            else:break
        possible_moves_for_axis.append(position_axis_to_cord(position_on_axis-i-1,axis,other_axis_position))
        
    for i in range(7-position_on_axis):
        if axis_of_board[position_on_axis+i+1][0] != '.':
            if axis_of_board[position_on_axis+i+1][0]==enemy_color:
                possible_moves_for_axis.append(position_axis_to_cord(position_on_axis+i+1,axis,other_axis_position))
                break
            else:break
        possible_moves_for_axis.append(position_axis_to_cord(position_on_axis+i+1,axis,other_axis_position))
    return possible_moves_for_axis

def castle_possible_moves(position,enemy_color):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position),enemy_color)
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position),enemy_color)
    return possible_moves

def bishop_possible_moves(position,enemy_color):
    possible_moves=[]
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position,enemy_color)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position,enemy_color)
    return possible_moves

def queen_possible_moves(position,enemy_color):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position),enemy_color)
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position),enemy_color)
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position,enemy_color)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position,enemy_color)
    return possible_moves

def king_possible_moves(position,enemy_color):
    possible_moves=[]
    king_move_relative=[[-1,0],[1,0],[-1,1],[0,1],[1,1],[-1,-1],[0,-1],[1,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+king_move_relative[i][0]),int(position[1])+king_move_relative[i][1])
        if (possible_move[0] not in ['-','8']) and (possible_move[1] not in ['-','8']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.',enemy_color]:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves

def horse_possible_moves(position,enemy_color):
    possible_moves=[]
    knight_move_relative=[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+knight_move_relative[i][0]),int(position[1])+knight_move_relative[i][1])
        if (possible_move[0] not in ['-','8','9']) and (possible_move[1] not in ['-','8','9']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.',enemy_color]:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves
    
def pawn_possible_moves(position,enemy_color):
    color = board[int(position[1])][int(position[0])][0]
    possible_moves=[]
    if color=='b':direction=1
    elif color=='w':direction=-1
    
    possible_move='{}{}'.format(int(position[0]),int(position[1])+direction)
    if board[int(possible_move[1])][int(possible_move[0])][0]=='.':
        if (direction==-1 and position[1]=='6')or(direction==1 and position[1]=='1'):
                possible_moves.append(possible_move)
                possible_move='{}{}'.format(int(position[0]),int(position[1])+direction*2)
        possible_moves.append(possible_move)
    if position[0]!='7' and board[int(position[1])+1][int(position[0])+1][0]==enemy_color:
        possible_move='{}{}'.format(int(position[0])+1,int(position[1])+1)
        possible_moves.append(possible_move)
    if position[0]!='0' and board[int(position[1])+1][int(position[0])-1][0]==enemy_color:
        possible_move='{}{}'.format(int(position[0])-1,int(position[1])+1)
        possible_moves.append(possible_move)
    return possible_moves

def enemy_color_finder(position):
    color=board[int(position[1])][int(position[0])][0]
    if color=='w':
        return 'b'
    elif color=='b':
        return 'w'
    
def peice_possible_moves(position,enemy_color):
    if board[int(position[1])][int(position[0])][0] != '.':
        peice=board[int(position[1])][int(position[0])][1]
        if peice=='p':return pawn_possible_moves(position,enemy_color)
        elif peice=='c':return castle_possible_moves(position,enemy_color)
        elif peice=='h':return horse_possible_moves(position,enemy_color)
        elif peice=='b':return bishop_possible_moves(position,enemy_color)
        elif peice=='q':return queen_possible_moves(position,enemy_color)
        elif peice=='k':return king_possible_moves(position,enemy_color)
        else:print('[ERROR] not a peice')
    else:print('[ERROR] position empty')
    
def is_king_checked(kings_position):#ineffecient
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if kings_position in peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i))):return True
    return False

def output_possible_moves(possible_moves):
    if possible_moves==None:return
    output_board=[]
    for i in range(8):output_board.append(list(board[i]))
    for i in range(len(possible_moves)):
        output_board[int((possible_moves[i])[1])][int((possible_moves[i])[0])]='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(output_board[0],output_board[1],output_board[2],output_board[3]
                                                    ,output_board[4],output_board[5],output_board[6],output_board[7]))
    
board=[['bc','bh','bb','bq','bk','bc','bh','bb'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wc','wh','wb','wq','wk','wb','wh','wc']]    


def user_input():
    while True:
        try:
            peice_position=str(input('peice position?'))
            if (int(peice_position[0]) in range(0,7)) and (int(peice_position[1]) in range(0,7)) and (len(peice_position)==2):
                print(1)
                if board[int(peice_position[1])][int(peice_position[0])]!='.':
                    print(2)
                    move_position=str(input('move position'))
                    if (int(move_position[0]) in range(0,7)) and (int(move_position[1]) in range(0,7)) and (len(move_position)==2):
                        if move_position in peice_possible_moves(peice_position,enemy_color_finder(peice_position)):
                            board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
                            board[int(peice_position[1])][int(peice_position[0])]='.'
##                            print(board)
                            return
            print('incorrect input')
        except:
            print('incorrect input')
    
    
    
while True:
    user_input()
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7]))

    
    
    
    
    
##output_possible_moves(peice_possible_moves(position,enemy_color_finder(position)))
##is_king_checked(position)

