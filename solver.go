package main

import (
	"fmt"
	"time"
)

func drawLine() {
	fmt.Println("+-----------------------+")
}

func drawBoard() {
	for row := 0; row < 9; row++ {
		if row%3 == 0 {
			drawLine()
		}
		for col := 0; col < 9; col++ {
			if col%3 == 0 {
				fmt.Print("| ")
			}
			if num[row][col] == 0 {
				fmt.Print(" ")
			} else {
				fmt.Print(num[row][col])
			}
			fmt.Print(" ")
		}
		fmt.Println("|")
	}
	drawLine()
}

func checkCell(val, row, col int) bool {
	/* first check if number exists in row or column */
	for i := 0; i < 9; i++ {
		if num[row][i] == val {
			// fmt.Println(val, "exists in row", row)
			return false
		} else if num[i][col] == val {
			// fmt.Println(val, "exists in col", col)
			return false
		}
	}

	/* check if number exists in 3x3 box */
	var _row = int(row/3) * 3
	var _col = int(col/3) * 3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if num[_row+i][_col+j] == val {
				return false
			}
		}
	}
	/* if no return false was given previously, cell can be filled with val */
	return true
}

func possibleNumbers(row, col int) {
	var possibilities = 0
	var value int
	for i := 1; i < 10; i++ {
		if checkCell(i, row, col) {
			possibilities += 1
			value = i
			// fmt.Println(value, "is a possibility")
		}
	}
	if possibilities == 1 {
		num[row][col] = value
	}
}

func solver() bool {
	var cellsolved = 0
	for row := 0; row < 9; row++ {
		for col := 0; col < 9; col++ {
			if num[row][col] == 0 {
				possibleNumbers(row, col)
			} else {
				cellsolved += 1
			}
			if cellsolved == 81 {
				return true
			}
		}
	}
	// fmt.Print("cellsolved =", cellsolved)
	return false
}

var num = [9][9]int{
	{1, 5, 0, 6, 0, 3, 0, 2, 0},
	{0, 0, 0, 0, 4, 0, 3, 7, 8},
	{3, 0, 0, 0, 0, 8, 0, 0, 0},
	{5, 1, 0, 0, 0, 0, 9, 0, 0},
	{0, 0, 2, 0, 0, 0, 6, 1, 0},
	{0, 0, 4, 3, 0, 0, 2, 0, 0},
	{7, 3, 5, 8, 0, 0, 0, 0, 6},
	{0, 8, 0, 0, 0, 0, 0, 4, 0},
	{0, 6, 9, 0, 0, 0, 8, 0, 0}}

func main() {
	drawBoard()
	start := time.Now()
	for !solver() {
	}
	stop := time.Now()
	drawBoard()
	fmt.Println("Operation took", stop.Sub(start))
	// possibleNumbers(2, 2)
}
