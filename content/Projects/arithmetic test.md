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

  
time_start = time.time()
for i in range(10):
    rand_num=random.randint(0,3)
    e=99 
    if rand_num==0:
        e=12
    if rand_num==1:
        c=random.randint(1,12)
        a=c*random.randint(2,12)
    
    else :
        a=random.randint(1,e)
        c=random.randint(1,e)
        
    b=equation_type[rand_num]

    
    user_input=int(input('{}{}{}= '.format(a,b,c)))
    if user_input==ans(a,rand_num,c):
        correct+=1
        print('correct')
    else:
        wrong+=1
        print('wrong')
        


print('correct:{}\nwrong:{}\nsuccess rate:{}\n time taken:{}'.format(correct,wrong,correct/10,(time.time()-time_start)))

```
