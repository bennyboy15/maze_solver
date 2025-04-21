from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, lw,rw,tw,bw, x1,y1,x2,y2, window):
        self.left_wall = lw
        self.right_wall = rw
        self.top_wall = tw
        self.bottom_wall = bw
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.window = window

    def draw(self):
        if self.left_wall:
            self.window.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")

        if self.right_wall:
            self.window.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
        
        if self.top_wall:
            self.window.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")

        if self.bottom_wall:
            self.window.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas:Canvas, fillColour):
        canvas.create_line(
            self.point1.x, 
            self.point1.y,
            self.point2.x,
            self.point2.y, 
            fill=fillColour, 
            width=2
        )
    
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("YAY")
        self.canvas = Canvas(self.root, {"bg":"white"})
        self.canvas.pack()
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line:Line, fillColour):
        line.draw(self.canvas, fillColour)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False


def main():
    win = Window(800,600)
    cell = Cell(False, True, True, False, 10,10,50,50,win)
    cell.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
