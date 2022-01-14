![image](https://user-images.githubusercontent.com/90515435/148846105-42a2ad49-20aa-476c-8f23-dd5d72fa4453.png)

``` python 
import turtle
turtle.tracer(0)
turtle.ht()
turtle.pu()
turtle.goto(-400,200)
turtle.pd()

def tri(a,depth,recursion):
    recursion+=1
    for i in range(3):
        turtle.fd(a)
        turtle.rt(120)
        if depth>recursion:tri(a/2,depth,recursion)

for i in range(6):
    tri(120,i+1,0)
    turtle.fd(120)

while True:
    turtle.update()
    
 
```
