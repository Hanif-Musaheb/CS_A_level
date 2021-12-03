# Chess
So far i have been workig on the UI and the engine seperatly
## Chess Engine
### First Iteration
```python
        
board=[['br1'],['bk1'],['bb1'],['bq'],['bK'],['bb2'],['bk2'],['br2'],
    ['bp1'],['bp2'],['bp3'],['bp4'],['bp5'],['bp6'],['bp7'],['bp8'],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    ['wp1'],['wp2'],['wp3'],['wp4'],['wp5'],['wp6'],['wp7'],['wp8'],
    ['wr1'],['wk1'],['wb1'],['wq'],['wK'],['wb2'],['wk2'],['wr2']]



def pawn_moves(position,color):
    if (position in range(8,16))and color=='b':
        return[position+8,position+16]
    elif (position in range(48,56))and color=='w':
        return[position-8,position-16]
    elif color=='w':
        return[position-8]
    return[position+8]
    

def possible_moves(position):
    possible_moves=[]
    
    color=''
    color=board[position][0][0]
    print(color)
    
    peice_type=''
    peice_type=board[position][0][1]
    print(peice_type)
    
    if peice_type=='p':
        possible_moves+=pawn_moves(position,color)
    
    return possible_moves

def show_possible_move(board,position):
    board_possible_moves=board
    possible_moves_=possible_moves(position)
    for i in range(len(possible_moves_)):
        board_possible_moves[possible_moves_[i]]+='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board_possible_moves[0:8],
                                                    board_possible_moves[8:16],
                                                    board_possible_moves[16:24],
                                                    board_possible_moves[24:32],
                                                    board_possible_moves[32:40],
                                                    board_possible_moves[40:48],
                                                    board_possible_moves[48:56],
                                                    board_possible_moves[56:64]))
        
    
show_possible_move(board,8)
```
For movement i propose using a method by which you subtract or add to a peices place in an array
```
[-9][-8][-7]
[-1][x][+1]
[+7][+8][+9]
```
This shows the how the would move for only one tile away.
### Second Iteration 
The secon iteration came about as the old approach of using an array and using kind of like a long list was very confusing to code a use and is why i could only get part throuhg programming the pawn movement rules. However it lay the gorund work for the method i am using in the second iteration which use an array in that array and yes i know this sounds more complicated but this way i can use it to give the peice coordinates. This removes the annoyance of having a move to the front left be -7 in the array as well as me not knowing how i would detect the edges of the board.
```python
board2=[['bc','.','.','bp','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]

position='00'
possible_moves=[]
def possible_moves(position):
    possible_moves_in=[]
    for i in range(7):
        possible_position='{}{}'.format((i+1),position[1])

        y_pos_pos=int(possible_position[1])
        x_pos_pos=int(possible_position[0])+int(position[0])
        
        if board2[y_pos_pos][x_pos_pos] != '.':
            if (str(board2[y_pos_pos][x_pos_pos]))[0]=='w':
                print(board2[y_pos_pos][x_pos_pos]) 
                possible_moves_in.append(possible_position)#entering possible move
                break
            else: break
        print(board2[y_pos_pos][x_pos_pos]) 
        possible_moves_in.append(possible_position)#entering possible move
        
    for i in range(7):
        possible_position='{}{}'.format(position[1],(i+1))
        #print(possible_position)
        if board2[int(possible_position[1])][int(possible_position[0])] != '.':
            if (str(board2[int(possible_position[1])][int(possible_position[0])]))[0]=='w':
                print(board2[int(possible_position[1])][int(possible_position[0])]) #y,x
                possible_moves_in.append(possible_position)#entering possible move
                break
            else: break
        print(board2[int(possible_position[1])][int(possible_position[0])]) #y,x
        possible_moves_in.append(possible_position)#entering possible move
    return possible_moves_in
    
    
print(possible_moves(position))
```

## UI
### First iteration
(UI code)
```python
import turtle
window = turtle.Screen()
window.title("chess")
window.bgcolor('light grey')
window.setup(width=800, height=800)
window.tracer(0)

window.addshape("chess_board.gif")
load_bar= turtle.Turtle()
load_bar.shape("chess_board.gif")
load_bar.goto(0,0)
load_bar.pu()

while True:
    window.update()

```
chess board is:

![chess_board](https://user-images.githubusercontent.com/90515435/138888602-5da74088-0051-490f-b819-83b5ea5823b7.gif)
![black_horse](https://user-images.githubusercontent.com/90515435/141696372-6871da5d-546f-4520-ad24-20e39b97f2d9.gif)
![horse_white](https://user-images.githubusercontent.com/90515435/141696381-2d4e7758-9442-4abf-967f-241fcf412e08.gif)
![rook_black](https://user-images.githubusercontent.com/90515435/141696387-f72f8168-7db5-4ae7-9595-1505ec59f451.gif)
![rook_white](https://user-images.githubusercontent.com/90515435/141696393-7e099da2-9e27-40b5-82e7-63da8a2a4b91.gif)
![white_pawn](https://user-images.githubusercontent.com/90515435/141697127-e978c715-8cf3-4283-b78a-0557c77094d4.gif)
![black_pawn](https://user-images.githubusercontent.com/90515435/141697132-c86e83a4-1073-4d6a-a594-10db0d725919.gif)
![white_king](https://user-images.githubusercontent.com/90515435/141700963-19b7ad33-28bc-490f-9e4c-f9aaa86d5e46.gif)
![black_king](https://user-images.githubusercontent.com/90515435/141700970-2a7bc674-d81b-4286-8c86-fe003680a273.gif)
![white_queen](https://user-images.githubusercontent.com/90515435/141700974-07bd37d2-ba0e-4a9f-8475-cbf3a5c8d1a8.gif)
![black_queen](https://user-images.githubusercontent.com/90515435/141700979-3c47806a-50e2-4ebe-ac2d-8c823feaebe5.gif)
![white_castle](https://user-images.githubusercontent.com/90515435/141700284-b7b9d68e-139b-4a31-8faf-1a6bd6c37ad4.gif)
![black_castle](https://user-images.githubusercontent.com/90515435/141700290-5d8c7c48-e525-4690-9dba-7d893c8ab91c.gif)

### Second Iteration
```python
import turtle
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

wrook1=turtle.Turtle()
wrook1.shape("white_rook.gif")
wrook1.pu()
wrook1.goto(-120,-280)

wrook2=wrook1.clone()
wrook2.goto(120,-280)

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

brook1=turtle.Turtle()
brook1.shape("black_rook.gif")
brook1.pu()
brook1.goto(-120,280)

brook2=brook1.clone()
brook2.goto(120,280)

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




window.listen()
wpawn1.ondrag(wpawn1.goto)
wpawn2.ondrag(wpawn2.goto)
wpawn3.ondrag(wpawn3.goto)
wpawn4.ondrag(wpawn4.goto)
wpawn5.ondrag(wpawn5.goto)
wpawn6.ondrag(wpawn6.goto)
wpawn7.ondrag(wpawn7.goto)
wpawn8.ondrag(wpawn8.goto)

wcastle1.ondrag(wcastle1.goto)
wcastle2.ondrag(wcastle2.goto)
wrook1.ondrag(wrook1.goto)
wrook2.ondrag(wrook2.goto)
whorse1.ondrag(whorse1.goto)
whorse2.ondrag(whorse2.goto)
wqueen.ondrag(wqueen.goto)
wking.ondrag(wking.goto)

####
bpawn1.ondrag(bpawn1.goto)
bpawn2.ondrag(bpawn2.goto)
bpawn3.ondrag(bpawn3.goto)
bpawn4.ondrag(bpawn4.goto)
bpawn5.ondrag(bpawn5.goto)
bpawn6.ondrag(bpawn6.goto)
bpawn7.ondrag(bpawn7.goto)
bpawn8.ondrag(bpawn8.goto)

bcastle1.ondrag(bcastle1.goto)
bcastle2.ondrag(bcastle2.goto)
brook1.ondrag(brook1.goto)
brook2.ondrag(brook2.goto)
bhorse1.ondrag(bhorse1.goto)
bhorse2.ondrag(bhorse2.goto)
bqueen.ondrag(bqueen.goto)
bking.ondrag(bking.goto)

def kill_peice():
    print('!')

window.onclick(kill_peice())

while True:
    window.update()

```
(evidence of it working)
![image](https://user-images.githubusercontent.com/90515435/142595436-9451735d-aee1-4cc7-8533-9f7558e69d20.png)

