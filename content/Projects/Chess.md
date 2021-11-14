## Chess
So far i have been workig on the UI and the engine seperatly
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
# Jake over here

```python
import turtle
window = turtle.Screen()
window.title("chess")
window.bgcolor('white')
window.setup(width=800, height=800)
window.tracer(0)

window.addshape("chess_board_.gif")
board= turtle.Turtle()
board.shape("chess_board_.gif")
board.goto(0,0)
board.pu()

window.addshape("pawn.gif")
wpawn1=turtle.Turtle()
wpawn1.shape("pawn.gif")
wpawn1.pu()

wpawn2=wpawn1.clone()
wpawn3=wpawn1.clone()
wpawn4=wpawn1.clone()
wpawn5=wpawn1.clone()
wpawn6=wpawn1.clone()
wpawn7=wpawn1.clone()
wpawn8=wpawn1.clone()

####
window.addshape("pawn.gif")
bpawn1=turtle.Turtle()
bpawn1.shape("pawn.gif")
bpawn1.pu()

bpawn2=bpawn1.clone()
bpawn3=bpawn1.clone()
bpawn4=bpawn1.clone()
bpawn5=bpawn1.clone()
bpawn6=bpawn1.clone()
bpawn7=bpawn1.clone()
bpawn8=bpawn1.clone()





window.listen()
wpawn1.ondrag(wpawn1.goto)
wpawn2.ondrag(wpawn2.goto)
wpawn3.ondrag(wpawn3.goto)
wpawn4.ondrag(wpawn4.goto)
wpawn5.ondrag(wpawn5.goto)
wpawn6.ondrag(wpawn6.goto)
wpawn7.ondrag(wpawn7.goto)
wpawn8.ondrag(wpawn8.goto)
####
bpawn1.ondrag(bpawn1.goto)
bpawn2.ondrag(bpawn2.goto)
bpawn3.ondrag(bpawn3.goto)
bpawn4.ondrag(bpawn4.goto)
bpawn5.ondrag(bpawn5.goto)
bpawn6.ondrag(bpawn6.goto)
bpawn7.ondrag(bpawn7.goto)
bpawn8.ondrag(bpawn8.goto)


while True:
    window.update()

```
