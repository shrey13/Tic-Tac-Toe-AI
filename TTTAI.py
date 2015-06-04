# AI for Tic Tac Toe
# Shoutout to XKCD for the optimality! http://xkcd.com/832/

from random import choice


class AI():

	def __init__(self):
		self.mark = " "
		self.other_moves = []
		self.prev_board = [" "]*9
		self.move_num = 0
		


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
				return int(line[path.index(" ")]) + 1
		return 0


	def two_chances(self, potential_board, mark):

		def winable(path):
			if mark not in path:
				return False
			path2 = list(path)
			path2.remove(mark)
			return " " in path2 and mark in path2

		chances = 0
		for line in ["012", "345", "678", "036", "147", "258", "048", "246"]:
			path = [potential_board[int(spot)] for spot in line]
			if winable(path):
				chances += 1
		return chances >= 2


	def can_force_win(self, flat_board, mark):

		empties = [i for i in range(9) if flat_board[i] == " "]
		for spot in empties:
			potential_board = list(flat_board)
			potential_board[spot] = mark
			if self.two_chances(potential_board, mark):
				return spot+1
		return 0


	def move(self, board):  # Only method called externally
		self.move_num += 1
		flat_board = []
		for row in board:
			flat_board.extend(row)

		if self.prev_board != flat_board:
			self.other_moves.append(self.find_change(flat_board))
		next_move = self.moves_list[self.move_num](flat_board)

		flat_board[next_move - 1] = self.mark
		self.prev_board = flat_board
		return str(next_move)







class AI_X(AI): # Plays X
	
	def __init__(self):
		AI.__init__(self)
		self.mark = "X"	
		self.moves_list = [None, self.move1, self.move2, self.move3, self.move4, self.move5]



	def move1(self, flat_board):
		return 1


	def move2(self, flat_board):
		diff = self.other_moves[-1]
		if diff % 2 == 0:
			return 5
		else:
			next_moves = {3:7, 5:9, 7:3, 9:3}
			print(diff)
			return next_moves[diff]


	def move3(self, flat_board):
		win_spot = self.can_win(flat_board, "X")
		if win_spot:
			return win_spot

		if self.other_moves[0] != 5:
			return self.can_force_win(flat_board, "X")
		else:
			return 10 - self.other_moves[1] # Awesome how that worked out!


	def move4(self, flat_board):
		win_spot = self.can_win(flat_board, "X")
		if win_spot:
			return win_spot
		lose_spot = self.can_win(flat_board, "O")
		if lose_spot:
			return lose_spot
		# That's all that can happen


	def move5(self, flat_board):
		for spot in flat_board:
			if spot == " ":
				return spot





class AI_O(AI): # Plays O
	
	def __init__(self):
		AI.__init__(self)
		self.mark = "O"
		self.moves_list = [None, self.move1, self.move2, self.move3, self.move4]



	def move1(self, flat_board):
		if self.other_moves[0] == 5:
			return 1
		else:
			return 5


	def move2(self, flat_board):
		lose_spot = self.can_win(flat_board, "X")
		if lose_spot:
			return lose_spot

		if self.other_moves[0] == 5 and self.other_moves[1] == 9:
			return choice[3, 7]
		if self.other_moves[0] % 2 == 1:
			if self.other_moves[1] % 2 == 0:
				return 10 - self.other_moves[0]
			else:
				return choice([2, 4, 6, 8])
		else:
			if self.other_moves[1] % 2 == 0:
				return 10 - self.other_moves[1]
			elif sum(self.other_moves) == 10:
				spots = [i for i in range(2, 10, 2) if i not in self.other_moves]
				return choice(spots)
			else:
				if abs(5 - self.other_moves[1]) > abs(5 - self.other_moves[0]):
					self.other_moves = [self.other_moves[1], self.other_moves[0]]
				spot = [i for i in [1, 3, 7, 9] if abs(i - self.other_moves[0] == 1) and 
												   abs(i - self.other_moves[1] == 3) ]
				return spot[0]


	def move3(self, flat_board):
		win_spot = self.can_win(flat_board, "O")
		if win_spot:
			return win_spot
		lose_spot = self.can_win(flat_board, "X")
		if lose_spot:
			return lose_spot

		force_win_spot = self.can_force_win(flat_board, "O")
		if force_win_spot:
			return force_win_spot


		empties = [i for i in range(9) if flat_board[i] == " "]
		for spot in empties:
			potential_board = list(flat_board)
			potential_board[spot] = "O"
			force_lose_spot = self.can_force_win(potential_board, "X")
			if force_lose_spot:
				return force_lose_spot

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

