#CreateBoard
import random
import tkinter
from tkinter import *
from enum import Enum
from Cell import Cell
from copy import deepcopy
from Legal_move import LegalMove
from Utils import *

HEIGHT = 8
WIDTH = 8
COLUMN_WIDTH = 500
COLUMN_HEIGHT = 500
ROW_WIDTH = 500
ROW_HEIGHT = 500


class Player(Enum):
    PLAYER_1 = "white"  # white player
    PLAYER_2 = "black"  # black player
    def __eq__(self, other):
        if self is not None and other is not None:
            return self.name == other.name and self.value == other.value
        return False

class CreateBoard:
    def __init__(self):
        row = [None] * WIDTH
        self.board = []
        # center values
        for i in range(WIDTH):
            self.board.append(deepcopy(row))
            for j in range(HEIGHT):
                new_cell = Cell(i, j)
                if (i == 3 and j == 4) or (i == 4 and j == 3):
                    new_cell.set_player(Player.PLAYER_1)
                elif (i == 3 and j == 3) or (i == 4 and j == 4):
                    new_cell.set_player(Player.PLAYER_2)
                self.board[i][j] = new_cell
        # self.root = Tk()
        # self.gui = Canvas(self.root, width=500, height=600, background="#222", highlightthickness=0)
        # self.gui.pack()

        self.player = self.whoGoesFirst()
        self.must_pass = False
        self.won = False
        # self.change = False
        self.old_arr = self.board

        self.screen_update(True)

    def whoGoesFirst(self):
     # Randomly choose the player who goes first.
         if random.randint(0, 1) == 0:
             return Player.PLAYER_1
         else:
             return Player.PLAYER_2

    def screen_update(self, first_time= False):
        return None
        if first_time:
            for i in range(WIDTH - 1):
                lineShift = 50 + 50 * (i + 1)

                # Horizontal line
                self.gui.create_line(50, lineShift, 450, lineShift, fill="#111")

                # Vertical line
                self.gui.create_line(lineShift, 50, lineShift, 450, fill="#111")
        self.gui.delete("highlight")
        self.gui.delete("tile")
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.old_arr[x][y].player == Player.PLAYER_1:
                    self.gui.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x,
                                       96 + 50 * y,
                                       tags="tile {0}-{1}".format(x, y),
                                       fill="#aaa", outline="#aaa")
                    self.gui.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x,
                                       94 + 50 * y,
                                       tags="tile {0}-{1}".format(x, y),
                                       fill="#fff", outline="#fff")

                elif self.old_arr[x][y].player == Player.PLAYER_2:
                    self.gui.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x,
                                       96 + 50 * y,
                                       tags="tile {0}-{1}".format(x, y),
                                       fill="#000", outline="#000")
                    self.gui.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x,
                                       94 + 50 * y,
                                       tags="tile {0}-{1}".format(x, y),
                                       fill="#111", outline="#111")

        self.gui.update()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.old_arr[x][y] != self.board[x][y] and self.board[x][y].player == Player.PLAYER_1:
                    self.gui.delete("{0}-{1}".format(x, y))
                    # 42 is width of tile so 21 is half of that
                    # Shrinking
                    for i in range(21):
                        self.gui.create_oval(54 + i + 50 * x, 54 + i + 50 * y,
                                           96 - i + 50 * x, 96 - i + 50 * y,
                                           tags="tile animated", fill="#000",
                                           outline="#000")
                        self.gui.create_oval(54 + i + 50 * x, 52 + i + 50 * y,
                                           96 - i + 50 * x, 94 - i + 50 * y,
                                           tags="tile animated", fill="#111",
                                           outline="#111")
                        self.gui.update()
                        self.gui.delete("animated")
                    # Growing
                    for i in reversed(range(21)):
                        self.gui.create_oval(54 + i + 50 * x, 54 + i + 50 * y,
                                           96 - i + 50 * x, 96 - i + 50 * y,
                                           tags="tile animated", fill="#aaa",
                                           outline="#aaa")
                        self.gui.create_oval(54 + i + 50 * x, 52 + i + 50 * y,
                                           96 - i + 50 * x, 94 - i + 50 * y,
                                           tags="tile animated", fill="#fff",
                                           outline="#fff")
                        self.gui.update()
                        self.gui.delete("animated")
                    self.gui.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x,
                                       96 + 50 * y, tags="tile", fill="#aaa",
                                       outline="#aaa")
                    self.gui.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x,
                                       94 + 50 * y, tags="tile", fill="#fff",
                                       outline="#fff")
                    self.gui.update()

                elif self.old_arr[x][y] != self.board[x][y] and self.board[x][y].player == Player.PLAYER_2:

                    self.gui.delete("{0}-{1}".format(x, y))
                    # 42 is width of tile so 21 is half of that
                    # Shrinking
                    for i in range(21):
                        self.gui.create_oval(54 + i + 50 * x, 54 + i + 50 * y,
                                           96 - i + 50 * x, 96 - i + 50 * y,
                                           tags="tile animated", fill="#aaa",
                                           outline="#aaa")
                        self.gui.create_oval(54 + i + 50 * x, 52 + i + 50 * y,
                                           96 - i + 50 * x, 94 - i + 50 * y,
                                           tags="tile animated", fill="#fff",
                                           outline="#fff")
                        self.gui.update()
                        self.gui.delete("animated")
                    # Growing
                    for i in reversed(range(21)):
                        self.gui.create_oval(54 + i + 50 * x, 54 + i + 50 * y,
                                           96 - i + 50 * x, 96 - i + 50 * y,
                                           tags="tile animated", fill="#000",
                                           outline="#000")
                        self.gui.create_oval(54 + i + 50 * x, 52 + i + 50 * y,
                                           96 - i + 50 * x, 94 - i + 50 * y,
                                           tags="tile animated", fill="#111",
                                           outline="#111")
                        # if i % 3 == 0:
                        #     sleep(0.01)
                        self.gui.update()
                        self.gui.delete("animated")

                    self.gui.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x,
                                       96 + 50 * y, tags="tile", fill="#000",
                                       outline="#000")
                    self.gui.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x,
                                       94 + 50 * y, tags="tile", fill="#111",
                                       outline="#111")
                    self.gui.update()

        # Drawing of highlight circles
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.player == Player.PLAYER_1:
                    if CreateBoard.static_validation(self.board, self.player, x, y):
                        self.gui.create_oval(68 + 50 * x, 68 + 50 * y,
                                           32 + 50 * (x + 1),
                                           32 + 50 * (y + 1), tags="highlight",
                                           fill="#008000", outline="#008000")
                else:
                    if CreateBoard.static_validation(self.board, self.player, x, y):
                        self.gui.create_oval(68 + 50 * x, 68 + 50 * y,
                                           32 + 50 * (x + 1),
                                           32 + 50 * (y + 1),
                                           tags="highlight",
                                           fill="#FFFF00",
                                           outline="#008000")

        if not self.won:
            # Draw the scoreboard and update the screen
            self.drawScoreBoard()
            self.gui.update()
        else:
            self.gui.create_text(250, 550, anchor="c", font=("Consolas", 15),
                               text="The game is done!")
        # self.change = False


    @staticmethod
    def static_legal_moves(board, player):
        legal_moves = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if CreateBoard.static_validation(board, player, x,y):
                    next_board = CreateBoard.static_move_helper(board, x, y)
                    new_legal_move = LegalMove(next_board, x, y)
                    legal_moves.append(new_legal_move)
        return legal_moves

    @staticmethod
    def static_validation(board, player, x, y):
        # Sets player colour
        color = player
        # If there's already a piece there, it's an invalid move
        if board[x][y].player != None:
            return False

        else:
            # Generating the list of neighbours
            neighbour = False
            neighbours = []
            for i in range(max(0, x - 1), min(x + 2, 8)):
                for j in range(max(0, y - 1), min(y + 2, 8)):
                    if board[i][j].player != None:
                        neighbour = True
                        neighbours.append([i, j])
            # If there's no neighbours, it's an invalid move
            if not neighbour:
                return False
            else:
                # Iterating through neighbours to determine if at least one line is formed
                valid = False
                for neighbour in neighbours:

                    neighX = neighbour[0]
                    neighY = neighbour[1]

                    # If the neighbour color is equal to your colour, it doesn't form a line
                    # Go onto the next neighbour
                    if board[neighX][neighY].player == color:
                        continue
                    else:
                        # Determine the direction of the line
                        deltaX = neighX - x
                        deltaY = neighY - y
                        tempX = neighX
                        tempY = neighY

                        while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                            # If an empty space, no line is formed
                            if board[tempX][tempY].player == None:
                                break
                            # If it reaches a piece of the player's color, it forms a line
                            if board[tempX][tempY].player == color:
                                valid = True
                                break
                            # Move the index according to the direction of the line
                            tempX += deltaX
                            tempY += deltaY
                return valid

    @staticmethod
    def static_move_helper(board, x, y):
        #Must copy the passedArray so we don't alter the original
        array = deepcopy(board)
        color = board[x][y].player
        array[x][y].player = color

        #Determining the neighbours to the square
        neighbours = []
        for i in range(max(0,x-1),min(x+2,8)):
            for j in range(max(0,y-1),min(y+2,8)):
                if array[i][j].player!=None:
                    neighbours.append([i,j])

        #Which tiles to convert
        convert = []

        #For all the generated neighbours, determine if they form a line
        #If a line is formed, we will add it to the convert array
        for neighbour in neighbours:
            neighX = neighbour[0]
            neighY = neighbour[1]
            #Check if the neighbour is of a different colour - it must be to form a line
            if array[neighX][neighY].player != color:
                #The path of each individual line
                path = []

                #Determining direction to move
                deltaX = neighX-x
                deltaY = neighY-y

                tempX = neighX
                tempY = neighY

                #While we are in the bounds of the board
                while 0<=tempX<=7 and 0<=tempY<=7:
                    path.append([tempX,tempY])
                    value = array[tempX][tempY].player
                    #If we reach a blank tile, we're done and there's no line
                    if value == None:
                        break
                    #If we reach a tile of the player's colour, a line is formed
                    if value == color:
                        #Append all of our path nodes to the convert array
                        for node in path:
                            convert.append(node)
                        break
                    #Move the tile
                    tempX+=deltaX
                    tempY+=deltaY

        #Convert all the appropriate tiles
        for node in convert:
            array[node[0]][node[1]].player=color
        return array

    def drawScoreBoard(self):
        return None
        global moves
        #Deleting prior score elements
        self.gui.delete("score")

        #Scoring based on number of tiles
        player1_score = 0
        player2_score = 0
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.board[x][y].player ==Player.PLAYER_1:
                    player1_score+=1
                elif self.board[x][y].player == Player.PLAYER_2:
                    player2_score+=1

        if self.player == Player.PLAYER_1:
            player_colour = "green"
            player2_color = "gray"
        else:
            player_colour = "gray"
            player2_color = "green"

        self.gui.create_oval(5,540,25,560,fill=player_colour,outline=player_colour)
        self.gui.create_oval(380,540,400,560,fill=player2_color,outline=player2_color)

        #Pushing text to screen
        self.gui.create_text(30,550,anchor="w", tags="score",font=("Consolas", 50),fill="white",text=player1_score)
        self.gui.create_text(400,550,anchor="w", tags="score",font=("Consolas", 50),fill="black",text=player2_score)

        # TODO: delete!
        moves = player1_score+player2_score

    def move(self,x,y):
        #Move and update screen
        # self.change = True
        self.old_arr = self.board
        self.old_arr[x][y].player = self.player
        self.board = self.move_helper(x,y)

        #Switch Player
        if self.player == Player.PLAYER_1:
            self.player = Player.PLAYER_2
        else:
            self.player = Player.PLAYER_1
        self.screen_update()

        #Check if ai must pass
        self.check_pass()

    def check_pass(self):
        mustPass = True
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if CreateBoard.static_validation(self.board, self.player, x,y):
                    mustPass=False
        if mustPass:
            if self.player == Player.PLAYER_1:
                self.player = Player.PLAYER_2
            else:
                self.player = Player.PLAYER_1
            if self.must_pass==True:
                self.won = True
            else:
                self.must_pass = True
            self.screen_update()
        else:
            self.must_pass = False



    def move_helper(self, x, y):
            #Must copy the passedArray so we don't alter the original
            array = deepcopy(self.board)
            color = self.board[x][y].player
            array[x][y].player = color

            #Determining the neighbours to the square
            neighbours = []
            for i in range(max(0,x-1),min(x+2,8)):
                for j in range(max(0,y-1),min(y+2,8)):
                    if array[i][j].player!=None:
                        neighbours.append([i,j])

            #Which tiles to convert
            convert = []

            #For all the generated neighbours, determine if they form a line
            #If a line is formed, we will add it to the convert array
            for neighbour in neighbours:
                neighX = neighbour[0]
                neighY = neighbour[1]
                #Check if the neighbour is of a different colour - it must be to form a line
                if array[neighX][neighY].player != color:
                    #The path of each individual line
                    path = []

                    #Determining direction to move
                    deltaX = neighX-x
                    deltaY = neighY-y

                    tempX = neighX
                    tempY = neighY

                    #While we are in the bounds of the board
                    while 0<=tempX<=7 and 0<=tempY<=7:
                        path.append([tempX,tempY])
                        value = array[tempX][tempY].player
                        #If we reach a blank tile, we're done and there's no line
                        if value == None:
                            break
                        #If we reach a tile of the player's colour, a line is formed
                        if value == color:
                            #Append all of our path nodes to the convert array
                            for node in path:
                                convert.append(node)
                            break
                        #Move the tile
                        tempX+=deltaX
                        tempY+=deltaY

            #Convert all the appropriate tiles
            for node in convert:
                array[node[0]][node[1]].player=color
            return array
