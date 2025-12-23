#pgzero
import random

WIDTH = 1200
HEIGHT = 600
TITLE = "YILBAŞI GECESİ"
FPS = 30

game_state = 0
story_step = 0

story = [
    "YILBAŞI GECESİ...",
    "Noel baba emekli olmaya karar verdi.",
    "Bu sene hiçbir çocuk hediye alamayacak.",
    "Fakat sen bunu değiştirebilirsin, Noel babayı yakala",
    "ENTER -> BASLA"
]

background = Actor("magicforest", size=(1200, 600))
hero = Actor("anakarakterstand", (70, 525), size=(130, 150))
go = Actor("go", size=(1200, 600))
santa = Actor("santa", (1100, 500), size=(250, 300))
engel = Actor("harbiciagac", (1300, 540), size=(160, 100))
engel2 = Actor("harbiciagac", (1900, 340), size=(160, 100))

count = 0

def draw():
    screen.clear()

    if game_state == 0:
        screen.fill("black")
        screen.draw.text(
            story[story_step],
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=50,
            color="white"
        )
        return

    if game_state == 1:
        background.draw()
        hero.draw()
        santa.draw()
        engel.draw()
        engel2.draw()
        screen.draw.text(str(count), (20, 20), color="white", fontsize=40)

    if game_state == 2:
        go.draw()
        screen.draw.text(
            count,
            center=(WIDTH // 2, HEIGHT - 80),
            fontsize=120,
            color="green"
        )

def update(dt):
    global count, game_state

    if game_state != 1:
        return

    speed = 2
    if hero.x < santa.x and santa.x < 1125:
        santa.x += speed
    elif hero.x > santa.x and santa.x > 85:
        santa.x -= speed

    if hero.y < santa.y and santa.y < 500:
        santa.y += speed
    elif hero.y > santa.y and santa.y > 100:
        santa.y -= speed

    if engel.x > -20:
        engel.x -= 8
    else:
        engel.x = WIDTH + 20

    if engel2.x > -20:
        engel2.x -= 8
    else:
        engel2.x = WIDTH + 20

    if hero.colliderect(santa):
        count += 1
        santa.x = random.randint(100, WIDTH - 100)
        santa.y = random.randint(100, HEIGHT - 100)

    if hero.colliderect(engel) or hero.colliderect(engel2):
        game_state = 2

    if keyboard.left and hero.x > 40:
        hero.image = "anakarakterleft"
        hero.x -= 5
    elif keyboard.right and hero.x < 1160:
        hero.image = "anakarakterright"
        hero.x += 5

def on_key_down(key):
    global story_step, game_state, count
    if game_state == 2 and keyboard.enter:
        game_state = 0 
        hero.pos = (70,525) 
        engel.pos = (1300,540) 
        engel2.pos = (1900,340) 
        santa.pos = (1100,500) 
        count = 0
    if game_state == 0 and keyboard.enter:
        story_step += 1
        if story_step >= len(story):
            game_state = 1
        return
    if keyboard.up:
        hero.image = "anakarakterstand"
        hero.y = 200
        animate(hero, tween='bounce_end', duration=2, y=530)
