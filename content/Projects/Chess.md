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
[Bishop Possible Moves](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/Bishop%20Possible%20Moves.py)


## UI
### First iteration
(UI code)
<Br>
[First Iteration](https://github.com/Hanif-Musaheb/CS_A_level/blob/main/content/Projects/chess%20files/ui%20first%20iteration.py)
<Br>
chess board is:

![chess_board](https://user-images.githubusercontent.com/90515435/138888602-5da74088-0051-490f-b819-83b5ea5823b7.gif)
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

