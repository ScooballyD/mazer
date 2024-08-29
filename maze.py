import time
import random
from cell import Cell
from graphics import Point, Window

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        if seed != None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        x = self._x1
        y = self._y1

        for i in range(self.num_cols):
            p1 = Point(x,y)
            p2 = Point(x + self.cell_size_x, y - self.cell_size_y)
            self._cells.append([Cell(p1, p2, self._win)])
            y = y + self.cell_size_y

            for j in range(self.num_rows - 1):
                p3 = Point(x, y)
                p4 = Point(x + self.cell_size_x, y - self.cell_size_y)
                self._cells[i].append(Cell(p3, p4, self._win))
                y = y + self.cell_size_y

            x = x + self.cell_size_x
            y = self._y1
        
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.has_bottom_wall = False

        for col in self._cells:
            for cell in col:
                cell.draw()
                if self._win:
                    self._animate()
        
        self._break_walls_r(0, 0)
        self._reset_cells_visisted()

    def _animate(self):
        self._win.redraw()
        time.sleep(.003)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        #DELETE
        if i > 0:
            left = self._cells[i-1][j]
        if j > 0:
            top = self._cells[i][j-1]
        if i < self.num_cols-1:
            right = self._cells[i+1][j]
        if j < self.num_rows-1:
            bottom = self._cells[i][j+1]

        while True:
            options = []

            if i > 0 and self._cells[i-1][j].visited == False:
                options.append(["left", i-1, j])
            if j > 0 and self._cells[i][j-1].visited == False:
                options.append(["top", i, j-1])
            if i < self.num_cols-1 and self._cells[i+1][j].visited == False:
                options.append(["right", i+1, j])
            if j < self.num_rows-1 and self._cells[i][j+1].visited == False:
                options.append(["bottom", i, j+1])
            
            if len(options) == 0:
                self._cells[i][j].draw()
                return

            next = random.choice(options)

            if next[0] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next[0] == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if next[0] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next[0] == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            self._cells[i][j].draw()
            if self._win:
                self._animate()
            self._break_walls_r(next[1], next[2])
    
    def _reset_cells_visisted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        if self._win:
            self._animate()

        self._cells[i][j].visited = True
        if i is self.num_cols - 1 and j is self.num_rows - 1:
            return True
        
        options = []
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            left = [i-1, j]
            options.append(left)
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            top = [i, j-1]
            options.append(top)
        if i < self.num_cols-1 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            right = [i+1, j]
            options.append(right)
        if j < self.num_rows-1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            bottom = [i, j+1]
            options.append(bottom)

        for opt in options:
            self._cells[i][j].draw_move(self._cells[opt[0]][opt[1]])
            if self._solve_r(opt[0], opt[1]):
                return True
            self._cells[i][j].draw_move(self._cells[opt[0]][opt[1]], True)
        return False