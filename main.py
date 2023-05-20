def showBoard(x, o):
    one = "X" if x[0] == "X" else "O" if o[0] == "O" else "1"
    two = "X" if x[1] == "X" else "O" if o[1] == "O" else "2"
    three = "X" if x[2] == "X" else "O" if o[2] == "O" else "3"
    four = "X" if x[3] == "X" else "O" if o[3] == "O" else "4"
    five = "X" if x[4] == "X" else "O" if o[4] == "O" else "5"
    six = "X" if x[5] == "X" else "O" if o[5] == "O" else "6"
    seven = "X" if x[6] == "X" else "O" if o[6] == "O" else "7"
    eight = "X" if x[7] == "X" else "O" if o[7] == "O" else "8"
    nine = "X" if x[8] == "X" else "O" if o[8] == "O" else "9"

    print(f" {one} | {two} | {three} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print("---|---|---")
    print(f" {seven} | {eight} | {nine} ")


def checkWin(x, o):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in wins:
        X = 0
        O = 0
        for j in i:
            if x[j] == "X":
                X += 1
            elif o[j] == "O":
                O += 1

        if X == 3:
            print("X wins")
            return 1

        if O == 3:
            print("O wins")
            return 0

    return -1



if __name__ == "__main__":
    text = '''
------------------------------welcome to tic tac toe game-------------------------------------------
    '''
    print(text)
    turn = 1
    xstatus = ["", "", "", "", "", "", "", "", ""]
    ostatus = ["", "", "", "", "", "", "", "", ""]
    running = True

    while running:
        showBoard(xstatus, ostatus)

        if turn == 1:
            print("X's turn")
            xinput = int(input("Enter position of X:"))
            if xinput < 1 or xinput > 9:
                print("invalid")
                continue
            if "X" in xstatus[xinput-1] or "O" in ostatus[xinput-1]:
                print("enter new place!")
                continue
            xstatus.pop(xinput-1)
            xstatus.insert(xinput-1, 'X')

        else:
            print("O's turn")
            oinput = int(input("Enter position of O:"))
            
            if oinput < 1 or oinput > 9:
                print("invalid")
                continue
            if ("O" in ostatus[oinput-1] or "X" in xstatus[oinput-1]):
                print("enter new place!")
                continue
            ostatus.pop(oinput-1)
            ostatus.insert(oinput-1, 'O')
            
        checkWin(xstatus, ostatus)

        if checkWin(xstatus, ostatus) != -1:

            break

        turn = 1-turn
