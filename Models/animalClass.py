import turtle
import random

# The Animal class represents a generic animal in the race.
# It includes basic attributes and methods that all animals will share.
class Animal:
    def __init__(self, shape, color, start_pos):
        # Initialize a turtle object to represent the animal on the screen.
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)  # Set the shape of the turtle to represent the animal.
        self.turtle.color(color)  # Set the color of the turtle.
        self.turtle.penup()  # Lift the pen so the turtle does not draw on the screen.
        self.turtle.goto(start_pos)  # Move the turtle to the starting position.
        self.speed = 1  # Initialize the speed of the animal.
        self.last_color = "white"  # Track the last terrain color the animal was on.

    # Method to move the animal forward based on its speed.
    def move(self, track):
        self.turtle.forward(self.speed)
        self.check_area(track)  # Check the terrain under the animal and adjust speed if needed.

    # Method to get the current position of the animal.
    def get_position(self):
        return self.turtle.xcor(), self.turtle.ycor()

    # Method to double the speed of the animal, used when the animal finds food.
    def double_speed(self):
        self.speed = self.speed * 2

    def reduce_speed(self):
        self.speed= self.speed / 2  # Halves speed

    # Method to check the terrain color under the animal and adjust speed accordingly.
    def check_area(self, track):
        current_x = self.turtle.xcor()  # Get the current x-coordinate of the turtle.
        current_color = track.get_color_under_turtle(current_x)  # Get the color of the track under the turtle.
        print(current_color)  # Print the current color for debugging purposes.
        if current_color != self.last_color:  # If the terrain color has changed,
            self.adjust_speed(current_color)  # Adjust the speed based on the new terrain color.
            self.last_color = current_color  # Update the last color to the new terrain color.

    # Placeholder method to adjust speed based on the terrain color.
    def adjust_speed(self, color):
        pass

# The Dog class represents a dog in the race.
# It inherits from the Animal class and can have additional or overridden methods.
class Dog(Animal):
    def __init__(self, start_pos):
        super().__init__("dog.gif", "brown", start_pos)  # Initialize with a dog shape and brown color.

    # Placeholder method to adjust speed based on the terrain color.
    def adjust_speed(self, color):
        if color == "light blue":  # Water terrain.
            self.speed = 1.2
        elif color == "light green":  # Forest terrain.
            self.speed = 1.2
        elif color == "pink": 
            self.speed = 1.2
        else:  # Normal terrain.
            self.speed = 2.5


class Pinkiepie(Animal):
    def __init__(self, start_pos):
        super().__init__("pinkiepie.gif", "blue", start_pos)  # Initialize with a pinkiepieshape and brown color.

    # Placeholder method to adjust speed based on the terrain color.
    def adjust_speed(self, color):
        if color == "light blue":  
            self.speed = 1.2
        elif color == "light green":  
            self.speed = 1.2
        elif color == "pink": 
            self.speed = 2.5
        else:  # Normal terrain.
            self.speed = 1.5


# It inherits from the Animal class and overrides the adjust_speed method.
class TurtleRacer(Animal):
    def __init__(self, start_pos):
        super().__init__("turtle.gif", "light green", start_pos)  # Initialize with a turtle shape and light green color.


    def adjust_speed(self, color):
        if color == "light blue":  
            self.speed = 2.7
        elif color == "light green":  # Forest terrain.
            self.speed = 1.2
        elif color == "pink": 
            self.speed = 1.1
        else:  # Normal terrain.
            self.speed = 1.2

# The Monkey class represents a monkey in the race.
# It inherits from the Animal class and overrides the adjust_speed method.
class Monkey(Animal):
    def __init__(self, start_pos):
        super().__init__("monkey.gif", "orange", start_pos)  # Initialize with a monkey shape and orange color.

    # Method to adjust the speed of the monkey based on the terrain color.
    def adjust_speed(self, color):
        if color == "light green":  # Forest terrain.
            self.speed = 2.5
        elif color == "light blue":  # Water terrain.
            self.speed = 1.2
        elif color == "pink": 
            self.speed = 1.4
        else:  # Normal terrain.
            self.speed = 1.3
