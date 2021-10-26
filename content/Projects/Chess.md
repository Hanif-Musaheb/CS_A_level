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

```python
forward_move=8
backward_move=-8
left_move=-1
right_move=1




class chess:
    def pawn(postion,move,color):
        possibe_moves=[]
        possible_moves+= 
    
        
board=[['br_1'],['bk_1'],['bb-1'],['bq'],['bK'],['bb-2'],['bk-2'],['br-2'],
    ['bp_1'],['bp_2'],['bp-3'],['bp-4'],['bp-5'],['bp-6'],['bp-7'],['bp-8'],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    ['wp-1'],['wp-2'],['wp-3'],['wp-4'],['wp-5'],['wp-6'],['wp-7'],['wp-8'],
    ['wr-1'],['wk-1'],['wb-1'],['wq'],['wK'],['wb-2'],['wk-2'],['wr-2']]
```
For movement i propose using a method by which you subtract or add to a peices place in an array
```
[-9][-8][-7]
[-1][x][+1]
[+7][+8][+9]
```
This shows the how the would move for only one tile away.

