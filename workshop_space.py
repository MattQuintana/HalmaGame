__author__ = 'Matt Q'

from Node import Node
from Board import Board
from MachinePlayer import MachinePlayer
import signal
import time


def main():
    a_list = [[1,2,[1,2,3],3,4],[2,3,4,54]]
    print(a_list)
    b_list = a_list.copy()
    print(b_list)
    a_list.append(36)
    print(a_list)
    print(b_list)




if __name__ == "__main__":
    main()