import pgzrun
from random import randint

WIDTH  = 600
HEIGHT = 500

score = 0
game_over = False

tom = Actor('tom')

jerry = Actor('jerry')
jerry.pos = 200,200

def draw():
    screen.blit("field", (0,0))
    jerry.draw()
    tom.draw()
    screen.draw.text("Score: "+ str(score), color = "black", topleft = (10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's Up! You final score is "+str(score), midtop = (WIDTH/2,10), color = "red")

def place_jerry():
    jerry.x = randint(70, (WIDTH - 70))
    jerry.y = randint(70, (HEIGHT - 70))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        tom.x = tom.x-2
    if keyboard.right:
        tom.x = tom.x+2
    if keyboard.up:
        tom.y = tom.y-2
    if keyboard.down:
        tom.y = tom.y+2

    jerry_collected = tom.colliderect(jerry)

    if jerry_collected:
        score = score+10
        place_jerry()

clock.schedule(time_up, 15.0)

pgzrun.go()