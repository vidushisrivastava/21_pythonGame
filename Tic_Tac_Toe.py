#tiik-tac-toe
#choose who starts
#pick a place, check, print
#check if won
#switch player
cur_player="x"
game_on=True
board=["-","-","-","-","-","-","-","-","-"]
winner="none"
def game():
    game_board()
    while game_on:
        placement()
        check()
        switch()
#game board
def game_board():
    print(board[0]+ "|" + board[1]+ "|"+ board[2])
    print(board[3]+ "|" + board[4]+ "|"+ board[5])
    print(board[6]+ "|" + board[7]+ "|"+ board[8])

#placement of the x and the o
def placement():
    global board, cur_player,game_on
    print("Current player: " + cur_player)
    place=int(input("Where do you want to place it? "))-1
    while True:
        if board[place]!="-":
            place=int(input("Place already occupied, choose another space "))-1
        
        elif place<0 or place>8:
            place=int(input("Enter a number between 1-9 "))-1        
        else:
            board[place]=cur_player
            game_board()
            return False
#checks for winner or draw
def check():
    global board, cur_player,game_on
    if board[0]==board[1]==board[2]!="-":
        game_on=False
        print("winner is " + board[0])
    elif board[3]==board[4]==board[5]!="-":
        game_on=False
        print("winner is " + board[3])
    elif board[6]==board[7]==board[8]!="-":
        game_on=False
        print("winner is " + board[6])
    elif board[0]==board[3]==board[6]!="-":
        game_on=False
        print("winner is " + board[3])
    elif board[1]==board[4]==board[7]!="-":
        game_on=False
        print("winner is " + board[1])
    elif board[2]==board[5]==board[8]!="-":
        game_on=False
        print("winner is " + board[2])
    elif board[0]==board[4]==board[8]!="-":
        game_on=False
        print("winner is " + board[0])
    elif board[2]==board[4]==board[6]!="-":
        game_on=False
        print("winner is " + board[2])
    elif board[1]!="-" and board[2]!="-" and board[0]!="-" and board[3]!="-" and board[4]!="-" and board[5]!="-" and board[6]!="-" and board[7]!="-" and board[8]!="-":
        print ("Game tied!")
        game_on=False
#switches player
def switch():
    global cur_player
    if cur_player=="x":
        cur_player="o"
    else:
        cur_player="x"
game()