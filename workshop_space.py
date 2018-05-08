__author__ = 'Matt Q'

from Node import Node
from Board import Board
from MachinePlayer import MachinePlayer
import signal
import time


def main():
    mp1 = MachinePlayer()
    myBoard = Board(8)
    myNode = Node(2, myBoard, 2)
    myBoard.initPieces(4)
    myBoard.print_board()
    print(mp1.utility(myNode))

    myBoard.move_piece((0,0), (2, 2))
    myNode = Node(2, myBoard, 2)
    myBoard.print_board()
    print(mp1.utility(myNode))




if __name__ == "__main__":
    main()