board=[['.','bp','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['wp','bp','.','wp','bp','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['bc','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]


position='35'

def start_pos_finder(position):#a tool for board_stripper_yx
    diagonal=[]
    start_pos=position
    while True:
        print(start_pos)
        if start_pos[0]=='0' or start_pos[1]=='7':
            print(start_pos,'start pos')
            return start_pos
        
        start_pos='{}{}'.format((int(start_pos[0])-1),int(start_pos[1])+1)
        
        



def board_stripper_yx(start_pos):
    diagonal=[]
    print(start_pos)
    start_pos=str(start_pos)
    start_pos='{}{}'.format(int(start_pos[0]),int(start_pos[1]))
    diagonal.append(start_pos)
    
    for i in range(int(start_pos[1])-int(start_pos[0])):
        start_pos='{}{}'.format(int(start_pos[0])+1,int(start_pos[1])-1)
        diagonal.append(start_pos)
    print(diagonal)
    return diagonal
        
def output_possible_moves(possible_moves):
    output_board=board
    print(len(possible_moves))
    for i in range(len(possible_moves)):
        print(possible_moves[i])
        output_board[int((possible_moves[i])[1])][int((possible_moves[i])[0])]='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(output_board[0],output_board[1],output_board[2],output_board[3]
                                                    ,output_board[4],output_board[5],output_board[6],output_board[7]))
    


    
output_possible_moves(board_stripper_yx(start_pos_finder(position)))#board_stripper_yx(position)))
