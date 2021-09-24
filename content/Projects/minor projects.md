# Minor Projects

## Fruit Machine


``` python
import random
player_credit=1
user_input=''
print('type exit for exit')
while player_credit>0 and user_input !='exit':
    slots=[random.randint(0,6),random.randint(0,6),random.randint(0,6)]
    print(slots)
    player_credit-=0.2
    if (slots[0]==6) and (slots[1]==6) and (slots[2]==6):
        player_credit=0
        print('Triple skulls')
    elif (slots[0]==5) and (slots[1]==5) and (slots[2]==5):
        player_credit+=5
        print('Triple Bells')
        
    elif (slots[0]==6 and slots[1]==6) or (slots[1]==6 and slots[2]==6) or (slots[0]==6 and slots[2]==6):
        player_credit-=1
        print('Double skulls')
    elif slots[0]==slots[1] and slots[1]==slots[2]:
        player_credit+=1
        print('triple')
        
    elif (slots[0]== slots[1]) or (slots[1]==slots[2]) or (slots[0]==slots[2]): 
        player_credit+=0.5
        print('Double')
    print(round(player_credit,2))
    user_input=str(input(''))
```
