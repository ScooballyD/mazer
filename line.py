


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(canvas, fill_color):
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)