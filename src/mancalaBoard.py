from src import pit

class MancalaBoard:
    def __init__(self, num_default_stones=4):
        self.board = []
        self.player_one_points = 0
        self.player_two_points = 0

        for x in range(0, 14):
            if x == 0 or x == 7:
                self.board.append(pit.Pit(x, x+1, 0))
            elif x == 13:
                self.board.append(pit.Pit(13, 0))
            else:
                self.board.append(pit.Pit(x, x+1, 4))

    def print_board(self):
        if len(self.board) != 14:
            return "board must be 14 spaces in length"

        # prints board edge
        print(" ", end='')
        for x in range(0, 31):
            print("-", end='')
        print()

        # prints opponents row
        print("    | ", end='')
        for x in reversed((range(8, 14))):
            print(str(self.board[x].value) + " | ", end='')
        print()

        print("  " + str(self.board[0].value) + " |", end='')

        # prints score row
        for x in range(0, 23):
            print("-", end='')

        print("| " + str(self.board[7].value))

        # prints player row
        print("    | ", end='')
        for x in range(1, 7):
            print(str(self.board[x].value) + " | ", end='')
        print()

        # prints board edge
        print(" ", end='')
        for x in range(0, 31):
            print("-", end='')
        print()

        # prints numbers for columns
        print("    | ", end='')
        for x in range(1, 7):
            print(str(x) + " | ", end='')
        print()

    def move(self, input_column, player):
        num_stones = 0
        player_two_input_key = {
            1: 13,
            2: 12,
            3: 11,
            4: 10,
            5: 9,
            6: 8
        }

        if not player:
            input_column = player_two_input_key[input_column]
        curr_pit = self.board[input_column]
        num_stones = curr_pit.value
        curr_pit.value = 0  # set current pit to 0
        curr_pit = self.board[curr_pit.next_pit]

        while num_stones > 0:
            curr_pit.value += 1
            curr_pit = self.board[curr_pit.next_pit]
            num_stones -= 1
            print("moved")

        print()
        print()
        self.print_board()

        # TODO: create empty pit capture rule
        # if the turn ends in the store, the player gets to go again
        if curr_pit.index == 1 or curr_pit.index == 8:
            return True
        else:
            return False

    def check_game_over(self):
        player_one_row_sum = 0
        player_two_row_sum = 0

        for x in range(1, 7):
            player_one_row_sum += self.board[x].value

        for x in range(8, 14):
            player_two_row_sum += self.board[x].value

        if player_one_row_sum == 0 or player_two_row_sum == 0:
            return True
        else:
            return False
