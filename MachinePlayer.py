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

    # Recursive method to search for a series of hops from some position
    def hop_search(self, row, col, board):
        row_offsets = [-1, 0, 1]
        col_offsets = [-1, 0, 1]
        jumps = []

        # check adjacent squares for blocked positions
        for row_offset in row_offsets:
            for col_offset in col_offsets:
                # Check if the offset is out of bounds on furthest edges
                if (row + row_offset) > board.length or (col + col_offset) > board[0].length:
                    continue

                # Check if the offset is out of bounds on the closest edges
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue

                # Check if the position at the offset is filled
                if (board[row + row_offset][col + col_offset] != 0):
                    # if it is, check the position past it to see if it is empty.
                    # Do this by doubling the x and y offsets and checking that position
                    row_jump_offset = row + 2*row_offset
                    col_jump_offset = col + 2*col_offset

                    if (row_jump_offset) > board.length or (col_jump_offset) > board[0].length:
                        continue

                    if (row_jump_offset) < 0 or (col_jump_offset) < 0:
                        continue

                    # if the space isn't filled, add it to the hops list
                    if (board[row + 2*row_offset][col+2*col_offset] != 0):
                        jumps.append((row + 2*row_offset, col + 2*col_offset))
                        # start a recursive hop search from that empty position
                        # Save all of the further jumps we might find
                        future_hops = self.hop_search(self, row_jump_offset, col_jump_offset, board)
                        # Add them to our list
                        jumps.extend(future_hops)
                        # Return the list back to previous caller
                        return jumps
                    else:
                        # The position was blocked, so return back the empty list
                        return jumps


    # Generate all of the legals moves from some position on the board
    def generate_legal_moves(self, row, col, board):
        # Create the offsets to check
        row_offsets = [-1, 0, 1]
        col_offsets = [-1, 0, 1]

        legal_moves = []
        blocked_spaces = []

        # for every x offset
        for row_offset in row_offsets:
            # for every y offset
            for col_offset in col_offsets:

                # Check if the offset is out of bounds on furthest edges
                if (row + row_offset) > board.length or (col + col_offset) > board[0].length:
                    continue

                # Check if the offset is out of bounds on the closest edges
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue

                # Check if the position at the offset is filled

                if (board[row + row_offset][col + col_offset] == 0):
                    legal_moves.append((row + row_offset, col + col_offset))
                else:
                    blocked_spaces.append((row+row_offset, col + col_offset))

        # For every blocked space, check if there is a hop, or a chain of hops over it
        for blocked_space in blocked_spaces:
            legal_moves.extend(self.hop_search(self, blocked_space[0], blocked_space[1], board))

        return legal_moves



    def minimax(self, node):
        pass