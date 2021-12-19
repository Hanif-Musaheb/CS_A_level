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
