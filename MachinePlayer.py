__author__ = 'Matt Q'

from Node import Node
from Board import Board

class MachinePlayer:

    def __init__(self):
        self.move_list = []
        self.piece_selected = 0
        self.selected_coords = ()
        self.prevSpots = []

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
                if (row + row_offset) >= len(board) or (col + col_offset) >= len(board[0]):
                    continue

                # Check if the offset is out of bounds on the closest edges
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue

                # Check if we are looking at ourselves
                if (row + row_offset) == row and (col + col_offset) == col:
                    continue

                # Check if the position at the offset is filled
                if (board[row + row_offset][col + col_offset] != 0):
                    # if it is, check the position past it to see if it is empty.
                    # Do this by doubling the x and y offsets and checking that position
                    row_jump_offset = row + 2*row_offset
                    col_jump_offset = col + 2*col_offset

                    if (row_jump_offset) >= len(board) or (col_jump_offset) >= len(board[0]):
                        continue

                    if (row_jump_offset) < 0 or (col_jump_offset) < 0:
                        continue

                    # if the space isn't filled, add it to the hops list
                    if (board[row + 2*row_offset][col+2*col_offset] == 0 and (row + 2*row_offset, col+2*col_offset) not in self.prevSpots):
                        self.prevSpots.append((row, col))
                        jumps.append((row + 2*row_offset, col + 2*col_offset))
                        # start a recursive hop search from that empty position
                        # Save all of the further jumps we might find
                        future_hops = self.hop_search(row_jump_offset, col_jump_offset, board)
                        # Add them to our list
                        jumps.extend(future_hops)
                        self.move_list.extend(future_hops)
                        # Return the list back to previous caller
        return jumps

    # Generate all of the legals moves from some position on the board
    def generate_legal_moves(self, row, col, board):
        # first check if there is a piece at that position to move
        if row >= len(board) or col >= len(board):
            print("That position is out of bounds.")
            return

        if row < 0 or col < 0:
            print("That position is out of bounds.")
            return

        if board[row][col] == 0:
            print("There isn't a piece there to move.")
            return

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
                if (row + row_offset) >= len(board) or (col + col_offset) >= len(board[0]):
                    continue

                # Check if we are looking at ourselves
                if (row + row_offset) == row and (col + col_offset) == col:
                    continue

                # Check if the offset is out of bounds on the closest edges
                if (row + row_offset) < 0 or (col + col_offset) < 0:
                    continue

                # Check if the position at the offset is filled

                if (board[row + row_offset][col + col_offset] == 0):
                    legal_moves.append((row + row_offset, col + col_offset))
                else:
                    blocked_spaces.append((row+row_offset, col + col_offset))


        legal_moves.extend(self.hop_search(row, col, board))
        self.move_list.extend(legal_moves)
        return legal_moves

    def clear_move_list(self):
        self.move_list = []


    '''
     Minimax con alfa-beta
     Pseudocode
     Entrada: Nodo N, valores alfa y beta
     Salida: Valor minimax de dicho nodo

     Si N es nodo hoja entonce devlolver f(N)
     sino
       Si N es nodo MAX entonces
           Para k = 1 hasta b hacer
                alfa = max [alfa, Evaluation(N_k, alfa, beta)]
                Si alfa >= beta then return beta ENDIF
                IF k = b then return alfa ENDIF
            END For loop
        else
            for k = 1 until b DO:
                beta = minimum[beta, Evaluation(N_k, alfa, beta)]
                if alfa >= beta then return alfa ENDIF
                if k = b then return beta ENDIF
            END FOR
        ENDIF
    ENDIF
    '''

    def alphaBetaSearch(self, node):
        pass
        
    def minimax(self, node, alfa, beta):
        # Get the data that we are working with out of the node
        game_board_copy = Board()
        game_board_copy.set_board(node.get_board())

        win_detect = game_board_copy.detectWin()

        if (win_detect[0] == True or win_detect[1] == True or node.get_depth() == 0):
            pass
            # return the evaluation function of the node since we have reached a leaf node

        player = node.get_player()

        if player == 1:
            player_positions = game_board_copy.get_red_positions()
        elif player == 2:
            player_positions = game_board_copy.get_green_positions()


        # if node type is max
            # for every possible position that our player can move from
                # for evey move that can be made from that position
                    # Create a copy of the table that has that particular move made
                    # Create a new node that has that table and set it to be a min node
                    # alpha equals the max of alpha and minimax of the next node and our
                    # current alpha and beta

                    # if alpha is bigger than beta then return beta
                    # if we've reached the end of all possible pieces, return alpha

        # else if node type is min
            # for every possible position that our player can move from
                # for every move that can be made from that position
                    # Create a copy of the table that has that particular move made
                    # Create a new node that has that table, set it to be a max node
                    # Beta equals the minimum of Beta and the minimax of the next node
                    # and our current alpha and beta

                    # if alpha is bigger than beta then return alpha
                    # if we've reached the end