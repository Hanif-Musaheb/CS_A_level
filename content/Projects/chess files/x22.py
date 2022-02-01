import random,time

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

def board_stripper_yx(start_pos,position,enemy_color,board):
    diagonal=[]
    possible_moves=[]
    start_pos=str(start_pos)
    start_pos='{}{}'.format(int(start_pos[0]),int(start_pos[1]))
    diagonal.append(start_pos)
    
    #takes the row of values that are on the yx axis of the peice
    for i in range(int(start_pos[1])-int(start_pos[0])):
        start_pos='{}{}'.format(int(start_pos[0])+1,int(start_pos[1])-1)
        diagonal.append(start_pos)
    #filters the values found above into the ones that can be legally moved to
    position_on_axis=diagonal.index(position)
    for i in range(position_on_axis):
        if board[int(diagonal[position_on_axis-i-1][1])][int(diagonal[position_on_axis-i-1][0])][0] != '.':
            if board[int(diagonal[position_on_axis-i-1][1])][int(diagonal[position_on_axis-i-1][0])][0]==enemy_color:
                possible_moves.append(diagonal[position_on_axis-i-1])
                break
            else:break
        possible_moves.append(diagonal[position_on_axis-i-1])
        
    for i in range(len(diagonal)-1-position_on_axis):
        if board[int(diagonal[position_on_axis+i+1][1])][int(diagonal[position_on_axis+i+1][0])][0] != '.':
            if board[int(diagonal[position_on_axis+i+1][1])][int(diagonal[position_on_axis+i+1][0])][0]==enemy_color:
                possible_moves.append(diagonal[position_on_axis+i+1])
                break
            else:break
        possible_moves.append(diagonal[position_on_axis+i+1])
    return possible_moves

    

def board_stripper_y_x(start_pos,position,enemy_color,board):
    diagonal=[]
    possible_moves=[]
    start_pos=str(start_pos)
    start_pos='{}{}'.format(int(start_pos[0]),int(start_pos[1]))
    diagonal.append(start_pos)
    #takes the row of values that are on the yx axis of the peice
    for i in range(int(start_pos[1])-(7-int(start_pos[0]))):
        start_pos='{}{}'.format(int(start_pos[0])-1,int(start_pos[1])-1)
        diagonal.append(start_pos)
    #filters the values found above into the ones that can be legally moved to
    position_on_axis=diagonal.index(position)
    for i in range(position_on_axis):
        if board[int(diagonal[position_on_axis-i-1][1])][int(diagonal[position_on_axis-i-1][0])][0] != '.':
            if board[int(diagonal[position_on_axis-i-1][1])][int(diagonal[position_on_axis-i-1][0])][0]==enemy_color:
                possible_moves.append(diagonal[position_on_axis-i-1])
                break
            else:break
        possible_moves.append(diagonal[position_on_axis-i-1])
        
    for i in range(len(diagonal)-1-position_on_axis):
        if board[int(diagonal[position_on_axis+i+1][1])][int(diagonal[position_on_axis+i+1][0])][0] != '.':
            if board[int(diagonal[position_on_axis+i+1][1])][int(diagonal[position_on_axis+i+1][0])][0]==enemy_color:
                possible_moves.append(diagonal[position_on_axis+i+1])
                break
            else:break
        possible_moves.append(diagonal[position_on_axis+i+1])
    return possible_moves

def board_stripper_x(position,board):
    return board[int(position[1])]

def board_stripper_y(position,board):
    column=[]
    for i in range(8):
        column.append(board[i][int(position[0])])
    return column

def position_axis_to_cord(axis_position,axis,other_axis_position):
    if axis=='x':return '{}{}'.format(axis_position,other_axis_position)
    elif axis=='y':return '{}{}'.format(other_axis_position,axis_position)
    
def possible_moves_for_axis(position,axis,axis_of_board,enemy_color,board):
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

def castle_possible_moves(position,enemy_color,board):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position,board),enemy_color,board)
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position,board),enemy_color,board)
    return possible_moves

def bishop_possible_moves(position,enemy_color,board):
    possible_moves=[]
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position,enemy_color,board)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position,enemy_color,board)
    return possible_moves

def queen_possible_moves(position,enemy_color,board):
    possible_moves=[]
    possible_moves+=possible_moves_for_axis(position,'x',board_stripper_x(position,board),enemy_color,board)
    possible_moves+=possible_moves_for_axis(position,'y',board_stripper_y(position,board),enemy_color,board)
    possible_moves+=board_stripper_yx(start_pos_finder_for_yx(position),position,enemy_color,board)
    possible_moves+=board_stripper_y_x(start_pos_finder_for_y_x(position),position,enemy_color,board)
    return possible_moves

def king_possible_moves(position,enemy_color,board):
    possible_moves=[]
    king_move_relative=[[-1,0],[1,0],[-1,1],[0,1],[1,1],[-1,-1],[0,-1],[1,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+king_move_relative[i][0]),int(position[1])+king_move_relative[i][1])
        if (possible_move[0] not in ['-','8']) and (possible_move[1] not in ['-','8']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.',enemy_color]:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves

def horse_possible_moves(position,enemy_color,board):
    possible_moves=[]
    knight_move_relative=[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+knight_move_relative[i][0]),int(position[1])+knight_move_relative[i][1])
        if (possible_move[0] not in ['-','8','9']) and (possible_move[1] not in ['-','8','9']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.',enemy_color]:#remember y and then x
                possible_moves.append(possible_move)
    return possible_moves
    
def pawn_possible_moves(position,enemy_color,board):
    color = board[int(position[1])][int(position[0])][0]
    possible_moves=[]
    if color=='b':direction=1
    elif color=='w':direction=-1
    
    possible_move='{}{}'.format(int(position[0]),int(position[1])+direction)
    if board[int(possible_move[1])][int(possible_move[0])][0]=='.':
        possible_moves.append(possible_move)
        if (direction==-1 and position[1]=='6')or(direction==1 and position[1]=='1'):
                possible_move='{}{}'.format(int(position[0]),int(position[1])+direction*2)
                if board[int(possible_move[1])][int(possible_move[0])][0]=='.':
                    possible_moves.append(possible_move)
    if position[0]!='7' and board[int(position[1])+direction][int(position[0])+1][0]==enemy_color:
        possible_move='{}{}'.format(int(position[0])+1,int(position[1])+direction)
        possible_moves.append(possible_move)
    if position[0]!='0' and board[int(position[1])+direction][int(position[0])-1][0]==enemy_color:
        possible_move='{}{}'.format(int(position[0])-1,int(position[1])+direction)
        possible_moves.append(possible_move)
    return possible_moves

def enemy_color_finder(position,board):
    color=board[int(position[1])][int(position[0])][0]
    if color=='w':
        return 'b'
    elif color=='b':
        return 'w'
    
def peice_possible_moves(position,enemy_color,board):
    if board[int(position[1])][int(position[0])][0] != '.':
        peice=board[int(position[1])][int(position[0])][1]
        if peice=='p':return pawn_possible_moves(position,enemy_color,board)
        elif peice=='c':return castle_possible_moves(position,enemy_color,board)
        elif peice=='h':return horse_possible_moves(position,enemy_color,board)
        elif peice=='b':return bishop_possible_moves(position,enemy_color,board)
        elif peice=='q':return queen_possible_moves(position,enemy_color,board)
        elif peice=='k':return king_possible_moves(position,enemy_color,board)
        else:print('[ERROR] not a peice')
    else:print('[ERROR] position empty')

def find_kings_position(color):
    for i in range(8):
        for j in range(8):
            if board[i][j]=='{}{}'.format(color,'k'):
                return '{}{}'.format(j,i)
                
    
def is_king_checked(color):#ineffecient
    kings_position=find_kings_position(color)
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if kings_position in peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i))):
                    if color=='w':print('{} king checked'.format('white'))
                    elif color=='b':print('{} king checked'.format('black'))
                    return True
    return False
    
board=[['bc','bh','bb','bq','bk','bc','bh','bb'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wc','wh','wb','wq','wk','wb','wh','wc']]     


def user_input(color):
    while True:
        try:
            peice_position=str(input('peice position?'))
            if (int(peice_position[0]) in range(0,8)) and (int(peice_position[1]) in range(0,8)) and (len(peice_position)==2):
                if board[int(peice_position[1])][int(peice_position[0])]!='.':
                    if board[int(peice_position[1])][int(peice_position[0])][0]==color:
                        move_position=str(input('move position'))
                        if (int(move_position[0]) in range(0,8)) and (int(move_position[1]) in range(0,8)) and (len(move_position)==2):
                            if move_position in peice_possible_moves(peice_position,enemy_color_finder(peice_position)):
                                board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
                                board[int(peice_position[1])][int(peice_position[0])]='.'
                                return
            print('incorrect input')
        except:print('incorrect input')

def random_computer_output(color):
    peices_with_moves=[]
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if board[i][j][0]==color:
                    if peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i))) !=[]:peices_with_moves.append('{}{}'.format(j,i))

    random.shuffle(peices_with_moves)
    peice_position=peices_with_moves[0]
    #print(peice_possible_moves(peice_position,enemy_color_finder(peice_position)))
    move_position=random.choice(peice_possible_moves(peice_position,enemy_color_finder(peice_position)))
    print(move_position,'position moved to')
    board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
    board[int(peice_position[1])][int(peice_position[0])]='.'

#################################chess ai

    
###finds all possible moves=====================================================================1
count=0
def move_finder(color,board,recursion,recursion_depth,theoretical_moves):
    global count
    peices_with_moves=[]
    #peice_position,move_position,[](new list of the next theoretical moves)
    
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if board[i][j][0]==color:
                    if peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board) !=[]:
                        peices_with_moves.append('{}{}'.format(j,i))
                        possible_moves=peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board)
                        for possible_move in possible_moves:
                            theoretical_moves.append(['{}{}'.format(j,i),possible_move,[]])
                            count+=1

    return theoretical_moves


###values board of every possible move==========================================================3
def peice_value(peice,color):
    if peice[1]=='p':value=100
    elif peice[1]=='h':value=400
    elif peice[1]=='b':value=400
    elif peice[1]=='c':value=600
    elif peice[1]=='q':value=1000
    elif peice[1]=='k':value=1000000
    if peice[0] != color:value*=-1
    return value

def board_valuer(board,color):#evaluating the board
    board_value=0
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.':
                board_value+=peice_value(board[i][j],color)
       
    return board_value

###puts all possible moves onto a board=========================================================2
def board_maker(board,peice_position,move_position):
    possible_move_board=[]
    for i in range(8):possible_move_board.append(list(board[i]))
    possible_move_board[int(move_position[1])][int(move_position[0])]=possible_move_board[int(peice_position[1])][int(peice_position[0])]
    possible_move_board[int(peice_position[1])][int(peice_position[0])]='.'
    return possible_move_board

def board_outputter(board):
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board[0],board[1],board[2],board[3]
                                                    ,board[4],board[5],board[6],board[7]))
    
###==============================================================================================4 hybrid of recursion and iteration making it find all the moves ahead to the recurrsion depth
def computer_move(board,color,recursion,recursion_depth,theoretical_moves):
    theoretical_moves+=move_finder('b',board,0,1,[])
    for counter_move in theoretical_moves:
        counter_move[2].append(move_finder('w',board_maker(board,counter_move[0],counter_move[1]),0,1,[]))
        if recursion<recursion_depth:
            for move in counter_move[2][0]:                        
                move[2]+=computer_move(board_maker(board_maker(board,counter_move[0],counter_move[1]),move[0],move[1]),'b',recursion+1,recursion_depth,[])

    return theoretical_moves



def output_value(theoretical_moves,color):
    board_valuer(board_maker(board),color)


def minimaxing(recursion,recursion_depth,theoretical_moves):
    complete_move_sequence=[]
    move_sequences=[]
    for move1 in theoretical_moves:
        for move2 in move1[2][0]:
            for move3 in move2[2]:
                for move4 in move3[2]:
                    move_sequences.append([move1[0],move1[1],move2[0],move2[1],move3[0],move3[1],move4[0][0],move4[0][1]])
                        
    return move_sequences     

def move_sequence_valuer(move_sequences,ply,board):
    for i in range(len(move_sequences)):
        for j in range(ply):
            theoretical_board=board_maker(board,move_sequences[i][j*2],move_sequences[i][(j*2)+1])#check if move and peice position the right way round
        print(board_valuer(theoretical_board,'b'))
        board

            



##print(computer_move(board,'b',0,1,[]))

print('!','COUNT:',count)
move_sequence_valuer(minimaxing(0,1,computer_move(board,'b',0,1,[])),4,board)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
##    print('BOARD VALUE:',board_valuer(possible_move_board,'b'))
##    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(possible_move_board[0],possible_move_board[1],possible_move_board[2],possible_move_board[3]
##                                                    ,possible_move_board[4],possible_move_board[5],possible_move_board[6],possible_move_board[7]))
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

##            for move3 in move2:
##                print(move3)
                
##                for move4 in next_move_sequences:
##                    move_sequences.append([move[0],move[1],counter_move[0],counter_move[1]])
##                    complete_move_sequence+=move_sequence+next_move_sequence            
    #print(move_sequences)

##theoretical_moves=computer_move(board,'b')
##for move in theoretical_moves:
##    possible_move_board=board_maker(board,move[0],move[1])
##    print('BOARD VALUE:',board_valuer(possible_move_board,'b'))
##    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(possible_move_board[0],possible_move_board[1],possible_move_board[2],possible_move_board[3]
##                                                    ,possible_move_board[4],possible_move_board[5],possible_move_board[6],possible_move_board[7])) 
##    for counter_move in move[2:len(move)][0][0]:
##        print(board_valuer(board_maker(board_maker(board,move[0],move[1]),counter_move[0],counter_move[1]),'b'))



##def minimaxing(recursion,recursion_depth,theoretical_moves):
##    complete_move_sequence=[]
##    move_sequences=[]
##    for move in theoretical_moves:
##        for counter_move in move[2][0]:
##            move_sequences.append([move[0],move[1],counter_move[0],counter_move[1]])
##            if recursion<recursion_depth:
##                for move_sequence in move_sequences:
##                    print(recursion)
##                    next_move_sequences=minimaxing(recursion+1,recursion_depth,counter_move)
##                    for next_move_sequence in next_move_sequences:
##                        complete_move_sequence+=move_sequence+next_move_sequence


