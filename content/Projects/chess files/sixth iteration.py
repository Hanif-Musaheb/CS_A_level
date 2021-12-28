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
wqueen.goto(-40,-280)

wking=turtle.Turtle()
wking.shape("white_king.gif")
wking.pu()
wking.goto(40,-280)

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
bqueen.goto(-40,280)

bking=turtle.Turtle()
bking.shape("black_king.gif")
bking.pu()
bking.goto(40,280)

user_input_pos=[]
def user_moving_peice_click(x,y):
    x=int((x+320)/80)
    y=int(abs(y-320)/80)
    print('{}{}'.format(x,y))
    if len(user_input_pos)>=2:user_input_pos.clear()
        
    user_input_pos.append('{}{}'.format(x,y))
    print(user_input_pos)
    return user_input_pos

def user_moving_peice_release(x,y):
    global user_input_pos
    x=int((x+320)/80)
    y=int(abs(y-320)/80)
    print('{}{}'.format(x,y))
    if len(user_input_pos)>=2:user_input_pos.clear()
        
    user_input_pos.append('{}{}'.format(x,y))
    print(user_input_pos)
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

turtle_board=[[bcastle1,bhorse1,bbishop1,bqueen,bking,bbishop2,bhorse2,bcastle2],
                    [bpawn4,bpawn3,bpawn2,bpawn1,bpawn5,bpawn6,bpawn7,bpawn8],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [wpawn4,wpawn3,wpawn2,wpawn1,wpawn5,wpawn6,wpawn7,wpawn8],
                    [wcastle1,whorse1,wbishop1,wqueen,wking,wbishop2,whorse2,wcastle2]]    

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

def board_stripper_yx(start_pos,position,enemy_color):
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

def board_stripper_y_x(start_pos,position,enemy_color):
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
                    if color=='w':print('white king checked')
                    elif color=='b':print('black king checked')
                    return True
    return False

def checkmate(color):
    kings_position=find_kings_position(color)
    if peice_possible_moves(find_kings_position(color),enemy_color_finder(find_kings_position(color))) == [] and is_king_checked(color)== True:
        if color=='w':window.textinput("CHECKMATE black wins", "END GAME")
        elif color=='b':window.textinput("CHECKMATE white wins", "END GAME")
        window.bye()

def king_status():
    checkmate('w')
    is_king_checked('w')
    checkmate('b')
    is_king_checked('b')
    
board=[['bc','bh','bb','bk','bq','bc','bh','bb'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wc','wh','wb','wk','wq','wb','wh','wc']]    


def user_input(color):
    try:
        peice_position=user_input_pos[0]
        if (int(peice_position[0]) in range(0,8)) and (int(peice_position[1]) in range(0,8)) and (len(peice_position)==2):
            if board[int(peice_position[1])][int(peice_position[0])]!='.':
                if board[int(peice_position[1])][int(peice_position[0])][0]==color:
                    move_position=user_input_pos[1]
                    if (int(move_position[0]) in range(0,8)) and (int(move_position[1]) in range(0,8)) and (len(move_position)==2):
                        if move_position in peice_possible_moves(peice_position,enemy_color_finder(peice_position)):
                            (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(move_position[1])][int(move_position[0])][0],position_board[int(move_position[1])][int(move_position[0])][1])
                            board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
                            board[int(peice_position[1])][int(peice_position[0])]='.'
                            if turtle_board[int(move_position[1])][int(move_position[0])] != None:                                    
                                (turtle_board[int(move_position[1])][int(move_position[0])]).ht()
                                (turtle_board[int(move_position[1])][int(move_position[0])]).goto(500,0)
                            turtle_board[int(move_position[1])][int(move_position[0])]=turtle_board[int(peice_position[1])][int(peice_position[0])]
                            turtle_board[int(peice_position[1])][int(peice_position[0])]=None
                            random_computer_output('b')
                            print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7]))
                            king_status()
                            return
                            
        print('incorrect input')
        (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(peice_position[1])][int(peice_position[0])][0],position_board[int(peice_position[1])][int(peice_position[0])][1])
        return
    except:
        print('incorrect input, system fail')
        (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(peice_position[1])][int(peice_position[0])][0],position_board[int(peice_position[1])][int(peice_position[0])][1])
        return

def random_computer_output(color):
    peices_with_moves=[]
    for i in range(8):
        for j in range(8):
            if board[i][j]!='.':
                if board[i][j][0]==color:
                    if peice_possible_moves('{}{}'.format(j,i),enemy_color_finder('{}{}'.format(j,i))) !=[]:peices_with_moves.append('{}{}'.format(j,i))

    random.shuffle(peices_with_moves)
    peice_position=peices_with_moves[0]
    move_position=random.choice(peice_possible_moves(peice_position,enemy_color_finder(peice_position)))
    print(move_position,'position moved to')
    board[int(move_position[1])][int(move_position[0])]=board[int(peice_position[1])][int(peice_position[0])]
    board[int(peice_position[1])][int(peice_position[0])]='.'

    (turtle_board[int(peice_position[1])][int(peice_position[0])]).goto(position_board[int(move_position[1])][int(move_position[0])][0],position_board[int(move_position[1])][int(move_position[0])][1])
    if turtle_board[int(move_position[1])][int(move_position[0])] != None:(turtle_board[int(move_position[1])][int(move_position[0])]).ht()
    turtle_board[int(move_position[1])][int(move_position[0])]=turtle_board[int(peice_position[1])][int(peice_position[0])]
    turtle_board[int(peice_position[1])][int(peice_position[0])]=None
    king_status()

    
while True:
    window.update()


    


