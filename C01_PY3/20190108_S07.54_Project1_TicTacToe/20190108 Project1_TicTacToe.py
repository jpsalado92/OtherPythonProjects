import random
import os
import time


def haswon(cells):
    for token in ["X", "O"]:
        if (cells[1] == token and cells[2] == token and cells[0] == token) \
                or (cells[4] == token and cells[5] == token and cells[3] == token) \
                or (cells[7] == token and cells[8] == token and cells[6] == token) \
                or (cells[1] == token and cells[4] == token and cells[7] == token) \
                or (cells[2] == token and cells[5] == token and cells[8] == token) \
                or (cells[0] == token and cells[3] == token and cells[6] == token) \
                or (cells[0] == token and cells[4] == token and cells[8] == token) \
                or (cells[2] == token and cells[4] == token and cells[6] == token):
            win = True
            break
        else:
            win = False
    return win


def drawboard(cellsdb):
    print(" _______ _______ _______ ")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(cellsdb[0], cellsdb[1], cellsdb[2]))
    print("|_______|_______|_______|")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(cellsdb[3], cellsdb[4], cellsdb[5]))
    print("|_______|_______|_______|")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(cellsdb[6], cellsdb[7], cellsdb[8]))
    print("|_______|_______|_______|")
    return None


def whostarts():
    print("This is the TIC TAC TOE GAME, Welcome players!!!!\n"
          "First of all, decide who is going to play Xs and Os\n")
    player1 = input("What is the name of the player playing Os?: ")
    player2 = input("What about the name of the one playing Xs?: ")
    if random.randint(1, 2) == 1:
        osbool = True
        print(player1 + " goes first")
    else:
        osbool = False
        print(player2 + " goes first")

    return player1, player2, osbool


def insert_mark(board_list, osturn):
    if osturn:
        print("It's Os turn...")
    else:
        print("It's Xs turn...")

    cell_to_fill = int(input("Where would you like to put your mark\n"
                             "(Please choose a number from the board)\nTile: ")) - 1
    if osturn:
        board_list[cell_to_fill] = "O"
    elif not osturn:
        board_list[cell_to_fill] = "X"
    else:
        return board_list


os.system('cls')
(player1, player2, ostart) = whostarts()

finished = False
turn = 1
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while finished is not True:
    os.system('cls')
    drawboard(board)
    initialized_board = insert_mark(board, ostart)

    if haswon(board):
        os.system('cls')
        drawboard(board)
        finished = True

        if ostart:
            print("Os won the game!!!, Congratulations {}".format(player1))
        elif not ostart:
            print("Xs won the game!!!, Congratulations {}".format(player2))
        time.sleep(10)

    turn += 1
    ostart = not ostart
    os.system('cls')

    if turn == 10:
        print("The match is a draw")
        finished = True
        time.sleep(10)

print("This game was coded by Juan Pablo Salado")
input("Did you enjoy the game?: ")
