import tkinter as tk
from Board import Board
from MachinePlayer import MachinePlayer

class GameBoard(tk.Frame):
    def __init__(self, parent, photo1=None, photo2=None, rows=8, columns=8, size=32, color1="white", color2="black"):
        self.rows = rows
        self.columns = columns
        self.sqrSize = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.photo1 = photo1
        self.photo2 = photo2
        self.totalPieces = 0

        self.data_board = Board(8)
        self.data_board.initRedPieces(4)
        self.data_board.initGreenPieces(4)

        boardWidth = columns * size
        boardHeight = rows * size

        self.pieceTracker = {}

        tk.Frame.__init__(self, parent)
        self.board = tk.Canvas(self, borderwidth=2, highlightthickness=0,
                                width=boardWidth, height=boardHeight, background="bisque")


        self.board.bind("<Button-1>", self.playerClick)

        self.board.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.board.bind("<Configure>", self.refresh)

        #self.initPieces(1, photo)
        #self.initPieces(2, photo)

        self.draw_pieces()

    def refresh(self, event):
        # Redraw the board, possibly in response to window being manipulated
        self.board.create_text(250, 250, fill = "red", text="Red Wins")
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.sqrSize = min(xsize, ysize)
        self.board.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.sqrSize)
                y1 = (row * self.sqrSize)
                x2 = x1 + self.sqrSize
                y2 = y1 + self.sqrSize
                self.board.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placePiece(name, self.pieces[name][0], self.pieces[name][1])
        self.board.tag_raise("piece")
        self.board.tag_lower("square")

    def manualRefresh(self):
        self.board.create_text(250, 250, fill="red", text="Red Wins")
        self.board.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.sqrSize)
                y1 = (row * self.sqrSize)
                x2 = x1 + self.sqrSize
                y2 = y1 + self.sqrSize
                self.board.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placePiece(name, self.pieces[name][0], self.pieces[name][1])
        self.board.tag_raise("piece")
        self.board.tag_lower("square")

    def createPiece(self, name, image, row, col):
        self.board.create_image(0, 0, tags=(name, 'piece'), image=image, anchor='center')
        self.placePiece(name, row, col)

    def placePiece(self, name, row, col):
        self.pieces[name] = (row, col)
        x0 = (col * self.sqrSize) + int(self.sqrSize / 2)
        y0 = (row * self.sqrSize) + int(self.sqrSize / 2)
        self.board.coords(name, x0, y0)

    def initPieces(self, player, photo):
        if player == 1:
            self.createPiece(self.totalPieces, photo, 100, 100)
            self.totalPieces += 1
            for i in range(int(self.rows/2)):
                for j in range(int(self.columns/2)-i):

                    self.createPiece(self.totalPieces, photo, i, j)
                    self.totalPieces += 1
        elif player == 2:
            for i in range(int(self.rows/2)):
                for j in range(int(self.columns/2)):
                    self.createPiece(self.totalPieces, photo,self.rows-1-i, self.rows-1-(j-i))
                    self.totalPieces += 1

    def detectWin(self):
        greenWin = False
        redWin = False

        for coord in self.data_board.greenCorner:
            if self.data_board.get_piece_at(coord[0], coord[1]) == False:
                redWin = False
                break
            elif self.data_board.get_piece_at(coord[0], coord[1]) == 1:
                redWin = True

        for coord in self.data_board.redCorner:
            if self.data_board.get_piece_at(coord[0], coord[1]) == False:
                greenWin = False
                break
            elif self.data_board.get_piece_at(coord[0], coord[1]) == 2:
                greenWin = True

        rtn = (redWin, greenWin)

        return rtn

    def playerClick(self, event):
        row = event.y
        col = event.x
        counter1 = 0
        counter2 = 0
        while row >= 0:
            row -= self.sqrSize
            counter1 += 1

        while col >= 0:
            col -= self.sqrSize
            counter2 += 1

        coords = (counter1 - 1, counter2 - 1)

        if self.data_board.get_piece_at(coords[0], coords[1]):
            # Choose a first piece to move
            mp1.piece_selected = self.data_board.get_piece_at(coords[0], coords[1])
            mp1.selected_coords = (coords[0], coords[1])
            if (mp1.move_list == []):
                print("New piece selected")
                mp1.generate_legal_moves(coords[0], coords[1], self.data_board.get_board())
                self.data_board.print_board()
                # Do some coloring of the board to show valid positions
            elif (mp1.move_list != []):
                print("NEW PIECE SELECTED")
                mp1.clear_move_list()
                mp1.generate_legal_moves(coords[0], coords[1], self.data_board.get_board())
                # Do some coloring of the board

        else:

            coordinate_tuple = (coords[0], coords[1])
            if coordinate_tuple in mp1.move_list:
                print("Moved piece")
                self.data_board.remove_piece_at(mp1.selected_coords[0], mp1.selected_coords[1])
                self.data_board.place_piece(mp1.piece_selected, coords[0], coords[1])
                self.board.delete("all")
                self.manualRefresh()
                self.draw_pieces()
                self.data_board.print_board()
                win = self.detectWin()
                if win[0] is True and win[1] is True:
                    print("HOW DID YOU GET A TIE?")
                elif win[0] is True:
                    print("RED IS THE WINNER!")
                elif win[1] is True:
                    print("GREEN IS THE WINNER!")


        print("clicked at tile", coords)
        return coords

    def draw_pieces(self):
        red_count = 0
        green_count = 0
        for i in range(0, self.data_board.get_height()):
            for j in range(0, self.data_board.get_width()):
                if (self.data_board.get_piece_at(i, j) == 1):
                    self.createPiece("p1_" + str(red_count), photo, i, j)
                    red_count += 1
                elif (self.data_board.get_piece_at(i, j) == 2):
                    #self.createPiece("p2_" + str(green_count), p2, i, j)
                    green_count += 1



if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=True, height=True)
    root.minsize(width=666, height=666)
    photo = tk.PhotoImage(file="red.png")
    photo = photo.zoom(25)
    photo = photo.subsample(100)

    p2 = tk.PhotoImage(file="green.png")
    p2 = p2.zoom(25)
    p2 = p2.subsample(100)

    mp1 = MachinePlayer()


    board = GameBoard(root)

    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
