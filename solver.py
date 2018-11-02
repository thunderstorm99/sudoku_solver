import os
import time

def drawLine():
    print('+-----------------------+')

def drawBoard():
    os.system('clear')
    for row in range(9):
        if(row %3 == 0):
            drawLine()
        for col in range(9):
            if(col%3 == 0):
                print("|" , end=' ')
            if(num[row][col] == 0):
                print(" ", end=' ')
            else:
                print(num[row][col], end=' ')
        print("|")
    drawLine()

def checkcell(val, row, col):
    ### check if number exists in this row or column
    for i in range(9):
        if(num[row][i] == val):
            return False
        elif(num[i][col] == val):
            return False
    
    ### check if number exists in 3x3 box
    _row = int(row/3)*3
    _col = int(col/3)*3
    for i in range(3):
        for j in range(3):
            if(num[_row+i][_col+j] == val):
                return False

    ### if no return False was given previously cell can be filled with val
    return True

# def inputNumbers():
#     row = int(input("Row: "))-1
#     col = int(input("Column: "))-1
#     if(num[row][col] != 0):
#         print("There's something in that cell already!")
#         # time.sleep(2)
#         return
#     possibleNumbers(row, col)
#     # time.sleep(5)

def possibleNumbers(row, col):
    possibilities = 0
    for i in range(1,10):
        if(checkcell(i, row, col)):
            possibilities +=1
            # print(i, " is possible to enter")
            value = i
    # print("There are ", possibilities, " possibilities")
    if(possibilities == 1):
        # print("Great news! There is only one number possible")
        num[row][col] = value
        # drawBoard()
        # time.sleep(0.1)

def solver():
    if(not solved()):
        for x in range(9):
            for y in range(9):
                if(num[x][y] == 0):
                    possibleNumbers(x, y)
        solver()
    else:
        return False

def solved():
    cellssolved = 0
    for x in range(9):
        for y in range(9):
            if(num[x][y] != 0):
                cellssolved +=1
                # print("Cells solved: ", cellssolved)
    if(cellssolved == 81):
        return True
    else:
        return False

def newSudoku():
    print("Please input rows in following format: 123000089")
    print("Empty cells are filled with zeroes")
    for i in range(9):
        print("Please input row ", i+1)
        newline = input()
        if(len(newline) != 9):
            print("invalid input")
        else:
            for j in range(9):
                num[i][j] = int(newline[j])
    print(num)

num = [[1,5,0,6,0,3,0,2,0],
           [0,0,0,0,4,0,3,7,8],
           [3,0,0,0,0,8,0,0,0],
           [5,1,0,0,0,0,9,0,0],
           [0,0,2,0,0,0,6,1,0],
           [0,0,4,3,0,0,2,0,0],
           [7,3,5,8,0,0,0,0,6],
           [0,8,0,0,0,0,0,4,0],
           [0,6,9,0,0,0,8,0,0]]

choice = int(input("Choose what you want to do: \n1. demo\n2. input Sudoku\n"))
if(choice == 1):
    start = time.time()
    solver()
    stop = time.time()
    drawBoard()
    print("It took", stop-start, "seconds")
else:
    newSudoku()
    solver()
