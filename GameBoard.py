import tkinter as tk


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

        boardWidth = columns * size
        boardHeight = rows * size

        self.pieceTracker = {}

        tk.Frame.__init__(self, parent)
        self.board = tk.Canvas(self, borderwidth=2, highlightthickness=0,
                                width=boardWidth, height=boardHeight, background="bisque")

        self.board.bind("<Button-1>", self.callback)

        self.board.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.board.bind("<Configure>", self.refresh)

        self.initPieces(1, photo)
        #self.initPieces(2, photo)

    def refresh(self, event):
        # Redraw the board, possibly in response to window being manipulated
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

    def callback(self, event):
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

        print("clicked at tile", coords)
        return coords




if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=True, height=True)
    root.minsize(width=666, height=666)
    photo = tk.PhotoImage(file="red.png")
    photo = photo.zoom(25)
    photo = photo.subsample(100)
    board = GameBoard(root)

    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
