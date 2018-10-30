import os

def printline():
    print('+-----------------+')
def display():
    os.system('clear')
    for row in range(len(numbers)):
        if(row %3 == 0):
            printline()
        for col in range(len(numbers[row])):
            if(col%3 == 0):
                print(f"|{numbers[row][col]}" , end='')
            elif(col == 8):
                print(f" {numbers[row][col]}|" , end='')
            else:
                print(f" {numbers[row][col]}" , end='')
        print("")
    printline()
    input()

def solve():
    display()
    for row in range(len(numbers)):
        print(f"row {row}")
        for col in range(len(numbers[row])):
            print(f"column {col}")
            if(numbers[row][col] == numbers[0][2]):
                print("found empty cell")

numbers = [(1,5,' ',6,' ',3,' ',2,' '),
        (' ',' ',' ',' ',4,' ',3,7,8),
        (3,' ',' ',' ',' ',8,' ',' ',' '),
        (5,1,' ',' ',' ',' ',9,' ',' '),
        (' ',' ',2,' ',' ',' ',6,1,' '),
        (' ',' ',4,3,' ',' ',2,' ',' '),
        (7,3,5,8,' ',' ',' ',' ',6),
        (' ',8,' ',' ',' ',' ',' ',4,' '),
        (' ',6,9,' ',' ',' ',8,' ',' ')]

while True:
    solve()
#solve()
