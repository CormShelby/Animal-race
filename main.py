from Controller.animalRaceGame import *
import turtle

def start_game():
    turtle.clearscreen()
    initialize()


def show_menu():
    # Configuration de l'écran
    screen = turtle.Screen()
    screen.title("Maurice le sage")
    screen.setup(width=550, height=400)
    screen.bgpic("homepage.gif")


    # Bouton Start
    start_button = turtle.Turtle()
    start_button.shape("square")
    start_button.color("green")
    start_button.shapesize(stretch_wid=2, stretch_len=5)
    start_button.penup()
    start_button.goto(0, -100)

    # Texte sur le bouton
    button_text = turtle.Turtle()
    button_text.penup()
    button_text.hideturtle()
    button_text.color("white")
    button_text.goto(0, -115)
    button_text.write("Mieux que GTA6", align="center", font=("Arial", 16, "bold"))

    # Fonction pour détecter le clic sur le bouton
    def on_start_click(x, y):
        if -50 <= x <= 50 and -130 <= y <= -90:  # Coordonnées du bouton
            start_game()

    # Enregistrement du clic
    screen.onclick(on_start_click)

    # Boucle principale du menu
    screen.mainloop()

def initialize():
    # Couleurs vives pour les éléments du jeu
    turtle.register_shape("dog.gif")
    turtle.register_shape("monkey.gif")
    turtle.register_shape("banana.gif")
    turtle.register_shape("bone.gif")
    turtle.register_shape("fence.gif")
    turtle.register_shape("lettuce.gif")
    turtle.register_shape("pinkiepie.gif")
    turtle.register_shape("cake.gif")
    turtle.register_shape("turtle.gif")


    game = AnimalRaceGame()
    game.track.create_random_areas(5, ["light blue", "light green", "pink"])
    monkey, dog, turtle_racer, pinkiepie = game.create_animals()
    foods = game.create_food_items(7)
    Obstacles = game.create_Obstacle_items(2)
    
    game.track.draw_lanes()

    while monkey.get_position()[0] < game.finish_line and dog.get_position()[0] < game.finish_line and turtle_racer.get_position()[0] < game.finish_line and pinkiepie.get_position()[0] < game.finish_line:
        monkey.move(game.track)
        dog.move(game.track)
        turtle_racer.move(game.track)
        pinkiepie.move(game.track)
        print(monkey.speed,"   ",dog.speed,"   ",turtle_racer.speed,"   ",pinkiepie.speed)
        print(monkey.last_color,"   ",dog.last_color,"   ",turtle_racer.last_color,"   ",pinkiepie.last_color)

        for food in foods:
            if isinstance(food, Banana) and abs(monkey.get_position()[0] - food.get_position()[0]) < 10 and abs(monkey.get_position()[1] - food.get_position()[1]) < 10:
                monkey.double_speed()
                food.hide()
                foods.remove(food)
                break
            if isinstance(food, Bone) and abs(dog.get_position()[0] - food.get_position()[0]) < 10 and abs(dog.get_position()[1] - food.get_position()[1]) < 10:
                dog.double_speed()
                food.hide()
                foods.remove(food)
                break
            if isinstance(food, Lettuce) and abs(turtle_racer.get_position()[0] - food.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - food.get_position()[1]) < 10:
                turtle_racer.double_speed()
                food.hide()
                foods.remove(food)
                break
            if isinstance(food, cake) and abs(pinkiepie.get_position()[0] - food.get_position()[0]) < 10 and abs(pinkiepie.get_position()[1] - food.get_position()[1]) < 10:
                pinkiepie.double_speed()
                food.hide()
                foods.remove(food)
                break
    
        for Obstacle in Obstacles:
            if isinstance(Obstacle, fence) and abs(pinkiepie.get_position()[0] - Obstacle.get_position()[0]) < 10 and abs(pinkiepie.get_position()[1] - Obstacle.get_position()[1]) < 10:
                pinkiepie.reduce_speed()
                Obstacle.hide()
                Obstacles.remove(Obstacle)
                break
            if isinstance(Obstacle, fence) and abs(monkey.get_position()[0] - Obstacle.get_position()[0]) < 10 and abs(monkey.get_position()[1] - Obstacle.get_position()[1]) < 10:
                monkey.reduce_speed()
                Obstacle.hide()
                Obstacles.remove(Obstacle)
                break
            if isinstance(Obstacle, fence) and abs(dog.get_position()[0] - Obstacle.get_position()[0]) < 10 and abs(dog.get_position()[1] - Obstacle.get_position()[1]) < 10:
                dog.reduce_speed()
                Obstacle.hide()
                Obstacles.remove(Obstacle)
                break
            if isinstance(Obstacle, fence) and abs(turtle_racer.get_position()[0] - Obstacle.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - Obstacle.get_position()[1]) < 10:
                turtle_racer.reduce_speed()
                Obstacle.hide()
                Obstacles.remove(Obstacle)
                break

    winners = []
    if monkey.get_position()[0] >= game.finish_line:
        winners.append("Monkey")
    if dog.get_position()[0] >= game.finish_line:
        winners.append("Dog")
    if turtle_racer.get_position()[0] >= game.finish_line:
        winners.append("Turtle")
    if pinkiepie.get_position()[0] >= game.finish_line:
        winners.append("pinkiepie")

    if len(winners) > 1:
        display_text = "It's a tie between: " + ", ".join(winners)
    else:
        display_text = f"The winner is: {winners[0]}"

   
    winner_turtle = turtle.Turtle()
    winner_turtle.penup()
    winner_turtle.hideturtle()
    winner_turtle.goto(0, 50)
    winner_turtle.color("red")
    winner_turtle.write(display_text, align="center", font=("Arial", 24, "bold"))

    quit_button = turtle.Turtle()
    quit_button.shape("square")
    quit_button.color("red")
    quit_button.shapesize(stretch_wid=1.5, stretch_len=5)
    quit_button.penup()
    quit_button.goto(0, -50)

    # Textesur le bouton
    quit_text = turtle.Turtle()
    quit_text.penup()
    quit_text.hideturtle()
    quit_text.color("white")
    quit_text.goto(0, -60)
    quit_text.write("QUIT", align="center", font=("Arial", 16, "bold"))
    
#fonctionpourdeterminerleclick
    def on_quit_click(x, y):
        if -50 <= x <= 50 and -65 <= y <= -35:  # Coordonnées du bouton
            quit_game()

      # Bouton Restart
    restart_button = turtle.Turtle()
    restart_button.shape("square")
    restart_button.color("blue")
    restart_button.shapesize(stretch_wid=1.5, stretch_len=5)
    restart_button.penup()
    restart_button.goto(100, -50)

  
    restart_text = turtle.Turtle()
    restart_text.penup()
    restart_text.hideturtle()
    restart_text.color("white")
    restart_text.goto(100, -60)
    restart_text.write("RESTART", align="center", font=("Arial", 16, "bold"))

    # Fonction pour détecter le clic sur le bouton Restart
    def on_restart_click(x, y):
        if 50 <= x <= 150 and -65 <= y <= -35:  # Coordonnées du bouton Restart
            turtle.clearscreen()
            initialize()

  # engeristrement
    screen = turtle.Screen()
    screen.onclick(on_quit_click)
    screen.onclick(on_restart_click)

    turtle.done()
if __name__ == "__main__":
    show_menu()
