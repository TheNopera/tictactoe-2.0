#global variables
Game_still_going = True
winner = None
current_player = "X"



#SET PLAYERS NAME---------------------
class player(object):
    def set_name(self, player1,player2):
        player.player1 = player1
        player.player2 = player2   

player1 = input("Escreva seu nome jogador 1:")
print("Bem vindo {}!".format(player1))
print("Você é o 'X'")

player2 = input("Escreva seu nome jogador 2:")
print("Bem vindo {}!".format(player2))
print("Você é a 'O'")

Players_dic = {"X" : player1, "O" : player2 }









#CONFIRM TO PLAY--------------------------
decisão = False

class Confirmation():
    def menu(self, decisão):
        while decisão == False:
            try:
                Answer = input("Ready to play [y/n]?")
                if Answer in {"y","n"}:
                    decisão = True
                    #print(decisão)
                    break
            finally:
                if Answer == "y":
                    print("let's play")
                elif Answer == "n":
                    print("ok, bye")
                    exit()
                else:
                    print("Write 'y' or 'n'")
                    continue

c = Confirmation()
c.menu(decisão)

#DISPLAY BOARD--------------------------------------------------

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print(board[6] + " | " + board[7] + " | " + board[8] )

b = board

#HANDLE EACH PLAYER TURN-------------------------------------
def handle_turns():
    global current_player
    print("{} is your turn".format(current_player) )
    valid = False
    play = input("choose a number from 1-9: ")
    play = int(play) -1
    while not valid:
        while play > 9 or play < 0:
            play = input("choose a number from 1-9: ")
            play = int(play) -1
        if b[play] == "-":
            valid = True
            b[play] = current_player
            break
        else:
            print("this number is already taken choose another one!")
            play = input("choose a number from 1-9: ")
            play = int(play) -1
            


#check for victories---------------------------------------------
def check_victory():
    global Game_still_going
    #horizontal
    h1 = b[0] == b[1] == b[2] != "-"
    h2 = b[3] == b[4] == b[5] != "-"
    h3 = b[6] == b[7] == b[8] != "-"

    if h1 or h2 or h3:
        Game_still_going = False
        if h1:
            for k,v in Players_dic.items():
                if k == b[0]:
                    print("{} is the winner".format(v))
        elif h2:
            for k,v in Players_dic.items():
                if k == b[3]:
                    print("{} is the winner".format(v))    
        elif h3:
            for k,v in Players_dic.items():
                if k == b[6]:
                    print("{} is the winner".format(v))
        else:
            print("something went really wrong")
        
    #vertical----------------------------------------
    v1 = b[0] == b[3] == b[6] != "-"
    v2 = b[1] == b[4] == b[7] != "-"
    v3 = b[2] == b[5] == b[8] != "-"

    if v1 or v2 or v3:
        Game_still_going = False
        if v1:
            for k,v in Players_dic.items():
                if k == b[0]:
                    print("{} is the winner".format(v))
        elif v2:
            for k,v in Players_dic.items():
                if k == b[1]:
                    print("{} is the winner".format(v))
        elif v3:
            for k,v in Players_dic.items():
                if k == b[2]:
                    print("{} is the winner".format(v))
        else:
            return None

    #diagonal-----------------------------------------
    d1 = b[0] == b[4] == b[8] != "-"
    d2 = b[2] == b[4] == b[6] != "-"

    if d1 or d2:
        Game_still_going = False
        if d1:
            for k,v in Players_dic.items():
                if k == b[0]:
                    print("{} is the winner".format(v))
        elif d2:
            for k,v in Players_dic.items():
                if k == b[2]:
                    print("{} is the winner".format(v))
        else:
            return None

            
#check for a tie -------------------------------------------
def check_tie():
    global Game_still_going
    if "-" not in board:
        print("It's a Tie!")    
        return True
    else:
        return False

#check if the game still going ---------------------------------
def check_if_gameover():
    
    check_victory()

    check_tie()


#flips player turn -------------------------------------------------
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

#Game.main -----------------------------------------------------------
def game():
    while Game_still_going:

        handle_turns()

        display_board()
        
        check_if_gameover()

        flip_player()

game()






