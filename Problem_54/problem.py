'''
	Sudoku problem, simply using backtracking will solve.
'''

import random

from copy import deepcopy
from math import ceil

def solve():
	board = create_board()

	backtrack(board, 0, 0)

def display_board(board):
	for row in board:
		print(row)
	print("-"*50)

def backtrack(board, row, col):

	if col >= 9:
		row += 1
		col = 0
	
	if row >= 9:
		return board

	if board[row][col] != -1:
		backtrack(board, row, col + 1)

	for num in range(1, 10):
		board[row][col] = num
		if is_valid(board):
			print(display_board(board))
			board = backtrack(board, row, col + 1)
			if all(-1 not in r for r in board):
				return board
		board[row][col] = -1
	return board

# May run infinitely, oops. Remove and just
# copy the board = ...
def create_board():
	# 9x9
	board = [[-1 for i in range(9)] for j in range(9)]

	# Place random numbers within rows/columns. (Check if validate placement)
	row, col = 0, 0
	while row < 9:
		if random.uniform(0, 1) < .1:
			board[row][col] = random.randint(1, 9)
			while not is_valid(board):
				board[row][col] = random.randint(1, 9)
		col += 1
		if col >= 9:
			row += 1
			col = 0
	return board

def is_valid(board):
	if board is None:
		return board
	# Validate row
	for row in board:
		if not validate_line(row):
			return False

	# Validate column
	for column in range(len(board[0])):
		line = []
		for row in range(len(board)):
			line.append(board[row][column])
		if not validate_line(line):
			return False
	
	# Validate boxes
	for box in range(9):
		if not validate_box(board, box):
			return False

	return True


def validate_line(line):
	if line is None:
		return line
	trending = []
	idx = 0
	while idx < len(line):
		if line[idx] != -1:
			trending.append(line[idx])
		idx += 1
	if len(set(trending)) != len(trending):
		return False
	return True

def validate_box(board, box_number):
	if board is None:
		return None
	if box_number < 0 or box_number > 9:
		return None

	def find_row(box_number):
		val = box_number
		idx = 0
		while val >= 3:
			val = ceil(val / 3)
			idx += 1
		return (idx * 3)

	def find_col(box_number):
		return (box_number % 3) * 3

	row, col = find_row(box_number), find_col(box_number)
	end_row, end_col = row + 3, col + 3
	box = []
	while row < end_row:
		if board[row][col] != -1:
			box.append(board[row][col])
		col += 1
		if col >= end_col:
			col = find_col(box_number)
			row += 1
	if len(set(box)) != len(box):
		return False
	return True

solve()