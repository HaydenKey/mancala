class MancalaBoard:
    def __init__(self, num_stones=4):
        self.board = []
        self.player_one_points = 0
        self.player_two_points = 0

        for x in range(0, 14):
            if not (x == 0 or x == 7):
                self.board.append(num_stones)
            else:
                self.board.append(0)

    @staticmethod
    def print_board(board):
        if len(board) != 14:
            return "board must be 14 spaces in length"

        # prints board edge
        print(" ", end='')
        for x in range(0, 31):
            print("-", end='')
        print()

        # prints opponents row
        print("    | ", end='')
        for x in range(1, 7):
            print(str(board[x]) + " | ", end='')
        print()

        print("  " + str(board[0]) + " |", end='')

        # prints score row
        for x in range(0, 23):
            print("-", end='')

        print("| " + str(board[7]))

        # prints player row
        print("    | ", end='')
        for x in range(8, 14):
            print(str(board[x]) + " | ", end='')
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

    def move(self, col, player):
        while self.board[col] > 0:
            num_stones = 0

            if player:
                num_stones = self.board[col]
                self.board[col] = 0
            else:
                num_stones = self.board[col + 6]
                self.board[col] = 0

            if 1 <= col <= 6:
                col -= 1
            else:
                col += 5

            while num_stones > 0:
                if 1 <= col <= 6:
                    self.board[col] += 1
                    num_stones -= 1
                    col -= 1

                if 8 <= col < 13:
                    self.board[col] += 1
                    num_stones -= 1
                    col += 1

                if col == 13:
                    self.board[col] += 1
                    num_stones -= 1
                    col = 7

                if col == 0:
                    if player:
                        self.board[col] += 1
                        num_stones -= 1
                        col = 8
                    else:
                        col = 8

                if col == 7:
                    if not player:
                        self.board[col] += 1
                        num_stones -= 1
                        col = 6
                    else:
                        col = 6

            print()
            print()
            self.print_board()

        print("got here")
        # if the turn ends in the store, the player gets to go again
        if col == 0 or col == 7:
            return True
        else:
            return False

    def check_game_over(self):
        player_one_row_sum = 0
        player_two_row_sum = 0

        for x in range(1, 7):
            player_one_row_sum += self.board[x]

        for x in range(8, 14):
            player_two_row_sum += self.board[x]

        if player_one_row_sum == 0:
            return 1
        elif player_two_row_sum == 0:
            return 2
        else:
            return 0
