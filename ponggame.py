import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (204, 204, 204)
DARKRED = (191, 0, 22)
DARKGREEN = (0, 191, 0)
GREY = (207, 207, 207)
 
def draw_ball(screen, x, y):
    img = pygame.image.load('ball.png')
    screen.blit(img, (x,y))
def draw_pad(screen, x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 20, 100])
def winscreen():
    screen.fill(DARKGREEN)
    pygame.draw.rect(screen, GREEN, [50, 50, 650, 400])
def losescreen():
    screen.fill(DARKRED)
    pygame.draw.rect(screen, RED, [50, 50, 650, 400])
def drawscore(x,y,score):
    font = pygame.font.Font("8-bit-hud.ttf", 25)
    text = font.render(str(score) ,True,WHITE)
    screen.blit(text, [x, y])
def drawrect(x, y, l, w):
   pygame.draw.rect(screen, GREY, [x, y, l, w])
pygame.init()
 
size = [750, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

clock = pygame.time.Clock()
 
pygame.mouse.set_visible(0)

play = True
oppx = 710
oppy = 200
padx = 20
pady = 200
x_speed = 3
y_speed = 3
xp_speed = 0
yp_speed = 0
x_coord = 350
y_coord = random.randint(100, 400)
padspeed = 0 
speedset = 2.5
score = 0
win = 0
lose = 0
pygame.mixer.music.load('retro.wav')
pygame.mixer.music.play(-1)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                padspeed = speedset * -1
            elif event.key == pygame.K_DOWN:
                padspeed = speedset
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                padspeed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                padspeed = 0
    
    if x_coord > 664:
        pygame.time.wait(300)
        x_speed = 0
        speedset = 2.5
        win = win + 1
        x_speed = 3
        y_speed = 3
        x_coord = 350
        y_coord = random.randint(100, 400)
    if x_coord < 35:
        pygame.time.wait(300)
        x_speed = 0
        speedset = 2.5
        lose = lose + 1
        x_speed = 3
        y_speed = 3
        x_coord = 350
        y_coord = random.randint(100, 350)
    if y_coord > 450 or y_coord < 0:
        y_speed = y_speed * -1.05
        speedset = speedset * 1.03
    elif x_coord < 40 and pady + 100 > y_coord and pady - 50 < y_coord:
        x_speed = x_speed * -1.05
        speedset = speedset * 1.03
        score += 1
    elif x_coord > 660 and oppy + 100 > y_coord and oppy - 50 < y_coord:
        x_speed = x_speed * -1.05
        speedset = speedset * 1.03
        score += 1
    if pady > 0 and pady < 400:
        pady = pady + padspeed
    elif pady < 1:
        pady = pady + abs(padspeed)
    elif pady > 399:
        pady = pady - abs(padspeed)
    x_coord += x_speed
    y_coord += y_speed
    if oppy + 25 < y_coord:
        oppy = oppy + speedset*0.93
    elif oppy + 25 > y_coord:
        oppy = oppy - speedset*0.93
    if play == True:
        screen.fill(BLACK)
        drawscore(100,100,win)
        drawscore(620,100,lose)
        drawrect(0,0,750,20)
        drawrect(370,0,20,500)
        drawrect(0,480,750,20)
        draw_ball(screen, x_coord, y_coord)
        draw_pad(screen, oppx, oppy)
        draw_pad(screen, padx, pady)
        pygame.display.flip()
        clock.tick(60)
    else:
        screen.fill(WHITE)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Welcome" ,True,WHITE)
        screen.blit(text, [100, 100])

pygame.quit()