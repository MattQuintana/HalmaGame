__author__ = 'Matt Q'

from Node import Node
from Board import Board
import time
import math

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


    def distance(self, p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def utility(self, node):
        board = node.board
        value = 0
        for col in range(board.get_width()):
            for row in range(board.get_width()):
                data_board = board.get_board()
                tile = data_board[row][col]

                #green piece
                if tile == 2:
                    distanceList = [self.distance((row,col),goals) for goals in board.redCorner if data_board[goals[0]][goals[1]] != 2]
                    if node.player == 1:
                        value += max(distanceList) if len(distanceList) else -100
                    else:
                        value -= max(distanceList) if len(distanceList) else -100

                #red piece
                elif tile == 1:
                    #elif red piece then create distance list for red
                    distanceList = [self.distance((row,col),goals) for goals in board.redCorner if data_board[goals[0]][goals[1]] != 2]
                    if node.player == 2:
                        value += max(distanceList) if len(distanceList) else -100
                    else:
                        value -= max(distanceList) if len(distanceList) else -100
        return value



    # Evaluate the board and give it a score
    def evaluate(self, node):

        # get the player that we are working with

        # if the opponent has one give a high negative score
        # if we have won, give a high positive score

        # get the board and all of our player's pieces
        # for every piece
            # get it's distance from the goal camp
            # add it to a sum total

        # divide sum by number of pieces to get the average distance
        # Lower the distance, the higher the evaluation
        # Higher the distance, the lower the evaluation

        # return the evaluation score
        pass

    #
    def alphaBetaMinimax(self, node):
        print("AI MOVE")
        max_node = self.maxValue(node)

        data_board = node.get_board()
        data_board.changeTurn()
        print("Player Turn")
        return max_node
        # return the action to do from the state


    # Get the maximum value from some node
    def maxValue(self, node, alpha, beta):
        # Get the data that we are working with out of the node
        data_board = node.get_board()
        win_detect = data_board.detectWin()

        if (win_detect[0] == True or win_detect[1] == True or node.get_depth() == 0):
            pass
            # return the evaluation function of the node since we have reached a leaf node

        player = node.get_player()
        next_player = 0

        if player == 1:
            player_positions = data_board.get_red_positions()
            next_player = 2
        elif player == 2:
            player_positions = data_board.get_green_positions()
            next_player = 1

        # value = -infinity
        value = float("-inf")

        # for every possible position that our player can move from
        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board.get_board())
            # for evey move that can be made from that position
            for legal_move in legal_moves:
                board_copy = Board()
                board_copy.set_board(data_board.get_board())
                # Create a copy of the table that has that particular move made
                board_copy.place_piece(player, move, legal_move)
                # Create a new node that has that table
                next_node = Node(next_player, board_copy, node.get_depth() - 1)
                # value is equal to the max of the value and the minvalue of the next
                # node and alpha and beta
                child_node = self.minValue(next_node, alpha, beta)
                value = max(value, child_node.get_value())
                return_node = next_node
                # if value is bigger than beta then return beta
                if value > beta:
                    return_node.set_value(beta)
                    return return_node
                # alpha is equal to the max of alpha and the value
                alpha = max(alpha, value)

        # return value
        return_node.set_value(value)
        return return_node


    # Get the minimum value from some node
    def minValue(self, node, alpha, beta):
        # Get the data that we are working with out of the node
        data_board = node.get_board()
        win_detect = data_board.detectWin()

        if (win_detect[0] == True or win_detect[1] == True or node.get_depth() == 0):
            pass
            # return the evaluation function of the node since we have reached a leaf node

        player = node.get_player()
        next_player = 0

        if player == 1:
            player_positions = data_board.get_red_positions()
            next_player = 2
        elif player == 2:
            player_positions = data_board.get_green_positions()
            next_player = 1


        # value = infinity
        value = float("inf")

        # for every piece that a player can move
        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board)
            # for every move that the piece can make
            for legal_move in legal_moves:
                board_copy = Board()
                board_copy.set_board(data_board.get_board())
                # Create a copy of the table that has that particular move made
                board_copy.place_piece(player, move, legal_move)
                # Create a new node that has that table
                next_node = Node(next_player, board_copy, node.get_depth() - 1)

                # value is equal to the minimum of the value and the maxvalue of
                # the child node with the move made and alpha, beta
                child_node = self.maxValue(next_node, alpha, beta)
                value = min(value, child_node.get_value())
                return_node = next_node
                # if value is less than alpha, return the value
                if value < alpha:
                    return_node.set_value(value)
                    return return_node
                # beta is equal to minimum(beta, value)
                beta = min(beta, value)

        # return value
        return_node.set_value(value)
        return return_node
