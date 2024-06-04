def display_board(board):    
    print(board[7]+' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4]+' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1]+' | ' + board[2] + ' | ' + board[3])
   
def player_input():
    marker=''
    while marker not in ['X','x','O','o']:
        marker = input('Player 1, Choose between X or O : ').upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    print(f"Player 1 : {player1} \nPlayer 2 : {player2}")    
    return (player1,player2)

def place_marker(board, marker, position):
    
    board[position]=marker
    
def win_check(board, mark):
    if board[7]==board[8]==board[9]==mark:
        return True
    if board[4]==board[5]==board[6]==mark:
        return True
    if board[1]==board[2]==board[3]==mark:
        return True
    if board[1]==board[4]==board[7]==mark:
        return True
    if board[2]==board[5]==board[8]==mark:
        return True
    if board[3]==board[6]==board[9]==mark:
        return True 
    if board[1]==board[5]==board[9]==mark:
        return True
    if board[3]==board[5]==board[7]==mark:
        return True
    return False            

import random

def choose_first():
    chance = random.randint(1,2)
    if chance==2:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    return ' ' not in board[1:10]

def player_choice(board):
    pos=0
    while pos not in range(1,10) or not space_check(board,pos):
        pos= int(input("Enter position(1-9): "))
        if not space_check(board,pos):
            print('Space is already filled')
    return pos    

def replay():
    choice=input("Play Again: Y or N? ")
    return choice=='Y' or choice=='y'    

print('Welcome to Tic Tac Toe!')

while True:
    board=[' ']*10
    p1_marker,p2_marker=player_input()
    turn=choose_first()
    print(turn + ' will go first')
    ready=input('Ready to play? Y or N: ').upper()
    if ready=='Y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player 1':
            display_board(board)
            position=player_choice(board)
            place_marker(board,p1_marker,position)
            if win_check(board,p1_marker):
                display_board(board)
                print('PLAYER 1 HAS WON!!')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("IT'S A TIE")
                    break
                else:
                    turn='Player 2'        
        else:    
            display_board(board)
            position=player_choice(board)
            place_marker(board,p2_marker,position)
            if win_check(board,p2_marker):
                display_board(board)
                print('PLAYER 2 HAS WON!!')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("IT'S A TIE")
                    break
                else:
                    turn='Player 1'             
    if not replay():
        break
print('\n'*50)    