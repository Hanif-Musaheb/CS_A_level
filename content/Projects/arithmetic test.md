# arithmetic test
``` python
import random
import time

user_name=str(input('name?'))
equation_type=['x','/','+','-']
correct=0
wrong=0
def ans(a,rand_num,c):
    if rand_num == 0:
        return (a*c)
    elif rand_num == 1:
        return (a/c)
    elif rand_num == 2:
        return (a+c)
    elif rand_num == 3:
        return (a-c)
def div_ques(a):
    c=a*random.randint(0,9)
    return c
 
    
time_start = time.time()
for i in range(6):
    rand_num=random.randint(2,3)
    a=random.randint(1,99)
    b=equation_type[rand_num]
    c=random.randint(1,99)
    user_input=int(input('{}{}{}= '.format(a,b,c)))
    if user_input==ans(a,rand_num,c):
        correct+=1
        print('correct')
    else:
        wrong+=1
        print('wrong')
        
for i in range(2):
    a=random.randint(0,12)
    c=random.randint(0,12)
    user_input=int(input('{}x{}= '.format(a,c)))
    if user_input==ans(a,0,c):
        correct+=1
        print('correct')
    else:
        wrong+=1
        print('wrong')

for i in range(2):
    c=random.randint(1,12)
    a=c*random.randint(1,12)
    
    user_input=int(input('{}/{}= '.format(a,c)))
    if user_input==ans(a,1,c):
        correct+=1
        print('correct')
    else:
        wrong+=1
        print('wrong')

print('correct:{}\nwrong:{}\nsuccess rate:{}\n time taken:{}'.format(correct,wrong,correct/10,(time.time()-time_start)))
```
