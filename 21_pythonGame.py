#21 game steps
#player chooses how many digits they want to enter
#append to the list
#computer chooses how many digits it wants to enter
#append to the list
#1st one to reach 21 loses :( 

import random
n=0
game_on=True
game_list=[0]
player_name= input("Your name: ")
chance=int(input("Okay "+ player_name + ", you start or the Computer?(ME=1/COMP=2) "))
winner="none"
#main game
def game():
    global n, game_on, winner, player_name,game_list
    chance_choose()  
    if n==1:
        print("Empty Board: %s"%( game_list))
        while game_on:
            print(player_name + "'s chance")
            player()
            if game_on==True:
                print("Computer's chance")
                comp()               

    elif n==2:
        print("Empty Board: %s"%( game_list))
        while game_on:
            print("Computer's chance")
            comp()
            if game_on==True:
                print(player_name + "'s chance")
                player()

    print(winner+ " wins!")
    print("Game over.")
#defining who starts first
def chance_choose():
    global n
    global chance
    while True:
        if chance==1:
            n=1
            return False
        elif chance==2:
            n=2
            return False
        else:
            print()
            chance=int(input(player_name + " Cut the crap. Choose btw 1 and 2.(ME=1/COMP=2)"))

#check if someone reached 21

#player's inputs
def player():
    global game_list,game_on,winner
    digit= int(input("Number of digits you want to enter "))
    n=0
    player_chance=True
    while player_chance:
        if digit<4:
            while n!=digit and len(game_list)<22:
                game_list.append(len(game_list))
                if 21 in game_list:
                    winner="Computer"
                    game_on=False
                n=n+1
            player_chance=False        
        else:
            digit= int(input("Number of digits you want to enter. Must be btw 1-3 "))
        
    print(game_list)

#computer's moves
def comp():
    global game_list,winner,player_name,game_on
    comp_moves=random.randint(1,3)
    n=0
    player_chance=True
    while player_chance:
        while n!=comp_moves and len(game_list)<22:
            game_list.append(len(game_list))
            if 21 in game_list:
                winner=player_name
                game_on=False
            n=n+1
        player_chance=False
    print (game_list)
game()
