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
