__author__ = 'Matt Q'

from Node import Node

class MachinePlayer:

    def move_generator(self, board, player):
        # get all of the pieces that belong to the player
        # for each piece
            # Generate all the legal moves that it can make
            # add those moves to the list of moves that the player can make
        # return the full list of moves
        pass

    def generate_legal_moves(self, row, col, board):
        # Create the offsets to check
        row_offsets = [-1, 0, 1]
        col_offsets = [-1, 0, 1]

        legal_moves = []

        # for every x offset
        for row_offset in row_offsets:
            # for every y offset
            for col_offset in col_offsets:
                pass
                # Check if the offset is out of bounds on furthest edges
                # if (row + row_offset) > board.length or (col + col_offset) > board[0].length:
                    # continue

                # Check if the offset is out of bounds on the closest edges
                # if (row + row_offset) < 0 or (col + col_offset) < 0:
                    # continue

                # Check if the position at the offset is filled

                # if (board[row + row_offset][col + col_offset] == Empty):
                    # legal_moves.append((row,col),(row + row_offset, col + col_offset))
                # If the position is filled, check if the space past it,
                # the jump, is filled.
                # else:
                    # Do this by doubling the x and y offsets and checking that position
                    # if (row + 2*row_offset) > board.length or (col + 2*col_offset) > board[0].length
                        # continue

                    # if (row + 2*row_offset) < 0 or (col + 2*col_offset) < 0:
                        # continue

                    # if the space isn't filled, add it to the legal moves list
                    # if (board[row + 2*row_offset][col+2*col_offset] == Empty):
                        # legal_moves.append((row,col),(row + 2*row_offset, col + 2*col_offset))

        return legal_moves

    def minimax(self, node):
        pass