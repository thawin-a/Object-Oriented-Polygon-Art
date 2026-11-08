import turtle
class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if pen_size > 0 and sides >= 3 and side_length > 0:
            self._x = x
            self._y = y
            self._sides = sides
            self._side_length = side_length
            self._color = color
            self._pen_size = pen_size
            self._angle = angle
            self._ink = turtle.Turtle()
        else:
            raise ValueError

        
        # TODO: initialize your object's state and its own turtle.Turtle()



    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        # TODO: lift pen; go to starting vertex; set heading/color/pensize;
        #       lower pen; draw sides; lift pen.
        self._ink.penup()
        self._ink.goto(self._x, self._y)
        self._ink.setheading(self._angle)
        self._ink.pencolor(self._color)
        self._ink.pensize(self._pen_size)
        self._ink.pendown()

        self._ink.pendown()
        for i in range(self._sides):
            self._ink.forward(self._side_length)
            self._ink.left(360 / self._sides)
        self._ink.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        # TODO: update this object's position, then clear and redraw.
        self._x = x
        self._y = y
        self._ink.clear()
        self.draw()


