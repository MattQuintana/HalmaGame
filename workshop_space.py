__author__ = 'Matt Q'

from Node import Node
from Board import Board
import signal
import time


def main():
    board = Board(8)

    board.initRedPieces(4)
    board.initGreenPieces(4)
    board.print_board()


if __name__ == "__main__":
    main()