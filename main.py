from graphics import Window, Point
from cell import Cell
from maze import Maze




def main():
    h = 800
    w = 600
    margin = 10
    mh = h - margin
    mw = w - margin

    win = Window(h, w)

    # max area of 3025
    # or 55 rows and 55 cols
    row = 40
    col = 40
    
    test = Maze(margin / 2, margin / 2 + mw / row, row, col, mh / col, mw / row, win)
    test.solve()
    

    win.wait_for_close()



main()