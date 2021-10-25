## Cypher
To Cypher

``` python
text='the text you want to send'
charactars='abcdefghijklmnopqrstuvwxyz123457890,. !?/:;#~[]{}"£$%^&*()abcdefghijklmnopqrstuvwxyz123457890,. !?/:;#~[]{}"£$%^&*()'
key='51251245'
cyphered_text=''
key=(int((len(text)/len(key)))+1)*key
for i in range(len(text)):cyphered_text+=charactars[(charactars.index(text[i]))+int(key[i])] 
print(cyphered_text)
```
To Decypher
``` python
text='yig;ug2y;zqz!yesy!vt!uisi'
charactars='abcdefghijklmnopqrstuvwxyz123457890,. !?/:;#~[]{}"£$%^&*()abcdefghijklmnopqrstuvwxyz123457890,. !?/:;#~[]{}"£$%^&*()'
decyphered_text=''
key='51251245'
key=(int((len(text)/len(key)))+1)*key
for i in range(len(text)):decyphered_text+=charactars[(charactars.index(text[i]))-int(key[i])+58]
print(decyphered_text)
```
