from graphics import Window, Point
from cell import Cell




def main():
    win = Window(800, 600)
    
    p1 = Point(100,300)
    p2 = Point(300,100)
    
    cell = Cell(p1, p2, win)
    cell.has_right_wall = False
    cell.draw()

    p3 = Point(300, 300)
    p4 = Point(500, 100)

    cell2 = Cell(p3, p4, win)
    cell2.has_left_wall = False
    cell2.draw()

    print(f"2 = {cell.cent.y}")
    cell.draw_move(cell2)
    

    win.wait_for_close()



main()