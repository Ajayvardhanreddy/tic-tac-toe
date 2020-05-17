# Hey Googlers! This is Ajay Vardhan Reddy. Thank you for visting to my github. Hope you love this game play.
# Board
board = ['', '', '', '', '', '', '', '', '']


def printboard(board):
    print("|", board[0], "|", board[1], "|", board[2], "|", "\n")
    print("|", board[3], "|", board[4], "|", board[5], "|", "\n")
    print("|", board[6], "|", board[7], "|", board[8], "|", "\n")


def boardfull():
    if len(board) == 9:
        return True
    else:
        return False


def printselectboard():
    print("|", 0, "|", 1, "|", 2, "|", "\n")
    print("|", 3, "|", 4, "|", 5, "|", "\n")
    print("|", 6, "|", 7, "|", 8, "|", "\n")


def iswin(boardd,c):
    if boardd[0] == c and boardd[1] == c and boardd[2] == c or boardd[3] == c and boardd[4] == c and boardd[5] == c \
            or boardd[6] == c and boardd[7] == c and boardd[8] == c:
        return True
    elif boardd[0] == c and boardd[3] == c and boardd[6] == c or boardd[1] == c and boardd[4] == c and boardd[7] == c or \
            board[2] == c and board[5] == c and board[8] == c:
        return True
    elif boardd[0] == c and boardd[4] == c and boardd[8] == c or boardd[2] == c and boardd[6] == c and boardd[4] == c:
        return True



def algochoice():
    boardtemp = list(board)
    remainposition = []
    for i in range(0,9):
        if board[i] == '':
            remainposition.append(i)
    # step-1:
    # check can algo wins


    for i in remainposition:
        boardtemp[i] = 'O'
        c = 'O'
        if iswin(boardtemp, c):
            return i

    # step-2
    # stop opponent win
    for i in remainposition:
        boardtemp[i] = 'X'
        c = 'X'
        if iswin(boardtemp, c):
            return i


    # step-3
    # select center position
    if 4 in remainposition:
        return 4

    # step-4
    # select random positions
    import random
    pos = random.randrange(0, len(remainposition))
    return pos




def start():
    chance = 'X'
    win = False
    stop = False
    count = 0
    name=input("Enter player Name")
    print("\n")
    print("{} please start the Game. Poor Algo is waiting for you\n".format(name))
    print("\n")
    while not (boardfull()) or not win or not stop:
        if count == 9:
            print("Oh! Match Tied. Congratulations both of {} and ALgo Bot".format(name))
            return True
        if chance == 'X':
            printselectboard()

            pos = int(input("Please select a position \n"))

            if board[pos] != '':
                print('Position is not empty select another \n')
                continue
            else:
                board[pos] = chance
                count+=1
                printboard(board)
                print("*********************************************************************************************\n")
                chance = 'O'
                if count >= 5:
                    c='X'
                    if iswin(board, c):
                        print(" Congratulations {} you won the match.\n".format(name))
                        return True


        elif chance == 'O':
            print("\n")
            print("Wait! Algo's turn now\n")
            pos = algochoice()
            board[pos] = chance
            count += 1
            chance = 'X'
            printboard(board)
            print("\n")
            print("*************************************************************************************************\n")
            if count >= 5:
                c = 'O'
                if iswin(board, c):
                    print("Algorithm wins the Match. Try again!\n")
                    return True


    return True




print("Hey Googlers!\n")
print("Welcome to Tic-Tac-Toe Game! This is single player game. An algorithm bot plays with you. \n")
print("Game may have few bugs. If you find, then report me!\n")
print("Player value is X \n")
print("Computer value is O \n")
tictactoe = start()
if tictactoe:
    print("Multi player coming soon. Stay Tuned\n")
    print("Execute code again to play \n")
    print("Thank you Googlers for playing")



