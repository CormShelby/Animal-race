#Import all the files, be careful here there will be a lot of errors
from Models.animalClass import Monkey
from Models.animalClass import Dog
from Models.animalClass import TurtleRacer
from Models.animalClass import Pinkiepie
from Models.foodClass import Lettuce
from Models.foodClass import Banana
from Models.foodClass import Bone
from Models.foodClass import cake
from Models.artefactsClass import fence
from Models.raceTrackClass import RaceTrack
import random


class AnimalRaceGame:
    def __init__(self):
        self.track = RaceTrack(1000, 400)
        self.finish_line = 450

    def create_animals(self):
        monkey = Monkey((-450, 150))
        dog = Dog((-450, 50))
        turtle_racer = TurtleRacer((-450, -45))
        pinkiepie = Pinkiepie((-450, -150))
        return monkey, dog, turtle_racer, pinkiepie

    def create_food_items(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        food_classes = [Bone, Lettuce, Banana, cake]
        foods = [random.choice(food_classes)((random.randint(starting_line, finish_line), random.choice([150, 50, -45, -150]))) for _ in range(num_items)]
        return foods
    
    def create_Obstacle_items(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        Obstacles = [fence((random.randint(starting_line, finish_line), random.choice([ 150, 50, -45, -150]))) for _ in range(num_items)]
        return Obstacles

    