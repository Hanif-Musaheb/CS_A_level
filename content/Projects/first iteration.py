        
board=[['br1'],['bk1'],['bb1'],['bq'],['bK'],['bb2'],['bk2'],['br2'],
    ['bp1'],['bp2'],['bp3'],['bp4'],['bp5'],['bp6'],['bp7'],['bp8'],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],
    ['wp1'],['wp2'],['wp3'],['wp4'],['wp5'],['wp6'],['wp7'],['wp8'],
    ['wr1'],['wk1'],['wb1'],['wq'],['wK'],['wb2'],['wk2'],['wr2']]



def pawn_moves(position,color):
    if (position in range(8,16))and color=='b':
        return[position+8,position+16]
    elif (position in range(48,56))and color=='w':
        return[position-8,position-16]
    elif color=='w':
        return[position-8]
    return[position+8]
    

def possible_moves(position):
    possible_moves=[]
    
    color=''
    color=board[position][0][0]
    print(color)
    
    peice_type=''
    peice_type=board[position][0][1]
    print(peice_type)
    
    if peice_type=='p':
        possible_moves+=pawn_moves(position,color)
    
    return possible_moves

def show_possible_move(board,position):
    board_possible_moves=board
    possible_moves_=possible_moves(position)
    for i in range(len(possible_moves_)):
        board_possible_moves[possible_moves_[i]]+='x'
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(board_possible_moves[0:8],
                                                    board_possible_moves[8:16],
                                                    board_possible_moves[16:24],
                                                    board_possible_moves[24:32],
                                                    board_possible_moves[32:40],
                                                    board_possible_moves[40:48],
                                                    board_possible_moves[48:56],
                                                    board_possible_moves[56:64]))
        
    
show_possible_move(board,8)
