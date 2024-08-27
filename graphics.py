from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazer")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, point1,  point2, win, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        self._win = win

    def draw(self):
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_line = Line(p1, p2)
            self._win.draw_line(left_line, "black")
            print("draw left")
        
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_line = Line(p1, p2)
            self._win.draw_line(right_line, "black")
            print("draw right")

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_line = Line(p1, p2)
            self._win.draw_line(top_line, "black")
            print("draw top")

        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_line = Line(p1, p2)
            self._win.draw_line(bottom_line, "black")
            print("draw bot")