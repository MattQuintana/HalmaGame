__author__ = 'Matt Q'

from Node import Node
from Board import Board
from MachinePlayer import MachinePlayer
import signal
import time


def main():
    board = Board(8)

    mp = MachinePlayer()

    board.initRedPieces(4)
    board.initGreenPieces(4)
    board.print_board()

    data_board = board.get_board()
    print("Possible moves:", mp.generate_legal_moves(6,6,data_board))


if __name__ == "__main__":
    main()