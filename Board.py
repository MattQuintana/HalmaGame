__author__ = 'Matt Q'

class Board:

    def __init__(self, size):
        # Board representation
        self.board = []
        self.size = size
        # Initialize the board with all empty spaces
        for i in range(0, size):
            row = []
            for j in range(0, size):
                row.append(0)
            self.board.append(row)

    def initRedPieces(self, size):
        for i in range(0, size):
            for j in range(0, size-i):
                self.place_piece(1, i, j)

    def initGreenPieces(self, size):
        for row in range(0, size):
            cur_row = (size*2) - (size - row)
            start_col = size*2 - 1 - row
            end_col = size*2
            for col in range(start_col, end_col):
                self.place_piece(2, cur_row, col)

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    def get_board(self):
        return self.board

    def place_piece(self, player, row, col):
        self.board[row][col] = player

    def get_piece_at(self, row, col):
        return self.board[row][col]

    def remove_piece_at(self, row, col):
        # Find what the original piece was at that position
        player = self.board[row][col]
        # Set it to empty
        self.board[row][col] = 0
        # Return the original piece that was there
        return player

    def print_board(self):
        for row in self.board:
            print(row)