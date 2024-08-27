from graphics import Line, Point

class Cell:
    def __init__(self, point1,  point2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        
        self.cent = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        self._win = win

    def draw(self):
        if self._win is None:
            return
        
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_line = Line(p1, p2)
            self._win.draw_line(left_line, "black")
        
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_line = Line(p1, p2)
            self._win.draw_line(right_line, "black")

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_line = Line(p1, p2)
            self._win.draw_line(top_line, "black")

        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_line = Line(p1, p2)
            self._win.draw_line(bottom_line, "black")

        
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        line = Line(self.cent, to_cell.cent)
        self._win.draw_line(line, color)