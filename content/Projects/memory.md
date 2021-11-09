```python
import turtle
import random
import time
 
###settings###
time_for_user=0.50
len_of_path=0
#
window = turtle.Screen()
window.title("Memroy")
window.bgcolor('light grey')
window.setup(width=800, height=600)
window.tracer(0)
 
scribe= turtle.Turtle()
scribe.speed(5)
scribe.color("dark grey")
scribe.penup()
scribe.ht()
scribe.goto(320, 250)
level=1
scribe.write("LEVEL {}".format(level),align = "center", font=("sogue UI",14,"normal"))
                       
 
shape0 = turtle.Turtle()
shape0.speed(10)
shape0.shape("square")
shape0.color("dark grey")
shape0.shapesize(stretch_wid=5, stretch_len=5)
shape0.penup()
shape0.goto(0, 0)
 
shape1 = shape0.clone()
shape1.goto(0, 105)
shape2 = shape0.clone()
shape2.goto(0, -105)
shape3 = shape0.clone()
shape3.goto(105, 105)
shape5 = shape0.clone()
shape5.goto(105, 0)
shape6 = shape0.clone()
shape6.goto(-105, 0)
shape7 = shape0.clone()
shape7.goto(-105, -105)
shape8 = shape0.clone()
shape8.goto(105, -105)
shape9 = shape0.clone()
shape9.goto(-105, 105)
 
 
users_input=[]
time.sleep(0.3)
def reset_squares():
      shape0.color("dark grey")
      shape1.color("dark grey")
      shape2.color("dark grey")
      shape3.color("dark grey")
      shape5.color("dark grey")
      shape6.color("dark grey")
      shape7.color("dark grey")
      shape8.color("dark grey")
      shape9.color("dark grey")
 
          
#  1  (middle)
def shape_command_0(x,y):
      print(x,y)
      shape0.color("yellow")
      user_input=1
      users_input.append(user_input)    
shape0.onclick(shape_command_0)
#  2  (top middle)
def shape_command_1(x,y):
      print(x,y)
      shape1.color("yellow")
      user_input=2
      users_input.append(user_input)    
shape1.onclick(shape_command_1)
#  3  (bottom middle)
def shape_command_2(x,y):
      print(x,y)
      shape2.color("yellow")
      user_input=3
      users_input.append(user_input)    
shape2.onclick(shape_command_2)
#  4  (top right)
def shape_command_3(x,y):
      print(x,y)
      shape3.color("yellow")
      user_input=4
      users_input.append(user_input)    
shape3.onclick(shape_command_3)
#  5  (middle right)
def shape_command_5(x,y):
      print(x,y)
      shape5.color("yellow")
      user_input=5
      users_input.append(user_input)    
shape5.onclick(shape_command_5)
#  6  (left middle)
def shape_command_6(x,y):
      print(x,y)
      shape6.color("yellow")
      user_input=6
      users_input.append(user_input)    
shape6.onclick(shape_command_6)
#  7  (bottom left)
def shape_command_7(x,y):
      print(x,y)
      shape7.color("yellow")
      user_input=7
      users_input.append(user_input)    
shape7.onclick(shape_command_7)
#  8  (bottom right)
def shape_command_8(x,y):
      print(x,y)
      shape8.color("yellow")
      user_input=8
      users_input.append(user_input)    
shape8.onclick(shape_command_8)
#  9  (top left)
def shape_command_9(x,y):
      print(x,y)
      shape9.color("yellow")
      user_input=9
      users_input.append(user_input)    
shape9.onclick(shape_command_9)   
window.listen()
 
for i in range(9):
      len_of_path+=1
      users_input=[]
      reset_squares()
     
      #path    
      path_1=[1,2,3,4,5,6,7,8,9]
      path=[]
      path_choice=0
 
      while len(path)<len_of_path:
            path_choice=random.randint(1,9)
            if path_choice not in path:
                  path.append(path_1[path_choice-1])      
      print(path)
 
 
      for i in range(len_of_path):
            print(path[i])
            if path[i]==1:#1
                  shape0.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape0.color("dark grey")
                  window.update()
            if path[i]==2:#2
                  shape1.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape1.color("dark grey")
                  window.update()
            if path[i]==3:#3
                  shape2.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape2.color("dark grey")
                  window.update()
            if path[i]==4:
                  shape3.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape3.color("dark grey")
                  window.update()
            if path[i]==5:
                  shape5.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape5.color("dark grey")
                  window.update()
            if path[i]==6:
                  shape6.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape6.color("dark grey")
                  window.update()
            if path[i]==7:
                  shape7.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape7.color("dark grey")
                  window.update()
            if path[i]==8:
                  shape8.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape8.color("dark grey")
                  window.update()
            if path[i]==9:
                  shape9.color("yellow")
                  window.update()
                  time.sleep(time_for_user)
                  shape9.color("dark grey")
                  window.update()
           
 
 
      while True:         
            window.update()
            if len(users_input) >= len_of_path:
                  if users_input == path:
                        print('correct')
                        window.bgcolor('#009933')
                        window.update()
                        time.sleep(0.75)
                        window.bgcolor('light grey')
                        level+=1
                        scribe.clear()     
                        scribe.write("LEVEL {}".format(level),align = "center", font=("sogue UI",14,"normal"))
                       
                        
                        break
                       
                  else:
                        print('incorrect')
                        window.bgcolor('#ff1a1a')
                        window.update()
```
