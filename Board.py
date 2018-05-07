__author__ = 'Matt Q'

class Board:

    GREEN = 2
    RED = 1
    EMPTY = 0

    def __init__(self, size):
        # Board representation
        self.board = []
        self.size = size
        self.greenCorner = []
        self.redCorner = []
        # Initialize the board with all empty spaces
        for i in range(0, size):
            row = []
            for j in range(0, size):
                row.append(self.EMPTY)
            self.board.append(row)

    def detectWin(self):
        greenWin = False
        redWin = False

        # Checking if all the tiles in the green corner are filled with red tiles
        for coord in self.greenCorner:
            if self.get_piece_at(coord[0], coord[1]) == False or self.get_piece_at(coord[0], coord[1]) == 2:
                redWin = False
                break
            elif self.get_piece_at(coord[0], coord[1]) == 1:
                redWin = True

        # Checking if all the tiles in the red corner are filled with green tiles
        for coord in self.redCorner:
            if self.get_piece_at(coord[0], coord[1]) == False or self.get_piece_at(coord[0], coord[1]) == 1:
                greenWin = False
                break
            elif self.get_piece_at(coord[0], coord[1]) == 2:
                greenWin = True

        rtn = (redWin, greenWin)

        return rtn

    def get_board(self):
        return self.board

    def initPieces(self, size):
        for i in range(0, size):
            for j in range(0, size-i):
                self.place_piece(self.RED, i, j)
                self.redCorner.append((i, j))
            cur_row = (size * 2) - (size - i)
            start_col = size * 2 - 1 - i
            end_col = size * 2
            for col in range(start_col, end_col):
                self.place_piece(self.GREEN, cur_row, col)
                self.greenCorner.append((cur_row, col))

    def initGreenPieces(self, size):
        for row in range(0, size):
            cur_row = (size*2) - (size - row)
            start_col = size*2 - 1 - row
            end_col = size*2
            for col in range(start_col, end_col):
                self.place_piece(2, cur_row, col)
                self.greenCorner.append((cur_row, col))

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    # Move a piece from one position to another on the data board
    def move_piece(self, start_pos, end_pos):
        player = self.remove_piece_at(start_pos[0], start_pos[1])
        self.place_piece(player, end_pos[0], end_pos[1])

    def place_piece(self, player, row, col):
        self.board[row][col] = player

    def get_piece_at(self, row, col):
        return self.board[row][col]

    def remove_piece_at(self, row, col):
        # Find what the original piece was at that position
        player = self.board[row][col]
        # Set it to empty
        self.board[row][col] = self.EMPTY
        # Return the original piece that was there
        return player

    def print_board(self):
        for row in self.board:
            print(row)

    def get_green_positions(self):
        green_pos_list = []
        for i in range(0, self.get_height()):
            for j in range(0, self.get_width()):
                if (self.board[i][j]) == self.GREEN:
                    green_pos_list.append((i, j))

        return green_pos_list

    def get_red_positions(self):
        red_pos_list = []
        for i in range(0, self.get_height()):
            for j in range(0, self.get_width()):
                if self.board[i][j] == self.RED:
                    red_pos_list.append((i,j))

        return red_pos_list

    # Create a new copy of a board passed in
    def set_board(self, new_board):
        # Using the copy operator avoids us working with the same
        # board as before
        self.board = new_board.copy()