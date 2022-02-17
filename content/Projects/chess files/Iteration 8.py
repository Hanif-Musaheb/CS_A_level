import random
import turtle

###CHESS UI###
window = turtle.Screen()
window.title("chess")
window.bgcolor('white')
window.setup(width=800, height=800)
window.tracer(0)

window.addshape("chess_board.gif")
window.addshape("black_queen.gif")
window.addshape("white_queen.gif")
window.addshape("black_king.gif")
window.addshape("white_king.gif")
window.addshape("white_queen.gif")
window.addshape("white_rook.gif")
window.addshape("black_rook.gif")
window.addshape("white_castle.gif")            
window.addshape("black_castle.gif")
window.addshape("black_horse.gif")
window.addshape("white_horse.gif")
window.addshape("black_pawn.gif")
window.addshape("white_pawn.gif")

board= turtle.Turtle()
board.shape("chess_board.gif")
board.goto(0,0)
board.pu()

wpawn1=turtle.Turtle()
wpawn1.shape("white_pawn.gif")
wpawn1.pu()
wpawn1.goto(-40,-200)

wpawn2=wpawn1.clone()
wpawn2.goto(-120,-200)
wpawn3=wpawn1.clone()
wpawn3.goto(-200,-200)
wpawn4=wpawn1.clone()
wpawn4.goto(-280,-200)
wpawn5=wpawn1.clone()
wpawn5.goto(40,-200)
wpawn6=wpawn1.clone()
wpawn6.goto(120,-200)
wpawn7=wpawn1.clone()
wpawn7.goto(200,-200)
wpawn8=wpawn1.clone()
wpawn8.goto(280,-200)

wcastle1=turtle.Turtle()
wcastle1.shape("white_castle.gif")
wcastle1.pu()
wcastle1.goto(-280,-280)
wcastle2=wcastle1.clone()
wcastle2.goto(280,-280)
wbishop1=turtle.Turtle()
wbishop1.shape("white_rook.gif")
wbishop1.pu()
wbishop1.goto(-120,-280)
wbishop2=wbishop1.clone()
wbishop2.goto(120,-280)
whorse1=turtle.Turtle()
whorse1.shape("white_horse.gif")
whorse1.pu()
whorse1.goto(-200,-280)
whorse2=whorse1.clone()
whorse2.goto(200,-280)
wqueen=turtle.Turtle()
wqueen.shape("white_queen.gif")
wqueen.pu()
wqueen.goto(40,-280)
wking=turtle.Turtle()
wking.shape("white_king.gif")
wking.pu()
wking.goto(-40,-280)

####

bpawn1=turtle.Turtle()
bpawn1.shape("black_pawn.gif")
bpawn1.pu()
bpawn1.goto(-40,200)

bpawn2=bpawn1.clone()
bpawn2.goto(-120,200)
bpawn3=bpawn1.clone()
bpawn3.goto(-200,200)
bpawn4=bpawn1.clone()
bpawn4.goto(-280,200)
bpawn5=bpawn1.clone()
bpawn5.goto(40,200)
bpawn6=bpawn1.clone()
bpawn6.goto(120,200)
bpawn7=bpawn1.clone()
bpawn7.goto(200,200)
bpawn8=bpawn1.clone()
bpawn8.goto(280,200)

bcastle1=turtle.Turtle()
bcastle1.shape("black_castle.gif")
bcastle1.pu()
bcastle1.goto(-280,280)
bcastle2=bcastle1.clone()
bcastle2.goto(280,280)
bbishop1=turtle.Turtle()
bbishop1.shape("black_rook.gif")
bbishop1.pu()
bbishop1.goto(-120,280)
bbishop2=bbishop1.clone()
bbishop2.goto(120,280)
bhorse1=turtle.Turtle()
bhorse1.shape("black_horse.gif")
bhorse1.pu()
bhorse1.goto(-200,280)
bhorse2=bhorse1.clone()
bhorse2.goto(200,280)
bqueen=turtle.Turtle()
bqueen.shape("black_queen.gif")
bqueen.pu()
bqueen.goto(40,280)
bking=turtle.Turtle()
bking.shape("black_king.gif")
bking.pu()
bking.goto(-40,280)

user_input_pos=[]
def user_moving_peice_click(x,y):
    x=int((x+320)/80)
    y=int(abs(y-320)/80)
    if len(user_input_pos)>=2:user_input_pos.clear()
        
    user_input_pos.append('{}{}'.format(x,y))
    return user_input_pos

def user_moving_peice_release(x,y):
    global user_input_pos
    x=int((x+320)/80)
    y=int(abs(y-320)/80)
    if len(user_input_pos)>=2:user_input_pos.clear()
        
    user_input_pos.append('{}{}'.format(x,y))
    user_input('w')

window.listen()
wpawn1.ondrag(wpawn1.goto)
wpawn1.onclick(user_moving_peice_click)
wpawn1.onrelease(user_moving_peice_release)
wpawn2.ondrag(wpawn2.goto)
wpawn2.onclick(user_moving_peice_click)
wpawn2.onrelease(user_moving_peice_release)
wpawn3.ondrag(wpawn3.goto)
wpawn3.onclick(user_moving_peice_click)
wpawn3.onrelease(user_moving_peice_release)
wpawn4.ondrag(wpawn4.goto)
wpawn4.onclick(user_moving_peice_click)
wpawn4.onrelease(user_moving_peice_release)
wpawn5.ondrag(wpawn5.goto)
wpawn5.onclick(user_moving_peice_click)
wpawn5.onrelease(user_moving_peice_release)
wpawn6.ondrag(wpawn6.goto)
wpawn6.onclick(user_moving_peice_click)
wpawn6.onrelease(user_moving_peice_release)
wpawn7.ondrag(wpawn7.goto)
wpawn7.onclick(user_moving_peice_click)
wpawn7.onrelease(user_moving_peice_release)
wpawn8.ondrag(wpawn8.goto)
wpawn8.onclick(user_moving_peice_click)
wpawn8.onrelease(user_moving_peice_release)

wcastle1.ondrag(wcastle1.goto)
wcastle1.onclick(user_moving_peice_click)
wcastle1.onrelease(user_moving_peice_release)
wcastle2.ondrag(wcastle2.goto)
wcastle2.onclick(user_moving_peice_click)
wcastle2.onrelease(user_moving_peice_release)
wbishop1.ondrag(wbishop1.goto)
wbishop1.onclick(user_moving_peice_click)
wbishop1.onrelease(user_moving_peice_release)
wbishop2.ondrag(wbishop2.goto)
wbishop2.onclick(user_moving_peice_click)
wbishop2.onrelease(user_moving_peice_release)
whorse1.ondrag(whorse1.goto)
whorse1.onclick(user_moving_peice_click)
whorse1.onrelease(user_moving_peice_release)
whorse2.ondrag(whorse2.goto)
whorse2.onclick(user_moving_peice_click)
whorse2.onrelease(user_moving_peice_release)
wqueen.ondrag(wqueen.goto)
wqueen.onclick(user_moving_peice_click)
wqueen.onrelease(user_moving_peice_release)
wking.ondrag(wking.goto)
wking.onclick(user_moving_peice_click)
wking.onrelease(user_moving_peice_release)


#####UI ENGINE EXCHANGE###
position_board=[[[-280,280],[-200,280],[-120,280],[-40,280],[40,280],[120,280],[200,280],[280,280]],
                [[-280,200],[-200,200],[-120,200],[-40,200],[40,200],[120,200],[200,200],[280,200]],
                [[-280,120],[-200,120],[-120,120],[-40,120],[40,120],[120,120],[200,120],[280,120]],
                [[-280,40],[-200,40],[-120,40],[-40,40],[40,40],[120,40],[200,40],[280,40]],
                [[-280,-40],[-200,-40],[-120,-40],[-40,-40],[40,-40],[120,-40],[200,-40],[280,-40]],
                [[-280,-120],[-200,-120],[-120,-120],[-40,-120],[40,-120],[120,-120],[200,-120],[280,-120]],
                [[-280,-200],[-200,-200],[-120,-200],[-40,-200],[40,-200],[120,-200],[200,-200],[280,-200]],
                [[-280,-280],[-200,-280],[-120,-280],[-40,-280],[40,-280],[120,-280],[200,-280],[280,-280]]]

turtle_board=[[bcastle1,bhorse1,bbishop1,bking,bqueen,bbishop2,bhorse2,bcastle2],
                    [bpawn4,bpawn3,bpawn2,bpawn1,bpawn5,bpawn6,bpawn7,bpawn8],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [wpawn4,wpawn3,wpawn2,wpawn1,wpawn5,wpawn6,wpawn7,wpawn8],
                    [wcastle1,whorse1,wbishop1,wking,wqueen,wbishop2,whorse2,wcastle2]]    

######CHESS ENGINE######

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


def castling(position,board):#only works for white
    possible_moves=[]
    can_castle=True
    color = board[int(position[1])][int(position[0])][0]
    if (has_wking_moved==False and color=='w') or (has_bking_moved==False and color=='b'):
        for i in range(2):
            possible_move='{}{}'.format((int(position[0])+i+1),int(position[1]))
            if board[int(position[1])][int(position[0])+i+1]!='.':can_castle=False
        if board[int(position[1])][7]!='{}{}'.format(color,'c'):can_castle=False
        if can_castle==True:possible_moves.append('{}{}'.format((int(position[0])+2),int(position[1])))
          
        can_castle=True
        for i in range(3):
            possible_move='{}{}'.format((int(position[0])-i-1),int(position[1]))
            if board[int(position[1])][int(position[0])-i-1]!='.':can_castle=False
        
        if board[int(position[1])][0]!='{}{}'.format(color,'c'):can_castle=False
        if can_castle==True:possible_moves.append('{}{}'.format((int(position[0])-2),int(position[1])))
    return possible_moves


def castling_UI(position,move_position,board):#only works for white
    can_castle=True
    color = board[int(position[1])][int(position[0])][0]
    a=None
    b=None
    
    if (has_wking_moved==False and color=='w') or (has_bking_moved==False and color=='b'):
        for i in range(2):
            possible_move='{}{}'.format((int(position[0])+i+1),int(position[1]))
            if board[int(position[1])][int(position[0])+i+1]!='.':can_castle=False
        if board[int(position[1])][7]!='{}{}'.format(color,'c'):can_castle=False
        if can_castle==True:a='{}{}'.format((int(position[0])+2),int(position[1]))
          
        can_castle=True
        for i in range(3):
            possible_move='{}{}'.format((int(position[0])-i-1),int(position[1]))
            if board[int(position[1])][int(position[0])-i-1]!='.':can_castle=False
        
        if board[int(position[1])][0]!='{}{}'.format(color,'c'):can_castle=False
        if can_castle==True:b='{}{}'.format((int(position[0])-2),int(position[1]))
    
    if move_position==a:
        (turtle_board[int(position[1])][7]).goto(position_board[0][int(position[0])+1][0],position_board[int(position[1])][0][1])
        board[int(position[1])][int(position[0])+1]=board[int(position[1])][7]
        board[int(position[1])][7]='.'
        turtle_board[int(position[1])][int(position[0])+1]=turtle_board[int(position[1])][7]
        turtle_board[int(position[1])][7]=None
         
    elif move_position==b:
        (turtle_board[int(position[1])][0]).goto(position_board[0][int(position[0])-1][0],position_board[int(position[1])][0][1])
        board[int(position[1])][int(position[0])-1]=board[int(position[1])][0]
        board[int(position[1])][0]='.'
        turtle_board[int(position[1])][int(position[0])-1]=turtle_board[int(position[1])][0]
        turtle_board[int(position[1])][0]=None
    
    
    

    
castling_moves=[]
def king_possible_moves(position,enemy_color,board,computer_search):
    global castling_moves
    possible_moves=[]
    castling_moves=[]
    
    king_move_relative=[[-1,0],[1,0],[-1,1],[0,1],[1,1],[-1,-1],[0,-1],[1,-1]]
    for i in range(8):
        possible_move='{}{}'.format((int(position[0])+king_move_relative[i][0]),int(position[1])+king_move_relative[i][1])
        if (possible_move[0] not in ['-','8']) and (possible_move[1] not in ['-','8']):
            if board[int(possible_move[1])][int(possible_move[0])][0] in ['.',enemy_color]:#remember y and then x
                possible_moves.append(possible_move)

    if computer_search==False:
        possible_moves+=castling(position,board)
        castling_moves+=castling(position,board)
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
    
def pawn_possible_moves(position,enemy_color,board,computer_search):
    color = board[int(position[1])][int(position[0])][0]
    possible_moves=[]
    if color=='b':direction=1
    elif color=='w':direction=-1
    
    if position[1]=='0' or position[1]=='7':
        while True:
            peice=str(window.textinput("b=Bishop c=Castle h=Horse q=Queen", "Peice?"))
            if peice in ['b','c','h','q']:
                board[int(position[1])][int(position[0])]='{}{}'.format(color,peice)
                if color=='b':
                    if peice=='b':(turtle_board[int(position[1])][int(position[0])]).shape("black_rook.gif")
                    if peice=='c':(turtle_board[int(position[1])][int(position[0])]).shape("black_castle.gif")
                    if peice=='h':(turtle_board[int(position[1])][int(position[0])]).shape("black_horse.gif")
                    if peice=='q':(turtle_board[int(position[1])][int(position[0])]).shape("black_king.gif")
                if color=='w':
                    if peice=='b':(turtle_board[int(position[1])][int(position[0])]).shape("white_rook.gif")
                    if peice=='c':(turtle_board[int(position[1])][int(position[0])]).shape("white_castle.gif")
                    if peice=='h':(turtle_board[int(position[1])][int(position[0])]).shape("white_horse.gif")
                    if peice=='q':(turtle_board[int(position[1])][int(position[0])]).shape("white_king.gif")
                window.update()    
                return peice_possible_moves(position,enemy_color_finder(position))
        
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
    
def peice_possible_moves(position,enemy_color,board,computer_search):
    if board[int(position[1])][int(position[0])][0] != '.':
        peice=board[int(position[1])][int(position[0])][1]
        if peice=='p':return pawn_possible_moves(position,enemy_color,board,computer_search)
        elif peice=='c':return castle_possible_moves(position,enemy_color,board)
        elif peice=='h':return horse_possible_moves(position,enemy_color,board)
        elif peice=='b':return bishop_possible_moves(position,enemy_color,board)
        elif peice=='q':return queen_possible_moves(position,enemy_color,board)
        elif peice=='k':return king_possible_moves(position,enemy_color,board,computer_search)
        else:print('[ERROR] not a peice')
    else:print('[ERROR] position empty')

def find_kings_position(color,board):
    for i in range(8):
        for j in range(8):
            if board[i][j]=='{}{}'.format(color,'k'):
                return '{}{}'.format(j,i)
                    
def is_king_checked(color,board):#ineffecient
    kings_position=find_kings_position(color,board)
        
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if kings_position in peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board,False):
                    if color=='w':print('white king checked')
                    elif color=='b':print('black king checked')
                    return True
    return False

def checkmate(color,board):
    kings_position=find_kings_position(color,board)
    if peice_possible_moves(find_kings_position(color,board),enemy_color_finder(find_kings_position(color,board),board),board,False) == [] and is_king_checked(color,board)== True:
        if color=='w':window.textinput("CHECKMATE black wins", "END GAME")
        elif color=='b':window.textinput("CHECKMATE white wins", "END GAME")
        window.bye()

def king_status(board):
    checkmate('w',board)
    is_king_checked('w',board)
    checkmate('b',board)
    is_king_checked('b',board)
    
board=[['bc','bh','bb','bq','bk','bb','bh','bc'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wc','wh','wb','wq','wk','wb','wh','wc']]

def board_outputter(board):
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board[0],board[1],board[2],board[3]
                                                    ,board[4],board[5],board[6],board[7]))

has_wking_moved=False
has_bking_moved=False

def user_input(color):
    global has_wking_moved#
    
    #try:
    peice_position=user_input_pos[0]
    if (int(peice_position[0]) in range(0,8)) and (int(peice_position[1]) in range(0,8)) and (len(peice_position)==2):
        if board[int(peice_position[1])][int(peice_position[0])]!='.':
            if board[int(peice_position[1])][int(peice_position[0])][0]==color:
                move_position=user_input_pos[1]
                if (int(move_position[0]) in range(0,8)) and (int(move_position[1]) in range(0,8)) and (len(move_position)==2):
                    if move_position in peice_possible_moves(peice_position,enemy_color_finder(peice_position,board),board,False):###
                        if (move_position in castling_moves) and board[int(peice_position[1])][int(peice_position[0])][1]=='k':
                            castling_UI(peice_position,move_position,board)
                        (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(move_position[1])][int(move_position[0])][0],position_board[int(move_position[1])][int(move_position[0])][1])
                        board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
                        board[int(peice_position[1])][int(peice_position[0])]='.'
                        if turtle_board[int(move_position[1])][int(move_position[0])] != None:                                    
                            (turtle_board[int(move_position[1])][int(move_position[0])]).ht()
                            (turtle_board[int(move_position[1])][int(move_position[0])]).goto(500,0)
                        turtle_board[int(move_position[1])][int(move_position[0])]=turtle_board[int(peice_position[1])][int(peice_position[0])]
                        turtle_board[int(peice_position[1])][int(peice_position[0])]=None
                        if board[int(move_position[1])][int(move_position[0])]=='wk':has_wking_moved=True#need to change if color changes
                        king_status(board)
                        output_of_ai()
                        return
                                
            print('incorrect input')
            (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(peice_position[1])][int(peice_position[0])][0],position_board[int(peice_position[1])][int(peice_position[0])][1])
            return
##    except:
##        print('incorrect input, system fail')
##        board_outputter(board)
##        #(turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(peice_position[1])][int(peice_position[0])][0],position_board[int(peice_position[1])][int(peice_position[0])][1])
##        return

#################################chess ai

def random_computer_output(color,board):
    peices_with_moves=[]
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if board[i][j][0]==color:
                    if peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board,True) !=[]:peices_with_moves.append('{}{}'.format(j,i))

    peice_position=random.choice(peices_with_moves)
    move_position=random.choice(peice_possible_moves(peice_position,enemy_color_finder(peice_position,board),board,False))
    print(move_position,'position moved to')
    board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
    board[int(peice_position[1])][int(peice_position[0])]='.'
    
    (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(move_position[1])][int(move_position[0])][0],position_board[int(move_position[1])][int(move_position[0])][1])
    if turtle_board[int(move_position[1])][int(move_position[0])] != None:(turtle_board[int(move_position[1])][int(move_position[0])]).ht()
    turtle_board[int(move_position[1])][int(move_position[0])]=turtle_board[int(peice_position[1])][int(peice_position[0])]
    turtle_board[int(peice_position[1])][int(peice_position[0])]=None
    #king_status()
    
###finds all possible moves=====================================================================1
count=0
def move_finder(color,board,recursion,recursion_depth,theoretical_moves):
    global count
    peices_with_moves=[]
    
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if board[i][j][0]==color:
                    if peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board,True) !=[]:
                        peices_with_moves.append('{}{}'.format(j,i))
                        possible_moves=peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i),board),board,True)
                        for possible_move in possible_moves:
                            theoretical_moves.append(['{}{}'.format(j,i),possible_move])
                            count+=1

    return theoretical_moves


###values board of every possible move==========================================================3
def peice_value(peice,color):
    if peice[1]=='p':value=100
    elif peice[1]=='h':value=400
    elif peice[1]=='b':value=400
    elif peice[1]=='c':value=600
    elif peice[1]=='q':value=1000
    elif peice[1]=='k':value=10000
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

def show_moves(moves,board):
    for move in moves:
        board_outputter(board_maker(board,move[0],move[1]))

def board_reset():
    theoretical_board=[]
    for i in range(8):theoretical_board.append(list(board[i]))
    return theoretical_board

def value_move_set(moves,color):
    pass

def theoretical_move_processing(board,color,theoretical_moves,recursion,recursion_depth):
    theoretical_moves=move_finder('b',board,0,0,[])

    
    for move in theoretical_moves:
        counter_moves=move_finder('w',board_maker(board,move[0],move[1]),0,0,[])
        move.append(counter_moves)
        
        for counter_move in counter_moves:    
            if recursion<recursion_depth:
                counter_move.append(theoretical_move_processing(board_maker(board_maker(board,move[0],move[1]),counter_move[0],counter_move[1]),'b',[],recursion+1,recursion_depth))
            
    return theoretical_moves   
            
#==============================================================================================5 minimaxing
def move_sequencing(theoretical_moves):
    sequenced_moves=[]
    count=0
    for move4 in theoretical_moves:
        c=[]
        for move3 in move4[2]:
            b=[]
            for move2 in move3[2]:
                a=[]
                for move1 in move2[2]:
                    a.append([move4[0],move4[1],move3[0],move3[1],move2[0],move2[1],move1[0],move1[1]])
                    count+=1
                b.append(a)
            c.append(b)
        sequenced_moves.append(c)
                    
    print(count)
    return sequenced_moves


def value_sequencing(sequenced_moves):
    valued_sequenced_moves=[]
    for move4 in sequenced_moves:
        c=[]
        for move3 in move4:
            b=[]
            for move2 in move3:
                a=[]
                for move1 in move2:
                    a.append(board_valuer(board_maker(board_maker(board_maker(board_maker(board,move1[0],move1[1]),move1[2],move1[3]),move1[4],move1[5]),move1[6],move1[7]),'b'))
                b.append(a)
            c.append(b)
        valued_sequenced_moves.append(c)
    return valued_sequenced_moves

def random_index(a,c):
    b=[]
    for i in range(len(a)):
        if a[i]==c:
            b.append(i)    
    return random.choice(b)

def minimaxing(sequenced_moves,squenced_values,theoretical_moves):
    base_move_values=[]
    for value3 in squenced_values:
        b=[]
        for value2 in value3:
            a=[]
            for value1 in value2:
                a.append(min(value1))
            b.append(max(a))
        base_move_values.append(min(b))
        
    if max(base_move_values)==board_valuer(board,'b'):
        print('???')
        
    random_index_value=random_index(base_move_values,max(base_move_values))    
    return theoretical_moves[random_index_value][0],theoretical_moves[random_index_value][1] 
    
    
def output_of_ai():    
    theoretical_moves=theoretical_move_processing(board,'b',[],0,1)
    sequenced_moves=move_sequencing(theoretical_moves)
    valued_sequenced_moves=value_sequencing(sequenced_moves)
    move=minimaxing(sequenced_moves,valued_sequenced_moves,theoretical_moves)

    peice_position=move[0]
    move_position=move[1]
    
    board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
    board[int(peice_position[1])][int(peice_position[0])]='.'
    
    (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(move_position[1])][int(move_position[0])][0],position_board[int(move_position[1])][int(move_position[0])][1])
    if turtle_board[int(move_position[1])][int(move_position[0])] != None:(turtle_board[int(move_position[1])][int(move_position[0])]).ht()
    turtle_board[int(move_position[1])][int(move_position[0])]=turtle_board[int(peice_position[1])][int(peice_position[0])]
    turtle_board[int(peice_position[1])][int(peice_position[0])]=None

    
while True:
    window.update()
    


    
