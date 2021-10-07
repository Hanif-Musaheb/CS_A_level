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
## Theif
Unfortunatly I could not successfully complete this I got very close though.
``` python
digits='1234'
for i in range(1000,9999):
    if (str(i).count(str(i)[0]))==digits.count(str(i)[0])and(str(i).count(str(i)[1]))==digits.count(str(i)[1])and(str(i).count(str(i)[2]))==digits.count(str(i)[2])and(str(i).count(str(i)[3]))==digits.count(str(i)[3]):print(i)
 ```
 That code works as it is but not for 0's this is the closest I got trying to program that in:
 ``` python
 digits='1234'    
for i in range(9999):
    if len(str(i))==1 and str(i).count('0')==0 and(str(i).count(str(i)[0]))==digits.count(str(i)[0]):print(i)
    elif len(str(i))==2 and str(i).count('0')==0 and (str(i).count(str(i)[0]))==digits.count(str(i)[0])and(str(i).count(str(i)[1]))==digits.count(str(i)[1]):print(i)
    elif len(str(i))==3 and str(i).count('0')==0 and (str(i).count(str(i)[0]))==digits.count(str(i)[0])and(str(i).count(str(i)[1]))==digits.count(str(i)[1])and(str(i).count(str(i)[2]))==digits.count(str(i)[2]):print('0'+str(i))    
    elif len(str(i))==4 and (str(i).count(str(i)[0]))==digits.count(str(i)[0])and(str(i).count(str(i)[1]))==digits.count(str(i)[1])and(str(i).count(str(i)[2]))==digits.count(str(i)[2])and(str(i).count(str(i)[3]))==digits.count(str(i)[3]):print(i)
    
```
Other attempts included:
``` python
digits=str(input(''))
a=''
a+=5*digits
print(a)

for i in range(1):
    output=''
    for j in range(len(digits)):
        
        output+=a[i+j]
        output+=a[i+j+1]
        output+=a[i+j+2]
        print(output+'\n'+output[::-1])
        
digits=str(input(''))

digits_input=str(input(''))
output=''
digits=3*digits_input
for i in range(len(digits_input)):
    for j in range(len(digits_input)):
        b=digits[]+digits[]

        output=digits[i]+b
        print(output)
        output=digits[i]+b[::-1]
        print(output)


numbers='1234'
for i in range(4):
    for j in range(4):
        for k in range(4):
            for p in range(4):
                numList=[numbers[i],numbers[j],numbers[k],numbers[p]]
                print(numList)

digits_input='1234'
output=''
digits=3*digits_input
def shifter():
    for i in range(len(digits_input)):
        b=digits[i+1]+digits[i+2]
        output=digits[i]+b
        print(output)
        output=digits[i]+b[::-1]
        print(output)

shifter()

digits_input='1234'
output=''
digits=3*digits_input
def shifter(digits,k):
    pair=digits[k+1]+digits[k+2]
    return pair


pair=[digits[0],digits[1],digits[2],digits[3]]
for i in range(4):
    digits[0]=
    
print(pair)

print(shifter(digits,0))

    #b_inv=b[::-1]
    
for i in range(4):
    for j in range(4):
        for k in range(4):
            for p in range(4):
                output+=digits_input[i]+digits_input[j]+digits_input[k]+digits_input[p]
                print(output)
                output=''


pin=['1','2','3','4','1','2','3','4','1','2','3','4']
k=''
j=0
p=0
c=0
for i in range(4):
    k+=pin[i+j]#(1,2,3,4)
    for j in range(3):
        k+=pin[i+1+p]#(234)
        for p in range(2):
            k+=pin[i+2+c]#(34)
            for c in range(1):
                k+=pin[i+3]#(4)
                print(k)
                k=k[0:3]
                print(k+'kkkkkkk')
            print(k)
            k=k[0:2]
        print(k)
        k=k[0:1] 
    print(k)
    k=''


pin=['1','2','3','4','1','2','3','4','1','2','3','4']

j=0
p=0
c=0
def shifter():
    k=''
    for a in range(4):
        k+=pin[a]
        print(k+'a')
        for b in range(3):
            k+=pin[(b+1)-a]
            print(k+'b')
            for c in range(2):
                print
                k+=pin[(c+2)-b+a]
                print(k+'c')
                for d in range(1):
                    k+=pin[(d+3)-c]
                    print(k+'d')
                    k=k[0:3]
                    #print(k+'#')
                k=k[0:2]
                #print(k+'# #')
            k=k[0:1]
        k=''
shifter()

```



































    
    

