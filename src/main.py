from src import mancalaBoard

board = mancalaBoard.MancalaBoard(4)
board.print_board()
player_one_turn = True

while not board.check_game_over():
    if player_one_turn:
        print("Player One's Turn")
    else:
        print("Player Two's Turn")

    user_input = int(input("what column will you choose?"))

    while not (1 <= user_input <= 6):
        print("you must input a number between 1 and 6. Please try again.")
        user_input = input("what column will you choose?")

    player_continue = board.move(user_input, player_one_turn)

    if board.check_game_over():
        break

    if not player_continue:
        player_one_turn = not player_one_turn
