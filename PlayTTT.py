from TTTAI import AI_X, AI_O

# Command line Tic Tac Toe 
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
available_spaces = [str(i) for i in range(1, 10)]

def mode1(): # Player vs Player
	print("To make a move, enter an integer from 1-9 indicating the location of the move.")
	whose_turn = 1

	while not game_over():
		print_game()
		print("Player %s's turn" % str(whose_turn))
		while True:
			next_move = raw_input("Your move: ")
			if next_move in available_spaces and len(next_move) == 1:
				break
			print("Invalid move! Try again")

		make_move(next_move, whose_turn)
		whose_turn = 3 - whose_turn # Switches player

	return game_over()




def mode2(): # Player vs AI
	while True:
		print("Would you like to go first(1) or second(2)?")
		choice = raw_input()
		if choice in ["1", "2"]:
			break
		print("Please enter 1 or 2")

	print("\nTo make a move, enter an integer from 1-9 indicating the location of the move.")
	if choice == "2":
		player_num = 2
		com_num = 1
		com = AI_X()
		move = com.move(board)
		make_move(move, com_num)
	else:
		player_num = 1
		com_num = 2
		com = AI_O()


	while not game_over():
		print_game()
		
		while True:
			next_move = raw_input("Your move: ")
			if next_move in available_spaces and len(next_move) == 1:
				break
			print("Invalid move! Try again")

		make_move(next_move, player_num)
		
		if game_over():
			return game_over()

		# AI's turn
		print_game()
		move = com.move(board)
		make_move(move, com_num)
		print("Com's move: " + move)

	return game_over()












def print_game():
	print("\n\n")
	print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
	print("   " + "--|---|--")
	print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
	print("   " + "--|---|--")
	print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])




def make_move(place, player):
	available_spaces.remove(place)
	place = int(place) - 1
	
	row = place / 3
	col = place % 3
	mark = "X" if player == 1 else "O"
	board[row][col] = mark
	




def game_over(): # Returns winner of game, 0 if it isn't over, and 3 for draw
	flat_board = []
	for row in board:
		flat_board.extend(row)

	def all_same(line):
		return flat_board[int(line[0])] == flat_board[int(line[1])] and \
			   flat_board[int(line[0])] == flat_board[int(line[2])]

	for line in ["012", "345", "678", "036", "147", "258", "048", "246"]:
		if flat_board[int(line[0])] != " " and all_same(line):
			mark = flat_board[int(line[0])]
			player = 1 if mark == "X" else 2
			print_game()
			return player

	if " " not in flat_board:
		return 3
	else:
		return 0





while True:
	print("""\nWelcome to Tic Tac Toe!  Select your desired game mode (Enter 1 or 2) 
	1. Human vs. Human
	2. Human vs. Computer\n""")

	winner = 0
	while winner == 0:
		choice = raw_input()
		if choice == "1":
			winner = mode1()
		elif choice == "2":
			winner = mode2()
		else:
			print("Please enter 1 or 2")

	if winner == 3:
		print_game()
		print("The game ended in a draw")
	else:
		print("Player %s wins!!" % winner)

	while True:
		choice2 = raw_input("\nPress 1 to play again, or 2 to quit:  ")
		if choice2 in ["1", "2"]:
			break
		print("Please press 1 or 2")

	if choice2 == "2":
		print("Thanks for playing!")
		break
	elif choice2 == "1":
		board = [[" "," "," "],[" "," "," "],[" "," "," "]]
		available_spaces = [str(i) for i in range(1, 10)]

