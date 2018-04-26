__author__ = 'Matt Q'

class Node:

    def __init__(self, board, node_depth):
        self.board = board
        self.type = ""
        self.player = 0
        self.to_explore = True
        self.node_value = 0
        self.node_depth = node_depth

        self.children = []


    def get_children(self):
        return self.children

    def get_depth(self):
        return self.node_depth

    def get_type(self):
        return self.type

    def get_player(self):
        return self.player

    def can_explore(self):
        return self.to_explore

    def set_explore(self, explore_truth):
        self.to_explore = explore_truth

    def set_value(self, value):
        self.node_value = value

    def get_value(self):
        return self.node_value

    def get_board(self):
        return self.board
