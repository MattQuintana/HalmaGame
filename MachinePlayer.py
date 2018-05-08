__author__ = 'Matt Q'

from Node import Node
from Board import Board
import time
import math

class MachinePlayer:

    def __init__(self, timeLimit, alphaBeta):
        self.move_list = []
        self.piece_selected = 0
        self.selected_coords = ()
        self.prevSpots = []
        self.timeLimit = timeLimit
        self.start = 0
        self.end = 0
        self.prunes = 0
        self.boards = 0
        self.alphaBeta = alphaBeta

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

        gameboard = Board(len(board))
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

                        if (board[row][col] == 1 and (row, col) not in gameboard.redCorner):
                            if ((row_jump_offset, col_jump_offset) in gameboard.redCorner):
                                continue

                        if (board[row][col] == 2 and (row, col) not in gameboard.greenCorner):
                            if ((row_jump_offset, col_jump_offset) in gameboard.greenCorner):
                                continue

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
        gameboard = Board(len(board))
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
                    # make sure a piece can't move back to its own camp
                    if (board[row][col] == 1 and (row, col) not in gameboard.redCorner):
                        if ((row + row_offset, col + col_offset) in gameboard.redCorner):
                            continue

                    if (board[row][col] == 2 and (row, col) not in gameboard.greenCorner):
                        if ((row + row_offset, col + col_offset) in gameboard.greenCorner):
                            continue

                    legal_moves.append((row + row_offset, col + col_offset))
                else:
                    blocked_spaces.append((row+row_offset, col + col_offset))


        legal_moves.extend(self.hop_search(row, col, board))
        self.move_list.extend(legal_moves)
        return legal_moves

    def clear_move_list(self):
        self.move_list = []

    def distance(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def utility(self, node):
        board = node.board
        winCheck = board.detectWin()
        data_board = board.get_board()
        value = 0
        red = 0
        green = 0
        for col in range(board.get_width()):
            for row in range(board.get_width()):
                tile = data_board[row][col]

                #green piece
                if tile == 2:
                    distanceList = [self.distance((row,col),goals) for goals in board.redCorner if data_board[goals[0]][goals[1]] != 2]
                    green += max(distanceList) if len(distanceList) else -100

                #red piece
                elif tile == 1:
                    #elif red piece then create distance list for red
                    distanceList = [self.distance((row,col),goals) for goals in board.greenCorner if data_board[goals[0]][goals[1]] != 1]
                    red += max(distanceList) if len(distanceList) else - 100

        if node.player == 1:
            value = red/green
        else:
            value = green/red

        if winCheck[0]:
            value = float("inf")
        elif winCheck[1]:
            value = float("inf")

        return value

    def alphaBetaMinimax(self, node):
        self.start = time.time()
        max_node, best_move = self.maxValue(node, float("-inf"), float("inf"))
        data_board = node.get_board()
        data_board.move_piece(best_move[0], best_move[1])
        print("Took", self.end - self.start, "seconds to choose a move.")
        print("Pruned", self.prunes, "branches.")
        print("Generated", self.boards, "boards.")
        self.prunes = 0
        self.boards = 0
        data_board.changeTurn()
        return max_node
        # return the action to do from the state


    # Get the maximum value from some node
    def maxValue(self, node, alpha, beta):
        self.end = time.time()
        # Get the data that we are working with out of the node
        board = node.get_board()
        win_detect = board.detectWin()
        best_move = None
        if (win_detect[0] == True or win_detect[1] == True or node.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(node)
            node.set_value(evaluation)
            return node, best_move
            # return the evaluation function of the node since we have reached a leaf node

        player = node.get_player()
        next_player = player

        if player == 1:
            player_positions = board.get_green_positions()
        elif player == 2:
            player_positions = board.get_red_positions()

        # value = -infinity
        value = float("-inf")
        data_board = board.get_board()
        # for every possible position that our player can move from
        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board)
            if len(legal_moves) == 0:
                continue

            # for evey move that can be made from that position
            for legal_move in legal_moves:
                self.end = time.time()
                if(self.end-self.start > self.timeLimit):
                    return node, best_move
                self.boards += 1
                board_copy = Board(node.get_board().get_height())
                board_copy.set_board(data_board)
                # Create a copy of the table that has that particular move made
                board_copy.move_piece(move, legal_move)
                # Create a new node that has that table
                next_node = Node(player, board_copy, node.get_depth() - 1)
                next_node.move = (move, legal_move)
                # value is equal to the max of the value and the minvalue of the next
                # node and alpha and beta
                child_node, _ = self.minValue(next_node, alpha, beta)
                board_copy.move_piece(legal_move, move)
                if (value < child_node.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = max(value, child_node.get_value())

                return_node = next_node
                # if value is bigger than beta then return beta
                if value > beta and self.alphaBeta:
                    self.prunes += 1
                    return_node.set_value(beta)
                    return return_node, None

                # alpha is equal to the max of alpha and the value
                alpha = max(alpha, value)

        # return value
        return_node.set_value(value)
        return return_node, best_move


    # Get the minimum value from some node
    def minValue(self, node, alpha, beta):
        self.end = time.time()
        # Get the data that we are working with out of the node
        board = node.get_board()
        win_detect = board.detectWin()
        best_move = None
        if (win_detect[0] == True or win_detect[1] == True or node.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(node)
            node.set_value(evaluation)
            return node, best_move
            # return the evaluation function of the node since we have reached a leaf node

        player = node.get_player()

        if player == 1:
            player_positions = board.get_green_positions()
        elif player == 2:
            player_positions = board.get_red_positions()


        # value = infinity
        value = float("inf")

        data_board = board.get_board()

        # for every piece that a player can move
        for move in player_positions:
            legal_moves = self.generate_legal_moves(move[0], move[1], data_board)
            if len(legal_moves) == 0:
                continue
            # for every move that the piece can make
            for legal_move in legal_moves:
                self.end = time.time()
                if (self.end - self.start > self.timeLimit):
                    return node, best_move
                self.boards += 1
                board_copy = Board(node.get_board().get_height())
                board_copy.set_board(data_board)
                # Create a copy of the table that has that particular move made
                board_copy.move_piece(move, legal_move)
                # Create a new node that has that table
                next_node = Node(player, board_copy, node.get_depth() - 1)
                next_node.move = (move, legal_move)


                # value is equal to the minimum of the value and the maxvalue of
                # the child node with the move made and alpha, beta
                child_node, _ = self.maxValue(next_node, alpha, beta)
                board_copy.move_piece(legal_move, move)
                if (value > child_node.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = min(value, child_node.get_value())
                return_node = next_node
                # if value is less than alpha, return the value
                if value < alpha and self.alphaBeta:
                    self.prunes += 1
                    return_node.set_value(value)
                    return return_node, None
                # beta is equal to minimum(beta, value)
                beta = min(beta, value)

        # return value
        return_node.set_value(value)
        return return_node, best_move
