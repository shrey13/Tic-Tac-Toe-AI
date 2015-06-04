# AI for Tic Tac Toe
# Shoutout to XKCD for the optimality! http://xkcd.com/832/

from random import choice


class AI1(): # Plays X
	


	def __init__(self):
		self.o_moves = []
		self.prev_board = []
		self.move_num = 0
		self.moves_list = [None, self.move1, self.move2, self.move3, self.move4, self.move5]


	def find_change(self, flat_board):
		old = self.prev_board
		new = flat_board
		for i in range(9):
			if old[i] != new[i]:
				return i+1

	def can_win(self, flat_board):

		def winable(path):
			if "X" not in path:
				return False
			path2 = list(path)
			path2.remove("X")
			return " " in path2 and "X" in path2


		for line in ["012", "345", "678", "036", "147", "258", "048", "246"]:
			path = [flat_board[int(spot)] for spot in line]
			if winable(path):
				return int(line[path.index(" ")]) + 1
		return 0
				



	def move1(self, flat_board):
		return 1

	def move2(self, flat_board):
		diff = self.o_moves[-1]
		if diff % 2 == 0:
			return 5
		else:
			next_moves = {3:7, 5:9, 7:3, 9:3}
			print(diff)
			return next_moves[diff]

	def move3(self, flat_board):
		spot = self.can_win(flat_board)
		if spot:
			return spot # Win if possible

		if self.o_moves[0] != 5:
			print("gg")
		else:
			return 10 - self.o_moves[1] # Awesome how that worked out!

	def move4(self, flat_board):
		spot = self.can_win(flat_board)
		if spot:
			return spot # Win if possible
		else:
			return 10 - self.o_moves[2]

	def move5(self, flat_board):
		for spot in flat_board:
			if spot == " ":
				return spot



	def move(self, board):
		self.move_num += 1
		flat_board = []
		for row in board:
			flat_board.extend(row)

		if self.move_num > 1:
			self.o_moves.append(self.find_change(flat_board))
		next_move = self.moves_list[self.move_num](flat_board)

		flat_board[next_move - 1] = "X"
		self.prev_board = flat_board
		return str(next_move)








class AI2(): # Plays O
	
	def __init__(self):
		self.x_moves = []
		self.prev_board = [" "," "," "," "," "," "," "," "," "]
		self.move_num = 0
		self.moves_list = [None, self.move1, self.move2, self.move3, self.move4]

	def find_change(self, flat_board):
		old = self.prev_board
		new = flat_board
		for i in range(9):
			if old[i] != new[i]:
				return i+1

	def can_win(self, flat_board, mark):

		def winable(path):
			if mark not in path:
				return False
			path2 = list(path)
			path2.remove(mark)
			return " " in path2 and mark in path2 

		for line in ["012", "345", "678", "036", "147", "258", "048", "246"]:
			path = [flat_board[int(spot)] for spot in line]
			if winable(path):
				return int(line[path.index(" ")])+1
		return 0

	def has_two_chances(self, potential_board, mark):

		def winable(path):
			path.remove(mark)
			return " " in path and mark in path 

		chances = 0
		for line in ["012", "345", "678", "036", "147", "258", "048", "246"]:
			path = [flat_board[int(line[spot])] for spot in line]
			if winable(path):
				chances += 1
		return chances >= 2



	def move1(self, flat_board):
		if self.x_moves[0] == 5:
			return 1
		else:
			return 5

	def move2(self, flat_board):
		lose_spot = self.can_win(flat_board, "X")
		if lose_spot:
			return lose_spot

		if self.x_moves[0] == 5 and self.x_moves[1] == 9:
			return choice[3, 7]
		if self.x_moves[0] % 2 == 1:
			if self.x_moves[1] % 2 == 0:
				return 10 - self.x_moves[0]
			else:
				return choice([2, 4, 6, 8])
		else:
			if self.x_moves[1] % 2 == 0:
				return 10 - self.x_moves[1]
			elif sum(self.x_moves) == 10:
				spots = [i for i in range(2, 10, 2) if i not in self.x_moves]
				return choice(spots)
			else:
				if abs(5 - self.x_moves[1]) > abs(5 - self.x_moves[0]):
					self.x_moves = [self.x_moves[1], self.x_moves[0]]
				spot = [i for i in [1, 3, 7, 9] if abs(i - self.x_moves[0] == 1) and 
												   abs(i - self.x_moves[1] == 3) ]
				return spot[0]

	def move3(self, flat_board):
		win_spot = self.can_win(flat_board, "O")
		if win_spot:
			return win_spot
		lose_spot = self.can_win(flat_board, "X")
		if lose_spot:
			return lose_spot

		empties = [i for i in range(9) if flat_board == " "]
		for spot in empties:
			potential_board = list(flat_board)
			potential_board[spot] = "O"
			if two_chances(potential_board, "O"):
				return spot+1

		for spot in empties:
			potential_board = list(flat_board)
			potential_board[spot] = "O"
			empties2 = [i for i in range(9) if potential_board == " "]
			for spot2 in empties2:
				potential2_board = list(flat_board)
				potential2_board[spot] = "X"
				if two_chances(potential2_board, "X"):
					return spot2+1

		return choice(empties)

		

	def move4(self, flat_board):
		win_spot = self.can_win(flat_board, "O")
		if win_spot:
			return win_spot
		lose_spot = self.can_win(flat_board, "X")
		if lose_spot:
			return lose_spot
		
		spots = [i+1 for i in range(9) if flat_board[i] == " "]
		return choice(spots)






	def move(self, board):
		self.move_num += 1
		flat_board = []
		for row in board:
			flat_board.extend(row)

		self.x_moves.append(self.find_change(flat_board))
		print(self.x_moves)
		next_move = self.moves_list[self.move_num](flat_board)

		flat_board[next_move - 1] = "O"
		self.prev_board = flat_board
		return str(next_move)





