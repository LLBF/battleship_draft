import numpy as np
import random

def print_board():
    print(*["    ", 1, " ", 2, " ", 3, " ", 4, " ", 5, " ", 6, " ", 7, " ", 8, " ", 9, " ", 10])
    for row in range(1, 11):
        if row == 10:
            print(row, board[row - 1])
        else:
            print(row, "", board[row - 1])


def print_empty_board():
    print(*["    ", 1, " ", 2, " ", 3, " ", 4, " ", 5, " ", 6, " ", 7, " ", 8, " ", 9, " ", 10])
    for row in range(1, 11):
        if row == 10:
            print(row, empty_board[row - 1])
        else:
            print(row, "", empty_board[row - 1])


def print_board_m():
    print(*["    ", 1, " ", 2, " ", 3, " ", 4, " ", 5, " ", 6, " ", 7, " ", 8, " ", 9, " ", 10])
    for row in range(1, 11):
        if row == 10:
            print(row, board_m[row - 1])
        else:
            print(row, "", board_m[row - 1])


def print_empty_board_m():
    print(*["    ", 1, " ", 2, " ", 3, " ", 4, " ", 5, " ", 6, " ", 7, " ", 8, " ", 9, " ", 10])
    for row in range(1, 11):
        if row == 10:
            print(row, empty_board_m[row - 1])
        else:
            print(row, "", empty_board_m[row - 1])


# adding ships on player board randomly
def place_ship_4_1(board):
    i = np.random.randint(0, 10)
    j = np.random.randint(0, 10)
    try:
        if board[i, j] == " " and board[i + 1, j] == " " and board[i - 1, j] == " " and board[i, j + 1] == " " and board[i, j - 1] == " ":
            board[i, j] = "O"
            ship1.append((i, j))
            return board

        else:
            return place_ship_4_1(board)

    except IndexError:
        return place_ship_4_1(board)


def place_ship_1_4(board):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_1_4(board)
    direction = random.choice(["N", "S", "E", "O"])

    try:
        if direction == "N":
            final_position = [initial_position[0] - 4, initial_position[1]]
            if final_position[0] < 0 or np.any(board[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_1_4(board)

            else:
                board[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship4.append((initial_position[0], initial_position[1]))
                ship4.append((initial_position[0] - 1, initial_position[1]))
                ship4.append((initial_position[0] - 2, initial_position[1]))
                ship4.append((initial_position[0] - 3, initial_position[1]))
                return board

        elif direction == "S":
            final_position = [initial_position[0] + 4, initial_position[1]]
            if final_position[0] > 9 or np.any(board[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_1_4(board)
            else:
                board[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship4.append((initial_position[0], initial_position[1]))
                ship4.append((initial_position[0] + 1, initial_position[1]))
                ship4.append((initial_position[0] + 2, initial_position[1]))
                ship4.append((initial_position[0] + 3, initial_position[1]))
                return board

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 4]
            if final_position[1] > 9 or np.any(board[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_1_4(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship4.append((initial_position[0], initial_position[1]))
                ship4.append((initial_position[0], initial_position[1] + 1))
                ship4.append((initial_position[0], initial_position[1] + 2))
                ship4.append((initial_position[0], initial_position[1] + 3))
                return board

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 4]
            if final_position[1] < 0 or np.any(board[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_1_4(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship4.append((initial_position[0], initial_position[1]))
                ship4.append((initial_position[0], initial_position[1] - 1))
                ship4.append((initial_position[0], initial_position[1] - 2))
                ship4.append((initial_position[0], initial_position[1] - 3))
                return board
    except:
        return place_ship_1_4


def place_ship_2_3(board):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_2_3(board)
    direction = random.choice(["N", "S", "E", "O"])

    try:
        if direction == "N":
            final_position = [initial_position[0] - 3, initial_position[1]]
            if final_position[0] < 0 or np.any(board[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_2_3(board)

            else:
                board[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship3.append((initial_position[0], initial_position[1]))
                ship3.append((initial_position[0] - 1, initial_position[1]))
                ship3.append((initial_position[0] - 2, initial_position[1]))
                return board

        elif direction == "S":
            final_position = [initial_position[0] + 3, initial_position[1]]
            if final_position[0] > 9 or np.any(board[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_2_3(board)
            else:
                board[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship3.append((initial_position[0], initial_position[1]))
                ship3.append((initial_position[0] + 1, initial_position[1]))
                ship3.append((initial_position[0] + 2, initial_position[1]))
                return board

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 3]
            if final_position[1] > 9 or np.any(board[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_2_3(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship3.append((initial_position[0], initial_position[1]))
                ship3.append((initial_position[0], initial_position[1] + 1))
                ship3.append((initial_position[0], initial_position[1] + 2))
                return board

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 3]

            if final_position[1] < 0 or np.any(board[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_2_3(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship3.append((initial_position[0], initial_position[1]))
                ship3.append((initial_position[0], initial_position[1] - 1))
                ship3.append((initial_position[0], initial_position[1] - 2))
                return board
    except:
        return place_ship_2_3


def place_ship_3_2(board):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_3_2(board)
    direction = random.choice(["N", "S", "E", "O"])

    try:

        if direction == "N":
            final_position = [initial_position[0] - 2, initial_position[1]]

            if final_position[0] < 0 or np.any(board[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_3_2(board)

            else:
                board[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship2.append((initial_position[0], initial_position[1]))
                ship2.append((initial_position[0] - 1, initial_position[1]))
                return board

        elif direction == "S":
            final_position = [initial_position[0] + 2, initial_position[1]]
            if final_position[0] > 9 or np.any(board[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_3_2(board)
            else:
                board[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship2.append((initial_position[0], initial_position[1]))
                ship2.append((initial_position[0] + 1, initial_position[1]))
                return board

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 2]
            if final_position[1] > 9 or np.any(board[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_3_2(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship2.append((initial_position[0], initial_position[1]))
                ship2.append((initial_position[0], initial_position[1] + 1))
                return board

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 2]
            if final_position[1] < 0 or np.any(board[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_3_2(board)

            else:
                board[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship2.append((initial_position[0], initial_position[1]))
                ship2.append((initial_position[0], initial_position[1] - 1))
                return board
    except:
        return place_ship_3_2

# adding ships on player board randomly. '_m' refers to machine

def place_ship_4_1_m(board_m):
    i = np.random.randint(0, 10)
    j = np.random.randint(0, 10)
    try:
        if board_m[i, j] == " " and board_m[i + 1, j] == " " and board_m[i - 1, j] == " " and board_m[i, j + 1] == " " and board_m[i, j - 1] == " ":
            board_m[i, j] = "O"
            ship1_m.append((i, j))
            return board_m

        else:
            return place_ship_4_1_m(board_m)

    except IndexError:
        return place_ship_4_1_m(board_m)


def place_ship_1_4_m(board_m):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_1_4_m(board_m)
    direction = random.choice(["N", "S", "E", "O"])

    try:
        if direction == "N":
            final_position = [initial_position[0] - 4, initial_position[1]]
            if final_position[0] < 0 or np.any(board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_1_4_m(board_m)

            else:
                board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship4_m.append((initial_position[0], initial_position[1]))
                ship4_m.append((initial_position[0] - 1, initial_position[1]))
                ship4_m.append((initial_position[0] - 2, initial_position[1]))
                ship4_m.append((initial_position[0] - 3, initial_position[1]))
                return board_m

        elif direction == "S":
            final_position = [initial_position[0] + 4, initial_position[1]]
            if final_position[0] > 9 or np.any(board_m[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_1_4_m(board_m)
            else:
                board_m[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship4_m.append((initial_position[0], initial_position[1]))
                ship4_m.append((initial_position[0] + 1, initial_position[1]))
                ship4_m.append((initial_position[0] + 2, initial_position[1]))
                ship4_m.append((initial_position[0] + 3, initial_position[1]))
                return board_m

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 4]

            if final_position[1] > 9 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_1_4_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship4_m.append((initial_position[0], initial_position[1]))
                ship4_m.append((initial_position[0], initial_position[1] + 1))
                ship4_m.append((initial_position[0], initial_position[1] + 2))
                ship4_m.append((initial_position[0], initial_position[1] + 3))
                return board_m

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 4]

            if final_position[1] < 0 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_1_4_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship4_m.append((initial_position[0], initial_position[1]))
                ship4_m.append((initial_position[0], initial_position[1] - 1))
                ship4_m.append((initial_position[0], initial_position[1] - 2))
                ship4_m.append((initial_position[0], initial_position[1] - 3))
                return board_m
    except:
        return place_ship_1_4_m


def place_ship_2_3_m(board_m):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_2_3_m(board_m)
    direction = random.choice(["N", "S", "E", "O"])

    try:
        if direction == "N":
            final_position = [initial_position[0] - 3, initial_position[1]]

            if final_position[0] < 0 or np.any(board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_2_3_m(board_m)

            else:
                board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship3_m.append((initial_position[0], initial_position[1]))
                ship3_m.append((initial_position[0] - 1, initial_position[1]))
                ship3_m.append((initial_position[0] - 2, initial_position[1]))
                return board_m

        elif direction == "S":
            final_position = [initial_position[0] + 3, initial_position[1]]
            if final_position[0] > 9 or np.any(board_m[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_2_3_m(board_m)
            else:
                board_m[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship3_m.append((initial_position[0], initial_position[1]))
                ship3_m.append((initial_position[0] + 1, initial_position[1]))
                ship3_m.append((initial_position[0] + 2, initial_position[1]))
                return board_m

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 3]

            if final_position[1] > 9 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_2_3_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship3_m.append((initial_position[0], initial_position[1]))
                ship3_m.append((initial_position[0], initial_position[1] + 1))
                ship3_m.append((initial_position[0], initial_position[1] + 2))
                return board_m

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 3]
            if final_position[1] < 0 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_2_3_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship3_m.append((initial_position[0], initial_position[1]))
                ship3_m.append((initial_position[0], initial_position[1] - 1))
                ship3_m.append((initial_position[0], initial_position[1] - 2))
                return board_m
    except:
        return place_ship_2_3_m


def place_ship_3_2_m(board_m):
    initial_position = [np.random.randint(0, 11), np.random.randint(0, 11)]
    if (initial_position[0] > 9 or initial_position[0] < 0) or (initial_position[1] > 9 or initial_position[1] < 0):
        return place_ship_3_2_m(board_m)
    direction = random.choice(["N", "S", "E", "O"])

    try:

        if direction == "N":
            final_position = [initial_position[0] - 2, initial_position[1]]

            if final_position[0] < 0 or np.any(board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] != " "):
                return place_ship_3_2_m(board_m)

            else:
                board_m[initial_position[0]:final_position[0]:-1, initial_position[1]] = "O"
                ship2_m.append((initial_position[0], initial_position[1]))
                ship2_m.append((initial_position[0] - 1, initial_position[1]))
                return board_m

        elif direction == "S":
            final_position = [initial_position[0] + 2, initial_position[1]]
            if final_position[0] > 9 or np.any(board_m[initial_position[0]:final_position[0], initial_position[1]] != " "):
                return place_ship_3_2_m(board_m)
            else:
                board_m[initial_position[0]:final_position[0], initial_position[1]] = "O"
                ship2_m.append((initial_position[0], initial_position[1]))
                ship2_m.append((initial_position[0] + 1, initial_position[1]))
                return board_m

        elif direction == "E":
            final_position = [initial_position[0], initial_position[1] + 2]
            if final_position[1] > 9 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]] != " "):
                return place_ship_3_2_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]] = "O"
                ship2_m.append((initial_position[0], initial_position[1]))
                ship2_m.append((initial_position[0], initial_position[1] + 1))
                return board_m

        elif direction == "O":
            final_position = [initial_position[0], initial_position[1] - 2]
            if final_position[1] < 0 or np.any(board_m[initial_position[0], initial_position[1]:final_position[1]:-1] != " "):
                return place_ship_3_2_m(board_m)

            else:
                board_m[initial_position[0], initial_position[1]:final_position[1]:-1] = "O"
                ship2_m.append((initial_position[0], initial_position[1]))
                ship2_m.append((initial_position[0], initial_position[1] - 1))
                return board_m
    except:
        return place_ship_3_2_m

# Starts player 1
def shooting():
    try:
        row = int(input("Insert row to shoot: "))-1
        column = int(input("Inserte column to shoot: "))-1
        position = (row, column) #position = (row-1, column-1) ++++

        if row > 1 or row < 10 or column > 1 or column < 10: #if (row > 0 and row < 11) and (column > 0 and column < 11):
            return position

        else:
            print("Out of the board!")
            return shooting()
    except ValueError:
        return shooting()


#machine turn
def machine_shoot():
    row = np.random.randint(1, 11) -1
    column = np.random.randint(1, 11) -1
    random_position = (row, column)
    if row > 1 or row < 10 or column > 1 or column < 10:
        return random_position
    else:
        return machine_shoot()


board = np.full((10, 10), " ")        #board with all boats
empty_board = np.full((10,10), " ")   #player board, machine will shoot it!
board_m = np.full((10, 10), " ")      #board with all boats to shoot by player
empty_board_m = np.full((10,10), " ")

#player ships positions
ship4 = []
ship3 = []
ship2 = []
ship1 = []
barcos_j1 = ship1 + ship2 + ship3 + ship4 #ships_J1 +++++

#machine ships positions
ship4_m = []
ship3_m = []
ship2_m = []
ship1_m = []
barcos_j2 = ship1_m + ship2_m + ship3_m + ship4_m #ships_J2 +++++


#place ships randomly player or J1
place_ship_1_4(board)
place_ship_2_3(board)
place_ship_2_3(board)
place_ship_3_2(board)
place_ship_3_2(board)
place_ship_3_2(board)
place_ship_4_1(board)
place_ship_4_1(board)
place_ship_4_1(board)
place_ship_4_1(board)

#place machine ships randomly * machine or J2
place_ship_1_4_m(board_m)
place_ship_2_3_m(board_m)
place_ship_2_3_m(board_m)
place_ship_3_2_m(board_m)
place_ship_3_2_m(board_m)
place_ship_3_2_m(board_m)
place_ship_4_1_m(board_m)
place_ship_4_1_m(board_m)
place_ship_4_1_m(board_m)
place_ship_4_1_m(board_m)


# THE GAME STARTS!!!
def run():

    print("Let's play battleship!")
    disp = [] ###???
    disp_2 = [] #???
    turno = 1

    while turno < 100:
        while True:
            print("YOUR TURN")
            print_empty_board()
            print_board() #the board with the ships
            shoot = shooting()

            if np.all(board_m[(shoot[0], shoot[0]), (shoot[1], shoot[1])] == " "):
                empty_board[(shoot[0], shoot[0]), (shoot[1], shoot[1])] = "-" #tablero_empty should be board empty of the machine
                board_m[(shoot[0], shoot[0]), (shoot[1], shoot[1])] = "-"

                print("WATER")
                break

            elif np.all(board_m[(shoot[0], shoot[0]), (shoot[1], shoot[1])] == "O"):
                empty_board[(shoot[0], shoot[0]), (shoot[1], shoot[1])] = "X" #machine?!
                board_m[(shoot[0], shoot[0]), (shoot[1], shoot[1])] = "X"
                print("HIT")
                disp_2.append(shoot)
                if "O" not in board_m:
                    print("You won!")
                    break
                else:
                    if shoot in ship1_m:
                        for i in ship1_m:
                            if i == shoot:
                                print("SUNK!")
                                break

                    elif shoot in ship2_m:
                        for i in ship2_m:
                            if ship2_m[0] == shoot or ship2_m[1] == shoot:
                                if ship2_m[0] in disp_2 and ship2_m[1] in disp_2:
                                    print("SUNK")
                                    break
                            elif ship2_m[2] == shoot or ship2_m[3] == shoot:
                                if ship2_m[2] in disp_2 and ship2_m[3] in disp_2:
                                    print("SUNK")
                                    break
                            elif ship2_m[4] == shoot or ship2_m[5] == shoot:
                                if ship2_m[4] in disp_2 and ship2_m[5] in disp_2:
                                    print("SUNK")
                                    break

                    elif shoot in ship3_m:
                        for i in ship3_m:
                            if ship3_m[0] == shoot or ship3_m[1] == shoot or ship3_m[2] == shoot:
                                if ship3_m[0] in disp_2 and ship3_m[1] in disp_2 and ship3_m[2] in disp_2:
                                    print("SUNK")
                                    break
                            elif ship3_m[3] == shoot or ship3_m[4] == shoot or ship3_m[5] == shoot:
                                if ship3_m[3] in disp_2 and ship3_m[4] in disp_2 and ship3_m[5] in disp_2:
                                    print("SUNK")
                                    break

                    elif shoot in ship4_m:
                        for i in ship4_m:
                            if ship4_m[0] == shoot or ship4_m[1] == shoot or ship4_m[2] == shoot or ship4_m[3] == disparo:
                                if ship4_m[0] in disp_2 and ship4_m[1] in disp_2 and ship4_m[2] in disp_2 and ship4_m[3] in disp_2:
                                    print("SUNK")
                                    break
        if "O" not in board_m:
            break

        while True:
            print("Machine turn")
            shoot_m = machine_shoot()

            if np.all(board[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] == " "):
                empty_board_m[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] = "-"  # tablero_empty should be board empty of the machine
                board[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] = "-"
                print("WATER")
                break

            elif np.all(board[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] == "O"):
                empty_board_m[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] = "X"  # machine?!
                board[(shoot_m[0], shoot_m[0]), (shoot_m[1], shoot_m[1])] = "X"
                print("HIT")
                disp.append(shoot_m)
                if "O" not in board:
                    print("You won!")
                    break
            else:
                if shoot_m in ship1:
                    for i in ship1:
                        if i == shoot_m:
                            print("SUNK!")
                            break

                elif shoot_m in ship2:
                    for i in ship2:
                        if ship2[0] == shoot_m or ship2[1] == shoot_m:
                            if ship2[0] in disp_2 and ship2[1] in disp_2:
                                print("SUNK")
                                break
                        elif ship2[2] == shoot_m or ship2[3] == shoot_m:
                            if ship2[2] in disp_2 and ship2[3] in disp_2:
                                print("SUNK")
                                break
                        elif ship2[4] == shoot_m or ship2[5] == shoot_m:
                            if ship2[4] in disp_2 and ship2[5] in disp_2:
                                print("SUNK")
                                break

                elif shoot_m in ship3:
                    for i in ship3:
                        if ship3[0] == shoot_m or ship3[1] == shoot_m or ship3[2] == shoot_m:
                            if ship3[0] in disp_2 and ship3[1] in disp_2 and ship3[2] in disp_2:
                                print("SUNK")
                                break
                        elif ship3[3] == shoot_m or ship3[4] == shoot_m or ship3[5] == shoot_m:
                            if ship3[3] in disp_2 and ship3[4] in disp_2 and ship3[5] in disp_2:
                                print("SUNK")
                                break

                elif shoot_m in ship4:
                    for i in ship4:
                        if ship4[0] == shoot_m or ship4_m[1] == shoot_m or ship4_m[2] == shoot_m or ship4_m[3] == shoot_m:
                            if ship4[0] in disp_2 and ship4[1] in disp_2 and ship4[2] in disp_2 and ship4[3] in disp_2:
                                print("SUNK")
                                break


        if "O" not in board:
            break
        next = input("Press ENTER to continue or 'exit' to exit the game")
        if next == "exit" or next == "EXIT":
            break

        turno += 1

if __name__ == '__main__':
    run()