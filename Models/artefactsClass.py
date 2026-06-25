import turtle
import random
class Obstacle:
    def __init__(self, color, shape, position):
        self.fence = turtle.Turtle()
        self.fence.shape(shape)
        self.fence.color(color)
        self.fence.penup()
        self.fence.goto(position)
        self.position = position

    def get_position(self):
        return self.position

    def hide(self):
        self.fence.hideturtle()

class fence(Obstacle):
    def __init__(self, position):
        super().__init__("brown", "fence.gif", position)

