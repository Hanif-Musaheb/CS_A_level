# Chess
So far i have been workig on the UI and the engine seperatly
## Chess Engine
### First Iteration
[First Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/first%20iteration.py)


For movement i propose using a method by which you subtract or add to a peices place in an array
```
[-9][-8][-7]
[-1][x][+1]
[+7][+8][+9]
```
This shows the how the would move for only one tile away.
### Second Iteration 
The secon iteration came about as the old approach of using an array and using kind of like a long list was very confusing to code a use and is why i could only get part throuhg programming the pawn movement rules. However it lay the gorund work for the method i am using in the second iteration which use an array in that array and yes i know this sounds more complicated but this way i can use it to give the peice coordinates. This removes the annoyance of having a move to the front left be -7 in the array as well as me not knowing how i would detect the edges of the board.

[Second Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/Second%20Iteration.py)

creation of a function that looks at the tiles on the x axis and the y axis of the peice

### Third Iteration
I worked around 6hrs straight to improve the code to what it is now which can show all the possible moves for a castle. Although this may not sound like much it a major peice of the puzzle solved as now using the same code with a few minor tweaks i can get it to scan possible moves in a diagonal for bishop and queen and other peices should be easier like a king which is similar to a castle.

[Third Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/third%20Iteration.py)


(Use of the code above and the third iteration code)
<Br>
![image](https://user-images.githubusercontent.com/90515435/145687879-b39b9cb5-6f48-4c7a-bef6-28109f8a372e.png)
        
        
[x5 (possible diagonal moves)](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/x5.py)
<Br>
[Bishop Possible Moves](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/Bishop%20Possible%20Moves.py)
### Fourth Iteration
19/12/21: I will hopefully be using this iteration for a while as my as the head way i making on the project has brought about too many iterations so I will use this till all the possible moves for all the peices are made. So far I have made the castle which was in the prior iteration and now I have made the bishop, which was supprisingly challemging as there were only a few lines of the castle code i could re use and little but more of the structure. Next I will make the queen which is just a combination of the two. 
<Br>
[Fourth Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/first%20iteration.py) 
22/12/21: Over the past few days i have completed the different peices possible moves starting with the queen, being very easy as it was just a combination of the rook and the bishop. Then the king to which i made a list of the possible moves relative to its position (-1,0 being to the left of the king 0,1 being above the king and so on aswell as making conditions for it being on the side of the board). For the horse i did the same thing which i was not really expecting to work but did and made programming the horse relatively easy. The pawn was a lot easier than the bishop and castle but was anoying with its exception and weird rules. However i have not programmed en passant and don't plan to. So with those additions i have completed iteration 4 and will move on to making the chess possible moves work for both colors.
### Fifth Iteration
[Fifth Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/Fifth%20Iteration.py)
23/12/21: I have now made it so that to show the possible moves you just have to input the position of the peice and the algorithm determines the color and the peice meaning all tou have to input in is the position which makes closer to the engine being complete.
``` 
w/bp - white/black pawn
w/bc - white/black castle
w/bh - white/black horse
w/bb - white/black bishop
w/bq - white/black queen
w/bk - white/black king
```
Next i guess i should create an algorithm to check whether or not the king is in check.
<Br>
This lead me onto a bug that was very confusing as i had no idea what pointers were and now that i know how to use ```id()``` and ```list()``` so it took a while to understand that all list have different places in the RAM even lists inside lists. Solved the pointers problem  ```for i in range(8):output_board.append(list(board[i]))```
<Br>
<Br>
I realised an end to iteration 5 it will be complete when i can get the computer to play against me randomly but legally.
24/12/21: Very close to ending iteration 5 now i have got the computer to play against me legally and randomly which was really good idea as it exposed a lot of bugs in my program one of which was very annoying to get rid of but i rewrote the diagonal move section so that it works now. In iteration 6 or whatever i call it since it will be combining my UI code with my engine i should be able to flush out any of the remaining bugs in the engine as it will be a lot easier to see whats happening heres what i can see now.
        <Br>
        <img width="344" alt="image" src="https://user-images.githubusercontent.com/90515435/147374150-22d9ed40-4b02-4e4c-a2e8-f50c1c1068a9.png">
        <Br>
 The last parts of iteration 5 will be implementing the checking code i have already made, checkmate and a mechanic that allows the user to change the pawn into a queen, horse, bishop or castle.
### Sixth Iteration
In this iteration i am combining the UI with Engine which means the next iteration will have AI.
<Br>
[Iteration 6](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/sixth%20iteration.py)
<Br>
I have now coded it to the point where you are playing against the computer by dragging peices to where you want them to move a massive upgrade over typing in coordinates which was sooo annoying. Although the computer is just playing completely randomly which is the next challenge. Still this iteration marks the end of building the engine something that took ages and is now (combined with the UI) over 500 lines long.
1/1/22:I debugged the code a bit and added castling somethin I forgot to add earlier.

## UI
### First iteration
(UI code)
<Br>
[First Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/ui%20first%20iteration.py)
<Br>
chess board is:
<Br>
![board](https://user-images.githubusercontent.com/90515435/147831407-1106ea0d-ee94-4135-9a71-660d8a9aab3e.gif)
![black_horse](https://user-images.githubusercontent.com/90515435/141696372-6871da5d-546f-4520-ad24-20e39b97f2d9.gif)
![horse_white](https://user-images.githubusercontent.com/90515435/141696381-2d4e7758-9442-4abf-967f-241fcf412e08.gif)
![rook_black](https://user-images.githubusercontent.com/90515435/141696387-f72f8168-7db5-4ae7-9595-1505ec59f451.gif)
![rook_white](https://user-images.githubusercontent.com/90515435/141696393-7e099da2-9e27-40b5-82e7-63da8a2a4b91.gif)
![white_pawn](https://user-images.githubusercontent.com/90515435/141697127-e978c715-8cf3-4283-b78a-0557c77094d4.gif)
![black_pawn](https://user-images.githubusercontent.com/90515435/141697132-c86e83a4-1073-4d6a-a594-10db0d725919.gif)
![white_king](https://user-images.githubusercontent.com/90515435/141700963-19b7ad33-28bc-490f-9e4c-f9aaa86d5e46.gif)
![black_king](https://user-images.githubusercontent.com/90515435/141700970-2a7bc674-d81b-4286-8c86-fe003680a273.gif)
![white_queen](https://user-images.githubusercontent.com/90515435/141700974-07bd37d2-ba0e-4a9f-8475-cbf3a5c8d1a8.gif)
![black_queen](https://user-images.githubusercontent.com/90515435/141700979-3c47806a-50e2-4ebe-ac2d-8c823feaebe5.gif)
![white_castle](https://user-images.githubusercontent.com/90515435/141700284-b7b9d68e-139b-4a31-8faf-1a6bd6c37ad4.gif)
![black_castle](https://user-images.githubusercontent.com/90515435/141700290-5d8c7c48-e525-4690-9dba-7d893c8ab91c.gif)

### Second Iteration
[Second Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/ui%20second%20iteration.py)

(evidence of it working)
![image](https://user-images.githubusercontent.com/90515435/142595436-9451735d-aee1-4cc7-8533-9f7558e69d20.png)
        
## AI
So now i am starting teh AI section of the chess project the final section which should mean im around 2/3 of the way through what seems like and endless project. To start this i watch a video showing a very summerised way someone else coded their AI and from that video i got the idea to start the AI by coding the AI to evaluate it's self by using my arbitrary values of the peices and evaulate every possible move it can make on its turn and choose the one where it has the highest value.
```
        pawn   = 100
        bishop = 400
        horse  = 400
        castle = 600
        queen  = 1000
        king   = 1000000
 ```
        

